from collections import OrderedDict

import numpy as np
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QColor as rgb

from utils.colorTable import mapLabelsToColors
from utils.utils import lettersPen


class ImageProcessWorker(QtCore.QThread):

    trigger = QtCore.Signal(dict)

    def __init__(self):

        super(ImageProcessWorker, self).__init__()

    def setArguments(self,
                     img, msk, temp_msk, opa,
                     foc_pos_2d, point_pos_2d, tool, shift_2d,
                     val_win, val_lev,
                     img_flip, zoom, viewer_size,
                     rai_display_letters
                     ):

        self.args = OrderedDict({
            'img': img,
            'msk': msk,
            'temp_msk': temp_msk,
            'opa': opa,
            'foc_pos_2d': foc_pos_2d,
            'point_pos_2d': point_pos_2d,
            'tool': tool,
            'shift_2d': shift_2d,
            'val_win': val_win,
            'val_lev': val_lev,
            'img_flip': img_flip,
            'zoom': zoom,
            'viewer_size': viewer_size,
            'rai_display_letters': rai_display_letters
        })

    def transform(self, img, msk, temp_msk, foc_pos_2d, point_pos_2d, img_flip):
        img_size = img.shape
        for axis, bool_flip in enumerate(img_flip):
            if bool_flip:
                img = np.flip(img, axis)
                msk = np.flip(msk, axis)
                temp_msk = np.flip(temp_msk, axis)

                foc_pos_2d[axis] = img_size[axis] - foc_pos_2d[axis] - 1
                point_pos_2d[axis] = img_size[axis] - point_pos_2d[axis] - 1

        return img, msk, temp_msk, foc_pos_2d, point_pos_2d

    def mapLabelToRGB(self, msk):

        msk_size = msk.shape
        lbl_ids = np.unique(msk)
        color_obj = mapLabelsToColors(lbl_ids)

        r, g, b = np.zeros(msk_size), np.zeros(msk_size), np.zeros(msk_size)
        for lbl_id in lbl_ids:
            lbl_pos = (msk == lbl_id)
            rgb_vals = color_obj[int(lbl_id)]
            r[lbl_pos] = rgb_vals[0]
            g[lbl_pos] = rgb_vals[1]
            b[lbl_pos] = rgb_vals[2]

        return r, g, b

    def run(self):

        img, msk, temp_msk, opa, foc_pos_2d, point_pos_2d, tool, shift_2d, val_win, val_lev, img_flip, zoom, viewer_size, rai_display_letters = self.args.values()

        val_max = val_lev + val_win / 2
        val_min = val_lev - val_win / 2

        img, msk, temp_msk, foc_pos_2d, point_pos_2d = self.transform(img, msk, temp_msk, foc_pos_2d, point_pos_2d, img_flip)
        img[img > val_max] = val_max
        img[img < val_min] = val_min
        img = (img - val_min)/(val_max-val_min+1e-5)
        img = np.stack([img.T, img.T, img.T], axis=-1)
        msk_pos = (msk > 0).astype(float)
        temp_msk_pos = (temp_msk > 0).astype(float)

        r, g, b = self.mapLabelToRGB(msk)
        msk = np.stack([r.T, g.T, b.T], axis=-1)
        msk_pos = np.stack([r.T, g.T, b.T], axis=-1)

        r, g, b = self.mapLabelToRGB(temp_msk)
        temp_msk = np.stack([r.T, g.T, b.T], axis=-1)
        temp_msk_pos = np.stack([r.T, g.T, b.T], axis=-1)

        img = img * (1. - msk_pos * opa / 100.) + msk * opa / 100.
        img = img * (1. - temp_msk_pos) + temp_msk

        img = (img * 255.).astype('uint8')
        img = Image.fromarray(img, mode='RGB')

        shape = img.size
        size = (round(viewer_size[0]), round(viewer_size[1]))
        zoom_factor = zoom
        foc_pos_2d = [pos*zoom_factor for pos in foc_pos_2d]
        point_pos_2d = [pos*zoom_factor for pos in point_pos_2d]

        newshape = (round(shape[0] * zoom_factor), (round(shape[1] * zoom_factor)))
        margin = ((size[0] - newshape[0]) // 2+shift_2d[0], (size[1] - newshape[1]) // 2+shift_2d[1])
        scaled_img = img.resize(newshape, resample=Image.NEAREST)
        final_img = Image.new(scaled_img.mode, size, color='black')
        final_img.paste(scaled_img, margin)

        spacing = max(zoom_factor, 3)

        imgqt = ImageQt.ImageQt(final_img.convert('RGBA'))
        pixmap = QtGui.QPixmap.fromImage(imgqt)
        
        new_foc = [foc_pos_2d[0]+margin[0], foc_pos_2d[1]+margin[1]]
        new_point = [point_pos_2d[0]+margin[0], point_pos_2d[1]+margin[1]]

        # Tool based curser drawing
        painter = tool.widgetDraw(pixmap, new_foc, new_point, zoom, margin, spacing, newshape)

        # RAI display letters
        painter.setPen(lettersPen(rgb(227, 170, 0)))
        size = 10
        painter.setFont(QtGui.QFont('Robato', size, QtGui.QFont.Bold))
        painter.drawText(pixmap.width()//2-size//2, 15, rai_display_letters[0]) # TOP
        painter.drawText(pixmap.width()-15, pixmap.height()//2+size//2, rai_display_letters[1]) # RIGHT
        painter.drawText(pixmap.width()//2-size//2, pixmap.height()-5, rai_display_letters[2]) # BOT
        painter.drawText(5, pixmap.height()//2+size//2, rai_display_letters[3]) # LEFT

        painter.end()

        self.trigger.emit({'pixmap': pixmap, 'margin': margin})

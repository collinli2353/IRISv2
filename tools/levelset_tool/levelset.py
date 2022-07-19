import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np
from tools.levelset_tool.ChanVese import runChanVese
from tools.levelset_tool.ui_levelset_widget import *
from tools.default_tool import Meta, default_tool
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
from utils.utils import theBrushPen

class levelset(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_levelset_widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()

        self.brush_size = 20
        self.brush_type = 'auto'
        self.brush_dim = '2D'

        def setBrushType(type, dim):
            self.brush_type = type
            self.brush_dim = dim
        
        def setBrushSize(size):
            self.brush_size = size
            self.ui.levelsetSize_label.setText(str(size))

        self.ui.levelsetSize_slider.valueChanged.connect(setBrushSize)
        self.ui.levelset2D_button.clicked.connect(lambda: setBrushType(self.brush_type, '2D'))
        self.ui.levelset3D_button.clicked.connect(lambda: setBrushType(self.brush_type, '3D'))
        self.ui.levelsetAuto_button.clicked.connect(lambda: setBrushType('auto', self.brush_dim))
        self.ui.levelsetLocal_button.clicked.connect(lambda: setBrushType('local', self.brush_dim))

        setBrushType(self.brush_type, self.brush_dim)
        setBrushSize(self.brush_size)

    def normMinMax(self, img, msk=None, p_val=None, ll=0, rr=255):
        new_img = np.zeros(img.shape)
        if msk is not None:
            min_val = np.min(img[msk > 0])
            max_val = np.max(img[msk > 0])
            new_img = (img - min_val) / (max_val - min_val) * (rr-ll) + ll
        else:
            min_val = np.min(img)
            max_val = np.max(img)
            new_img = ((img - min_val) / (max_val - min_val)) * (rr-ll) + ll

        if p_val is not None:
            p_val = (p_val - min_val) / (max_val - min_val) * (rr-ll) + ll

            return new_img, p_val

        return new_img

    def runLevelSet2D(self, img, x_box, y_box, w_box, h_box, x_sel, y_sel, w_sel, h_sel):
        lsf = np.ones((img.shape[0], img.shape[1]), img.dtype)
        if self.brush_type == 'auto':
            pos = np.where(img[x_sel:x_sel+w_sel, y_sel:y_sel+h_sel] == np.amax(img[x_sel:x_sel+w_sel, y_sel:y_sel+h_sel]))
            lsf[pos] = -1
        else:
            lsf[x_sel:x_sel+w_sel, y_sel:y_sel+h_sel] = -1
        lsf = -lsf

        img = img[x_box:x_box+w_box, y_box:y_box+h_box]
        lsf = lsf[x_box:x_box+w_box, y_box:y_box+h_box]

        norm_img = self.normMinMax(img)

        lsf = runChanVese(norm_img, lsf, max_iter=30)

        return (lsf >= 0).astype(float)

    def runLevelSet3D(self, img, x_box, y_box, z_box, w_box, h_box, d_box, x_sel, y_sel, z_sel, w_sel, h_sel, d_sel):
        lsf = np.ones((img.shape[0], img.shape[1], img.shape[2]), img.dtype)
        lsf[x_sel:x_sel+w_sel, y_sel:y_sel+h_sel, z_sel:z_sel+d_sel] = -1
        lsf = -lsf

        img = img[x_box:x_box+w_box, y_box:y_box+h_box, z_box:z_box+d_box]
        lsf = lsf[x_box:x_box+w_box, y_box:y_box+h_box, z_box:z_box+d_box]

        norm_img = self.normMinMax(img)

        lsf = runChanVese(norm_img, lsf, max_iter=30)

        return (lsf >= 0).astype(float)

    def recursive(self, orig_msk, msk, x, y):
        if orig_msk[x, y] == 0 or msk[x, y] == 1:
            return msk

        msk[x, y] = 1
        if x > 0:
            msk = self.recursive(orig_msk, msk, x-1, y)
        if x < msk.shape[0]-1:
            msk = self.recursive(orig_msk, msk, x+1, y)
        if y > 0:
            msk = self.recursive(orig_msk, msk, x, y-1)
        if y < msk.shape[1]-1:
            msk = self.recursive(orig_msk, msk, x, y+1)

        return msk

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        xx, yy, w, h = self.computeCoords(xx, yy, self.brush_size, self.brush_size, margin, self.IMG_OBJ.ZOOM_FACTOR, shape)
        self.IMG_OBJ.POINT_POS = [x, y, z]
        
        if event.buttons() & PySide6.QtCore.Qt.LeftButton:
            ls_msk = None

            if self.brush_dim == '2D':
                if axis == 'axi':
                    ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[:, :, z], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                    if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                    pos = (ls_msk > 0)
                    t_msk = self.MSK_OBJ.MSK[:, :, z]
                    xx, yy = xx-w//2, yy-h//2
                    t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                    self.MSK_OBJ.MSK[:, :, z] = t_msk
                elif axis == 'cor':
                    ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[x, :, :], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                    if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                    pos = (ls_msk > 0)
                    t_msk = self.MSK_OBJ.MSK[x, :, :]
                    xx, yy = xx-w//2, yy-h//2
                    t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                    self.MSK_OBJ.MSK[x, :, :] = t_msk
                elif axis == 'sag':
                    ls_msk = self.runLevelSet2D(self.IMG_OBJ.NP_IMG[:, y, :], xx-w//2, yy-h//2, w, h, xx, yy, 1, 1)
                    if self.brush_type == 'local': ls_msk = self.recursive(ls_msk, np.zeros(ls_msk.shape, dtype=int), ls_msk.shape[0]//2, ls_msk.shape[1]//2)
                    pos = (ls_msk > 0)
                    t_msk = self.MSK_OBJ.MSK[:, y, :]
                    xx, yy = xx-w//2, yy-h//2
                    t_msk[xx:xx+w, yy:yy+h][pos] = self.MSK_OBJ.CURRENT_LBL
                    self.MSK_OBJ.MSK[:, y, :] = t_msk
            
            elif self.brush_dim == '3D':
                w = min(w, h)
                ls_msk = self.runLevelSet3D(self.IMG_OBJ.NP_IMG, x-w//2, y-w//2, z-w//2, w, w, w, x, y, z, 1, 1, 1)
                print(ls_msk.shape)

        elif event.buttons() & PySide6.QtCore.Qt.RightButton:
            if axis == 'axi':
                self.MSK_OBJ.MSK[xx-w//2:xx+w//2, yy-h//2:yy+h//2, z] = 0
            elif axis == 'cor':
                self.MSK_OBJ.MSK[x, xx-w//2:xx+w//2, yy-h//2:yy+h//2] = 0
            elif axis == 'sag':
                self.MSK_OBJ.MSK[xx-w//2:xx+w//2, y, yy-h//2:yy+h//2] = 0

        elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.x(), event.y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theBrushPen(lbl=self.MSK_OBJ.CURRENT_LBL))
        cx, cy = new_point[0], new_point[1]          
        cx, cy = np.round((cx-margin[0])/zoom), np.round((cy-margin[1])/zoom)
        s_x, s_y = cx - self.brush_size // 2, cy - self.brush_size // 2 
        s_x = s_x * zoom + margin[0]
        s_y = s_y * zoom + margin[1]
        w = self.brush_size * zoom
        
        if self.brush_type == 'local':
            painter.drawLine(new_point[0]-5, new_point[1],
                                new_point[0]+5, new_point[1])
            painter.drawLine(new_point[0], new_point[1]-5,
                                new_point[0], new_point[1]+5)

        painter.drawLine(s_x,s_y,s_x+w,s_y)
        painter.drawLine(s_x,s_y,s_x,s_y+w)
        painter.drawLine(s_x+w,s_y+w,s_x,s_y+w)
        painter.drawLine(s_x+w,s_y+w,s_x+w,s_y)

        return painter

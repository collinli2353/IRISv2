import os
import sys

import nibabel as nib
import numpy as np
import PySide6
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets
from qt_material import *

# from qtredux.Component import qtComponent
from ui_MainWindow import *


class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.__initState__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        themes = [
            'dark_amber.xml',
            'dark_blue.xml',
            'dark_cyan.xml',
            'dark_lightgreen.xml',
            'dark_pink.xml',
            'dark_purple.xml',
            'dark_red.xml',
            'dark_teal.xml',
            'dark_yellow.xml',
            'light_amber.xml',
            'light_blue.xml',
            'light_cyan.xml',
            'light_cyan_500.xml',
            'light_lightgreen.xml',
            'light_pink.xml',
            'light_purple.xml',
            'light_red.xml',
            'light_teal.xml',
            'light_yellow.xml'
            ]

        # TODO: have a setting to change the theme
        # apply_stylesheet(app, theme=themes[0])

        # Menubar actions
        self.ui.actionOpen_Image.triggered.connect(self.openImageAction)

        # Toolbar actions
        self.ui.toolbar0_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))   
        self.ui.toolbar1_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.toolbar2_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.toolbar3_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.toolbar4_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.toolbar5_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.toolbar6_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(6))
        self.ui.toolbar7_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(7))
        self.ui.toolbar8_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(8))
        self.ui.toolbar9_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(9))

        # Window actions
        self.ui.single_button.clicked.connect(lambda: self.ui.viewer_stackedWidget.setCurrentIndex(0))
        self.ui.topLeft_button.clicked.connect(lambda: self.ui.viewer_stackedWidget.setCurrentIndex(1))
        self.ui.topRight_button.clicked.connect(lambda: self.ui.viewer_stackedWidget.setCurrentIndex(1))
        self.ui.botLeft_button.clicked.connect(lambda: self.ui.viewer_stackedWidget.setCurrentIndex(1))
        self.ui.botRight_button.clicked.connect(lambda: self.ui.viewer_stackedWidget.setCurrentIndex(1))

        def set_viewer_stackedWidget_index(index):
            self.state['img_obj']['viewer_type'] = index

        self.ui.single_button.clicked.connect(lambda: set_viewer_stackedWidget_index(4))
        self.ui.topLeft_button.clicked.connect(lambda: set_viewer_stackedWidget_index(0))
        self.ui.topRight_button.clicked.connect(lambda: set_viewer_stackedWidget_index(1))
        self.ui.botLeft_button.clicked.connect(lambda: set_viewer_stackedWidget_index(2))
        self.ui.botRight_button.clicked.connect(lambda: set_viewer_stackedWidget_index(3))

        # QLabel actions
        self.ui.topLeft_label.mousePressEvent = self.topLeft_labelMousePressEvent
        self.ui.topRight_label.mousePressEvent = self.topRight_labelMousePressEvent
        self.ui.botLeft_label.mousePressEvent = self.botLeft_labelMousePressEvent
        self.ui.botRight_label.mousePressEvent = self.botRight_labelMousePressEvent

        # QScrollBar actions
        self.ui.topLeft_scrollBar.valueChanged.connect(self.topLeft_scrollBarValueChanged)
        self.ui.topRight_scrollBar.valueChanged.connect(self.topRight_scrollBarValueChanged)
        self.ui.botLeft_scrollBar.valueChanged.connect(self.botLeft_scrollBarValueChanged)
        self.ui.botRight_scrollBar.valueChanged.connect(self.botRight_scrollBarValueChanged)

        self.update()
        self.show()

    def __initState__(self):
        self.state = {
            'img_obj': {
                'img': np.zeros([320, 320, 320]),
                'affine': None,
                'header': None,
                'img_size': (320, 320, 320),
                'min_max': [0, 0],
                'val_win': 0,
                'val_lev': 0,
                'foc_pos': [160, 160, 100],
                'zoom_factor': 1.0,
                'shift': [0, 0, 0],
                'RAIcode': 'LAI',
                'axismapping': None,
                'trans': [0, 0, 0],
                'viewer_type': 4, # 0 - 4 where 0-4 represent axial, coronal, mixed, sagittal & 4 represents multi_viewer 
                'isdicom': False,
            }
        }

    # ================================================== #
    # Menubar Actions ================================== #
    # ================================================== #
    def openImageAction(self):
        fp = self.getValidFilePath()[0]
        if not fp:
            return
        self.openImage(fp)

    def openImage(self, fp):
        img_nii, img_affine, img_header = None, None, None

        # TODO: make work for dcm files
        if fp.split('.')[-1] == 'dcm':
            self.state['img_obj']['isdicom'] = True
        else:
            img_nii = nib.load(fp)
            np_img, img_affine, img_header = img_nii.get_fdata(), img_nii.affine, img_nii.header
            self.state['img_obj']['isdicom'] = False
            # TODO: axismapping to display correctly

        self.state['img_obj']['img'] = np_img
        self.state['img_obj']['affine'] = img_affine
        self.state['img_obj']['header'] = img_header
        self.state['img_obj']['img_size'] = np_img.shape
        self.state['img_obj']['min_max'] = [np_img.min(), np_img.max()]
        self.state['img_obj']['val_win'] = 0
        self.state['img_obj']['val_lev'] = 0
        self.state['img_obj']['foc_pos'] = [int(np_img.shape[0]/2), int(np_img.shape[1]/2), int(np_img.shape[2]/2)]
        self.state['img_obj']['zoom'] = 1.0
        self.state['img_obj']['shift'] = [0, 0, 0]
        # TODO: fix RAIcode
        self.state['img_obj']['RAIcode'] = 'LAI'
        self.state['img_obj']['axismapping'] = None

        self.ui.topLeft_scrollBar.setMinimum(1)
        self.ui.topRight_scrollBar.setMinimum(1)
        self.ui.botRight_scrollBar.setMinimum(1)

        self.ui.topLeft_scrollBar.setMaximum(self.state['img_obj']['img_size'][0])
        self.ui.topRight_scrollBar.setMaximum(self.state['img_obj']['img_size'][1])
        self.ui.botRight_scrollBar.setMaximum(self.state['img_obj']['img_size'][2])

        self.update_scrollBars()
        self.update()
        

    def getValidFilePath(self, prompt='', filter='Default(*.nii *.nii.gz *.dcm);;*.nii.gz;;*.nii;;*dcm;;All Files(*)', is_save=False):
        if is_save:
            func = PySide6.QtWidgets.QFileDialog.getSaveFileName
        else:
            func = PySide6.QtWidgets.QFileDialog.getOpenFileName

        return func(
            self.ui.menubar,
            caption=prompt,
            filter=filter,
        )
    
    # ================================================== #
    # KeyPress Events ================================== #
    # ================================================== #
    def keyPressEvent(self, event):
        print(event.key(), 'pressed')

    def keyReleaseEvent(self, event):
        print(event.key(), 'released')

    def resizeEvent(self, event):
        print('resizedEvent', event)
        self.update_multi_viewer()

    def topLeft_labelMousePressEvent(self, event):
        print('topLeft_labelMousePressEvent', event.x(), event.y())

    def topRight_labelMousePressEvent(self, event):
        print('topRight_labelMousePressEvent', event.x(), event.y())

    def botLeft_labelMousePressEvent(self, event):
        print('botLeft_labelMousePressEvent', event.x(), event.y())

    def botRight_labelMousePressEvent(self, event):
        print('botRight_labelMousePressEvent', event.x(), event.y())

    # ================================================== #
    # Slider Actions =================================== #
    # ================================================== #
    def topLeft_scrollBarValueChanged(self, value):
        self.state['img_obj']['foc_pos'][0] = value-1
        self.update()

    def topRight_scrollBarValueChanged(self, value):
        self.state['img_obj']['foc_pos'][1] = value-1
        self.update()

    def botLeft_scrollBarValueChanged(self, value):
        self.update()

    def botRight_scrollBarValueChanged(self, value):
        self.state['img_obj']['foc_pos'][2] = value-1
        self.update()

    # ================================================== #
    # Update Events ==================================== #
    # ================================================== #
    def update(self):
        if self.state['img_obj']['viewer_type'] == 4:
            self.update_multi_viewer()
        else:
            self.update_single_viewer()
        self.update_scrollBarLabels()

    def update_single_viewer(self):
        print('update_single_viewer', self.state['img_obj']['viewer_type'])

    def update_multi_viewer(self):
        x, y, z = self.state['img_obj']['foc_pos']
        x_img = self.state['img_obj']['img'][x, :, :]
        y_img = self.state['img_obj']['img'][:, y, :]
        z_img = self.state['img_obj']['img'][:, :, z]

        imgs = [x_img, y_img, z_img]

        # All label should be same size
        multi_size = (self.ui.topLeft_frame.width(), self.ui.topLeft_frame.height())
        multi_newshape = (round(multi_size[0] * self.state['img_obj']['zoom_factor']),
                         (round(multi_size[1] * self.state['img_obj']['zoom_factor'])))
        multi_margin = ((multi_size[0] - multi_newshape[0]) // 2+self.state['img_obj']['trans'][0],
                       (multi_size[1] - multi_newshape[1]) // 2+self.state['img_obj']['trans'][1])

        for index in range(len(imgs)):
            i = imgs[index]
            i = np.stack([i.T, i.T, i.T], axis=-1)
            i = (i * 255).astype(np.uint8)
            i = Image.fromarray(i, mode='RGB')
            scaled_img = i.resize(multi_newshape, resample=Image.NEAREST)
            final_img = Image.new(i.mode, multi_size, color='black')
            final_img.paste(scaled_img, multi_margin)
            final_img = ImageQt.ImageQt(final_img.convert('RGBA'))
            imgs[index] = PySide6.QtGui.QPixmap.fromImage(final_img)

        self.ui.topLeft_label.setPixmap(imgs[0])
        self.ui.topRight_label.setPixmap(imgs[1])
        self.ui.botRight_label.setPixmap(imgs[2])

    def update_scrollBars(self):
        self.ui.topLeft_scrollBar.setValue(self.state['img_obj']['foc_pos'][0])
        self.ui.topRight_scrollBar.setValue(self.state['img_obj']['foc_pos'][1])
        self.ui.botRight_scrollBar.setValue(self.state['img_obj']['foc_pos'][2])

    def update_scrollBarLabels(self):        
        self.ui.topLeftZoomToFit_label.setText(str(self.state['img_obj']['foc_pos'][0]) + ' of ' + str(self.state['img_obj']['img_size'][0]))
        self.ui.topRightZoomToFit_label.setText(str(self.state['img_obj']['foc_pos'][1]) + ' of ' + str(self.state['img_obj']['img_size'][1]))
        self.ui.botRightZoomToFit_label.setText(str(self.state['img_obj']['foc_pos'][2]) + ' of ' + str(self.state['img_obj']['img_size'][2]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
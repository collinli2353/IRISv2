import os
import sys

import nibabel as nib
import numpy as np
import PySide2
from PIL import Image, ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from qt_material import *

from qtredux.Component import qtComponent
from ui_MainWindow import *


class MainWindow(qtComponent, PySide2.QtWidgets.QMainWindow):
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
                'zoom': 1.0,
                'shift': [0, 0, 0],
                'RAIcode': 'LAI',
                'axismapping': None,
                'transX': [0, 0, 0],
                'transY': [0, 0, 0],
                'ismain': [False, False, False],
                'isdisplay': [True, True, True],
                'isimgloaded': False,
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

        self.update()
        

    def getValidFilePath(self, prompt='', filter='Default(*.nii *.nii.gz *.dcm);;*.nii.gz;;*.nii;;*dcm;;All Files(*)', is_save=False):
        if is_save:
            func = PySide2.QtWidgets.QFileDialog.getSaveFileName
        else:
            func = PySide2.QtWidgets.QFileDialog.getOpenFileName

        return func(
            self.ui.menubar,
            caption=prompt,
            filter=filter,
        )
    
    # ================================================== #
    # KeyPress Events ================================== #
    # ================================================== #
    def keyPressEvent(self, event):

        self.store.dispatch({
            'type': 'UPDATE_TRIGGER_KEY_PRESSED',
            'key_pressed': event.key(),
        })

    def keyReleaseEvent(self, event):

        self.store.dispatch({
            'type': 'UPDATE_TRIGGER_KEY_RELEASED',
            'key_released': event.key(),
        })

    # ================================================== #
    # Update Events ==================================== #
    # ================================================== #
    def update(self):
        print('update')
        self.update_viewer()

    def update_viewer(self):
        print(self.state)
        x, y, z = self.state['img_obj']['foc_pos']
        x_img = self.state['img_obj']['img'][x, :, :]
        y_img = self.state['img_obj']['img'][:, y, :]
        z_img = self.state['img_obj']['img'][:, :, z]

        x_img = np.stack([x_img.T, x_img.T, x_img.T], axis=-1)
        y_img = np.stack([y_img.T, y_img.T, y_img.T], axis=-1)
        z_img = np.stack([z_img.T, z_img.T, z_img.T], axis=-1)

        x_img = (x_img * 255).astype(np.uint8)
        y_img = (y_img * 255).astype(np.uint8)
        z_img = (z_img * 255).astype(np.uint8)

        x_img = Image.fromarray(x_img, mode='RGB')
        y_img = Image.fromarray(y_img, mode='RGB')
        z_img = Image.fromarray(z_img, mode='RGB')

        x_img = ImageQt.ImageQt(x_img.convert('RGBA'))
        y_img = ImageQt.ImageQt(y_img.convert('RGBA'))
        z_img = ImageQt.ImageQt(z_img.convert('RGBA'))
        
        x_pixmap = PySide2.QtGui.QPixmap.fromImage(x_img)
        y_pixmap = PySide2.QtGui.QPixmap.fromImage(y_img)
        z_pixmap = PySide2.QtGui.QPixmap.fromImage(z_img)

        print('end')

        self.ui.topLeft_graphicsView.setPixmap(x_pixmap)
        self.ui.topRight_graphicsView.setPixmap(y_pixmap)
        self.ui.botRight_graphicsView.setPixmap(z_pixmap)

        self.ui.singleTop_graphicsView.setPixmap(x_pixmap)





        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())



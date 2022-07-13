import os
import sys
from enum import Enum
from tkinter.font import BOLD

import nibabel as nib
import numpy as np
import PySide6
from PIL import Image, ImageQt
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QColor as rgb
from qt_material import *

from dialogs.reorientImageDialog import ReorientImageDialog
# from qtredux.Component import qtComponent
from ui_MainWindow import *
from utils.globalConstants import IMG_OBJ, TOOL_OBJ
from utils.utils import clamp, lettersPen, theCrossPen


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
        self.ui.actionReorient_Image.triggered.connect(self.openReorientDialog)
        self.ui.actionDebug.triggered.connect(self.debug)

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
        def set_viewer_stackedWidget_index(viewerTypeIndex, stackedWidgetIndex):
            self.IMG_OBJ.VIEWER_TYPE = viewerTypeIndex
            self.ui.viewer_stackedWidget.setCurrentIndex(stackedWidgetIndex)

        self.ui.single_button.clicked.connect(lambda: set_viewer_stackedWidget_index(4, 0))
        self.ui.topLeft_button.clicked.connect(lambda: set_viewer_stackedWidget_index(0, 1))
        self.ui.topRight_button.clicked.connect(lambda: set_viewer_stackedWidget_index(1, 1))
        self.ui.botLeft_button.clicked.connect(lambda: set_viewer_stackedWidget_index(2, 1))
        self.ui.botRight_button.clicked.connect(lambda: set_viewer_stackedWidget_index(3, 1))

        # QLabel actions
        # self.ui.topLeft_label.mousePressEvent = self.topLeft_labelMousePressEvent
        # self.ui.topRight_label.mousePressEvent = self.topRight_labelMousePressEvent
        # self.ui.botLeft_label.mousePressEvent = self.botLeft_labelMousePressEvent
        # self.ui.botRight_label.mousePressEvent = self.botRight_labelMousePressEvent

        self.ui.topLeft_label.mouseMoveEvent = self.topLeft_labelMouseMoveEvent
        self.ui.topRight_label.mouseMoveEvent = self.topRight_labelMouseMoveEvent
        self.ui.botLeft_label.mouseMoveEvent = self.botLeft_labelMouseMoveEvent
        self.ui.botRight_label.mouseMoveEvent = self.botRight_labelMouseMoveEvent

        # QScrollBar actions
        self.ui.topLeft_scrollBar.valueChanged.connect(self.topLeft_scrollBarValueChanged)
        self.ui.topRight_scrollBar.valueChanged.connect(self.topRight_scrollBarValueChanged)
        self.ui.botLeft_scrollBar.valueChanged.connect(self.botLeft_scrollBarValueChanged)
        self.ui.botRight_scrollBar.valueChanged.connect(self.botRight_scrollBarValueChanged)

        self.init_scrollBars()
        self.update_scrollBars()
        self.update()
        self.show()

    def __initState__(self):
        self.IMG_OBJ = IMG_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()
        self.reorientDialog = ReorientImageDialog()

    # ================================================== #
    # Menubar Actions ================================== #
    # ================================================== #
    def openImageAction(self):
        fp = self.getValidFilePath()[0]
        if not fp:
            return
        self.openImage(fp)

    def openImage(self, fp):
        self.IMG_OBJ.__loadImage__(fp)

        self.init_scrollBars()
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

    def openReorientDialog(self):
        self.reorientDialog.exec()

    def debug(self):
        print()
        print('==================================================')
        print(self.IMG_OBJ)
        print('==================================================')
        print(self.TOOL_OBJ)
        print('==================================================')

    # ================================================== #
    # KeyPress Events ================================== #
    # ================================================== #
    def keyPressEvent(self, event):
        print(event.key(), 'pressed')

    def keyReleaseEvent(self, event):
        print(event.key(), 'released')

    def resizeEvent(self, event):
        self.update_multi_viewer()

    def topLeft_labelMouseMoveEvent(self, event):
        [x, y, z] = [
            clamp(0, int(event.x()/self.ui.topLeft_label.width()*self.IMG_OBJ.SHAPE[0]), self.IMG_OBJ.SHAPE[0]-1),
            clamp(0, self.IMG_OBJ.SHAPE[1]-1, int(event.y()/self.ui.topLeft_label.height()*self.IMG_OBJ.SHAPE[1])),
            self.IMG_OBJ.FOC_POS[2]
        ]

        [x, y, z] = [
            self.IMG_OBJ.SHAPE[0] - x - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['topLeft'] ][0] else x,
            self.IMG_OBJ.SHAPE[1] - y - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['topLeft'] ][1] else y,
            z
        ]

        if TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                pass

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                pass            

        self.update_scrollBars()
        self.update()

    def topRight_labelMouseMoveEvent(self, event):
        [x, y, z] = [
            self.IMG_OBJ.FOC_POS[0],
            clamp(0, int(event.x()/self.ui.topRight_label.width()*self.IMG_OBJ.SHAPE[1]), self.IMG_OBJ.SHAPE[1]-1),
            clamp(0, int(event.y()/self.ui.topRight_label.height()*self.IMG_OBJ.SHAPE[2]), self.IMG_OBJ.SHAPE[2]-1),
        ]

        [x, y, z] = [
            x,
            self.IMG_OBJ.SHAPE[1] - y - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['topRight'] ][0] else y,
            self.IMG_OBJ.SHAPE[2] - z - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['topRight'] ][1] else z,
        ]

        if TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                pass

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                pass
        

        self.update_scrollBars()
        self.update()

    def botLeft_labelMouseMoveEvent(self, event):
        print('botLeft_labelMousePressEvent', event.x(), event.y())

    def botRight_labelMouseMoveEvent(self, event):
        [x, y, z] = [
            clamp(0, int(event.x()/self.ui.botRight_label.width()*self.IMG_OBJ.SHAPE[0]), self.IMG_OBJ.SHAPE[0]-1),
            self.IMG_OBJ.FOC_POS[1],
            clamp(0, int(event.y()/self.ui.botRight_label.height()*self.IMG_OBJ.SHAPE[2]), self.IMG_OBJ.SHAPE[2]-1),
        ]

        [x, y, z] = [
            self.IMG_OBJ.SHAPE[0] - x - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['botRight'] ][0] else x,
            y,
            self.IMG_OBJ.SHAPE[2] - z - 1 if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING['botRight'] ][1] else z,
        ]

        if TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                pass

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                pass

        self.update_scrollBars()
        self.update()

    # ================================================== #
    # Slider Actions =================================== #
    # ================================================== #
    def topLeft_scrollBarValueChanged(self, value):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']] = value-1
        self.update()

    def topRight_scrollBarValueChanged(self, value):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']] = value-1
        self.update()

    def botLeft_scrollBarValueChanged(self, value):
        self.update()

    def botRight_scrollBarValueChanged(self, value):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']] = value-1
        self.update()

    # ================================================== #
    # Update Events ==================================== #
    # ================================================== #
    def update(self):
        self.update_scrollBarLabels()
        self.update_curserLabels()
        if self.IMG_OBJ.VIEWER_TYPE == 4:
            self.update_multi_viewer()
        else:
            self.update_single_viewer()

    def update_single_viewer(self):
        print('update_single_viewer', self.IMG_OBJ.VIEWER_TYPE)

    # TODO: Multithread this operation
    def update_multi_viewer(self):
        x, y, z = self.IMG_OBJ.FOC_POS
        x_img = self.IMG_OBJ.NP_IMG[x, :, :]
        y_img = self.IMG_OBJ.NP_IMG[:, y, :]
        z_img = self.IMG_OBJ.NP_IMG[:, :, z]

        imgs = [x_img, y_img, z_img]

        # All label should be same size
        multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        multi_newshape = (round(multi_size[0] * self.IMG_OBJ.ZOOM_FACTOR),
                         (round(multi_size[1] * self.IMG_OBJ.ZOOM_FACTOR)))
        

        for index in range(len(imgs)):
            [axisMappingX, axisMappingY] = self.IMG_OBJ.AXISMAPPING[index]

            multi_margin = ((multi_size[0] - multi_newshape[0]) // 2+self.IMG_OBJ.TRANS[axisMappingX],
                            (multi_size[1] - multi_newshape[1]) // 2+self.IMG_OBJ.TRANS[axisMappingY])
            scaled_foc_pos2D = [self.IMG_OBJ.FOC_POS_PERCENT()[axisMappingX] * multi_size[0], self.IMG_OBJ.FOC_POS_PERCENT()[axisMappingY] * multi_size[1]]
            
            # Transform
            ## Flip horizontally
            if self.IMG_OBJ.IMG_FLIP[ self.IMG_OBJ.VIEWER_MAPPING[index] ][0]:
                imgs[index] = np.flipud(imgs[index])

            if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING[index] ][0]:
                scaled_foc_pos2D[0] = multi_size[0] - scaled_foc_pos2D[0]

            ## Flip vertically
            if self.IMG_OBJ.IMG_FLIP[ self.IMG_OBJ.VIEWER_MAPPING[index] ][1]:
                imgs[index] = np.fliplr(imgs[index])

            if self.IMG_OBJ.CURSER_FLIP[ self.IMG_OBJ.VIEWER_MAPPING[index] ][1]:
                scaled_foc_pos2D[1] = multi_size[1] - scaled_foc_pos2D[1]

            i = imgs[index]
            i = np.stack([i.T, i.T, i.T], axis=-1)
            i = (i * 255).astype(np.uint8)
            i = Image.fromarray(i, mode='RGB')
            scaled_img = i.resize(multi_newshape, resample=Image.NEAREST)
            final_img = Image.new(i.mode, multi_size, color='black')
            final_img.paste(scaled_img, multi_margin)
            final_img = ImageQt.ImageQt(final_img.convert('RGBA'))
            pixmap_img = PySide6.QtGui.QPixmap.fromImage(final_img)         

            painter_img = PySide6.QtGui.QPainter(pixmap_img)
            painter_img.setPen(theCrossPen())

            # Draw cross
            painter_img.drawLine(0, scaled_foc_pos2D[1], pixmap_img.width(), scaled_foc_pos2D[1]) # Horizontal
            painter_img.drawLine(scaled_foc_pos2D[0], 0, scaled_foc_pos2D[0], pixmap_img.height()) # Vertical

            painter_img.setPen(lettersPen(rgb(227, 170, 0)))

            # Draw letters
            size = 10
            painter_img.setFont(QtGui.QFont('Robato', size, QFont.Bold))
            painter_img.drawText(pixmap_img.width()//2-size//2, 15, self.IMG_OBJ.RAI_DISPLAY_LETTERS[index][0]) # TOP
            painter_img.drawText(pixmap_img.width()-15, pixmap_img.height()//2+size//2, self.IMG_OBJ.RAI_DISPLAY_LETTERS[index][1]) # RIGHT
            painter_img.drawText(pixmap_img.width()//2-size//2, pixmap_img.height()-5, self.IMG_OBJ.RAI_DISPLAY_LETTERS[index][2]) # BOT
            painter_img.drawText(5, pixmap_img.height()//2+size//2, self.IMG_OBJ.RAI_DISPLAY_LETTERS[index][3]) # LEFT
            
            painter_img.end()

            imgs[index] = pixmap_img


        self.ui.topLeft_label.setPixmap(imgs[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']])
        self.ui.topRight_label.setPixmap(imgs[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']])
        self.ui.botRight_label.setPixmap(imgs[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']])

    def init_scrollBars(self):
        self.ui.topLeft_scrollBar.setMinimum(1)
        self.ui.topRight_scrollBar.setMinimum(1)
        self.ui.botRight_scrollBar.setMinimum(1)

        self.ui.topLeft_scrollBar.setMaximum(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']])
        self.ui.topRight_scrollBar.setMaximum(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']])
        self.ui.botRight_scrollBar.setMaximum(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']])

    def update_scrollBars(self):
        self.ui.topLeft_scrollBar.setValue(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']]+1)
        self.ui.topRight_scrollBar.setValue(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']]+1)
        self.ui.botRight_scrollBar.setValue(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']]+1)

    def update_scrollBarLabels(self):        
        self.ui.topLeftZoomToFit_label.setText(str(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']]+1) + ' of ' + str(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topLeft']]))
        self.ui.topRightZoomToFit_label.setText(str(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']]+1) + ' of ' + str(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['topRight']]))
        self.ui.botRightZoomToFit_label.setText(str(self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']]+1) + ' of ' + str(self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING['botRight']]))

    def update_curserLabels(self):
        self.ui.curserX_label.setNum(self.IMG_OBJ.FOC_POS[0]+1)
        self.ui.curserY_label.setNum(self.IMG_OBJ.FOC_POS[1]+1)
        self.ui.curserZ_label.setNum(self.IMG_OBJ.FOC_POS[2]+1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

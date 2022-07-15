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
from ImageProecessWorker import ImageProcessWorker

from dialogs.reorientImageDialog import ReorientImageDialog
# from qtredux.Component import qtComponent
from ui_MainWindow import *
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
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
        def set_tool(tool_name, index):
            self.TOOL_OBJ.ACTIVE_TOOL_NAME = tool_name
            self.TOOL_OBJ.ACTIVE_TOOL_INDEX = index

        self.ui.toolbar0_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.toolbar0_button.clicked.connect(lambda: set_tool('curser', 0))
        
        self.ui.toolbar1_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.toolbar1_button.clicked.connect(lambda: set_tool('smartclick', 1))

        self.ui.toolbar2_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.toolbar2_button.clicked.connect(lambda: set_tool('levelset', 2))

        self.ui.toolbar3_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.toolbar3_button.clicked.connect(lambda: set_tool('zoom', 3))

        self.ui.toolbar4_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.toolbar4_button.clicked.connect(lambda: set_tool('painter', 4))

        self.ui.toolbar5_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))
        self.ui.toolbar5_button.clicked.connect(lambda: set_tool('toolbar5', 5))

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
        self.ui.topLeft_label.mousePressEvent = self.topLeft_labelMousePressEvent
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
        self.MSK_OBJ = MSK_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()
        self.reorientDialog = ReorientImageDialog()

        self.axi_worker = ImageProcessWorker()
        self.sag_worker = ImageProcessWorker()
        self.cor_worker = ImageProcessWorker()
        self.axi_worker.trigger.connect(self.setAxiPixmap)
        self.sag_worker.trigger.connect(self.setSagPixmap)
        self.cor_worker.trigger.connect(self.setCorPixmap)

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
        self.MSK_OBJ.MSK = np.zeros(self.IMG_OBJ.SHAPE)

        # TODO: new image, new mask, ask prompt to save old mask

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
        print(self.MSK_OBJ)
        print('==================================================')


    # ================================================== #
    # KeyPress Events ================================== #
    # ================================================== #
    def computePosition(self, ev_x, ev_y, zoom, margin, flip, img_size):
        new_x, new_y = ev_x - margin[0], ev_y - margin[1]
        
        new_foc_pos_2d = [new_x, new_y]
        new_foc_pos_2d = [int(pos / zoom) for pos in new_foc_pos_2d]
        new_foc_pos_2d = [clamp(0,val,img_size-1) for val, img_size in zip(new_foc_pos_2d, img_size)]

        for axis, bool_flip in enumerate(flip):
            if bool_flip:
                new_foc_pos_2d[axis] = img_size[axis] - new_foc_pos_2d[axis] - 1
        
        return new_foc_pos_2d

    def keyPressEvent(self, event):
        print(event.key(), 'pressed')

    def keyReleaseEvent(self, event):
        print(event.key(), 'released')

    def resizeEvent(self, event):
        self.update()

    def topLeft_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['axi'] = [event.x(), event.y()]
        self.topLeft_labelMouseMoveEvent(event)

    def topRight_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['sag'] = [event.x(), event.y()]
        self.topRight_labelMouseMoveEvent(event)

    def botRight_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['cor'] = [event.x(), event.y()]
        self.botRight_labelMouseMoveEvent(event)

    def topLeft_labelMouseMoveEvent(self, event):
        [x, y] = self.computePosition(
            event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
            self.IMG_OBJ.MARGIN['axi'],
            self.IMG_OBJ.IMG_FLIP['axi'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[1]]
            )
        [x, y, z] = [x, y, self.IMG_OBJ.FOC_POS[2]]

        if self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                diff = self.TOOL_OBJ.INIT_MOUSE_POS['axi'][1] - event.y()
                self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
                self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                diffX = self.TOOL_OBJ.INIT_MOUSE_POS['axi'][0] - event.x()
                diffY = self.TOOL_OBJ.INIT_MOUSE_POS['axi'][1] - event.y()
                self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]

        elif self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'painter':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.MSK_OBJ.MSK[x, y, z] = self.MSK_OBJ.CURRENT_LBL

        self.TOOL_OBJ.INIT_MOUSE_POS['axi'] = [event.x(), event.y()]

        self.update_scrollBars()
        self.update()

    def topRight_labelMouseMoveEvent(self, event):
        [x, y] = self.computePosition(
            event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
            self.IMG_OBJ.MARGIN['sag'],
            self.IMG_OBJ.IMG_FLIP['sag'], [self.IMG_OBJ.SHAPE[1], self.IMG_OBJ.SHAPE[2]]
            )
        [x, y, z] = [self.IMG_OBJ.FOC_POS[0], x, y]

        if self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                diff = self.TOOL_OBJ.INIT_MOUSE_POS['sag'][1] - event.y()
                self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
                self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                diffX = self.TOOL_OBJ.INIT_MOUSE_POS['sag'][0] - event.x()
                diffY = self.TOOL_OBJ.INIT_MOUSE_POS['sag'][1] - event.y()
                self.IMG_OBJ.SHIFT = [0, self.IMG_OBJ.SHIFT[1] - diffX, self.IMG_OBJ.SHIFT[2] - diffY]

        elif self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'painter':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.MSK_OBJ.MSK[x, y, z] = self.MSK_OBJ.CURRENT_LBL

        self.TOOL_OBJ.INIT_MOUSE_POS['sag'] = [event.x(), event.y()]

        self.update_scrollBars()
        self.update()

    def botLeft_labelMouseMoveEvent(self, event):
        print('botLeft_labelMousePressEvent', event.x(), event.y())

    def botRight_labelMouseMoveEvent(self, event):
        [x, y] = self.computePosition(
            event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
            self.IMG_OBJ.MARGIN['cor'],
            self.IMG_OBJ.IMG_FLIP['cor'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[2]]
            )
        [x, y, z] = [x, self.IMG_OBJ.FOC_POS[1], y]

        if self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'curser':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.IMG_OBJ.FOC_POS = [x, y, z]

            elif event.buttons() & PySide6.QtCore.Qt.RightButton:
                diff = self.TOOL_OBJ.INIT_MOUSE_POS['cor'][1] - event.y()
                self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
                self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

            elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
                diffX = self.TOOL_OBJ.INIT_MOUSE_POS['cor'][0] - event.x()
                diffY = self.TOOL_OBJ.INIT_MOUSE_POS['cor'][1] - event.y()
                self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, 0, self.IMG_OBJ.SHIFT[2] - diffY]

        elif self.TOOL_OBJ.ACTIVE_TOOL_NAME == 'painter':
            if event.buttons() & PySide6.QtCore.Qt.LeftButton:
                self.MSK_OBJ.MSK[x, y, z] = self.MSK_OBJ.CURRENT_LBL

        self.TOOL_OBJ.INIT_MOUSE_POS['cor'] = [event.x(), event.y()]

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
            # All label should be same size

            self.update_multi_viewer()
        else:
            self.update_single_viewer()

    def update_single_viewer(self):
        print('update_single_viewer', self.IMG_OBJ.VIEWER_TYPE)

    def update_multi_viewer(self):
        x, y, z = self.IMG_OBJ.FOC_POS
        multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        self.axi_worker.setArguments(
            self.IMG_OBJ.NP_IMG[:, :, z], self.MSK_OBJ.MSK[:, :, z], self.MSK_OBJ.OPA,
            [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][1]]], [0, 0],
            self.IMG_OBJ.WINDOW_LEVEL, self.IMG_OBJ.LEVEL_VALUE, self.IMG_OBJ.IMG_FLIP['axi'], self.IMG_OBJ.ZOOM_FACTOR, 
            multi_size,
        )
        self.sag_worker.setArguments(
            self.IMG_OBJ.NP_IMG[x, :, :], self.MSK_OBJ.MSK[x, :, :], self.MSK_OBJ.OPA,
            [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][1]]], [0, 0],
            self.IMG_OBJ.WINDOW_LEVEL, self.IMG_OBJ.LEVEL_VALUE, self.IMG_OBJ.IMG_FLIP['sag'], self.IMG_OBJ.ZOOM_FACTOR, 
            multi_size,
        )
        self.cor_worker.setArguments(
            self.IMG_OBJ.NP_IMG[:, y, :], self.MSK_OBJ.MSK[:, y, :], self.MSK_OBJ.OPA,
            [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][1]]], [0, 0],
            self.IMG_OBJ.WINDOW_LEVEL, self.IMG_OBJ.LEVEL_VALUE, self.IMG_OBJ.IMG_FLIP['cor'], self.IMG_OBJ.ZOOM_FACTOR, 
            multi_size,
        )
        self.axi_worker.start()
        self.sag_worker.start()
        self.cor_worker.start()

    def setAxiPixmap(self, obj):
        pixmap = obj['pixmap']
        self.IMG_OBJ.MARGIN['axi'] = obj['margin']
        self.ui.topLeft_label.setPixmap(pixmap)

    def setSagPixmap(self, obj):
        pixmap = obj['pixmap']
        self.IMG_OBJ.MARGIN['sag'] = obj['margin']
        self.ui.topRight_label.setPixmap(pixmap)
        
    def setCorPixmap(self, obj):
        pixmap = obj['pixmap']
        self.IMG_OBJ.MARGIN['cor'] = obj['margin']
        self.ui.botRight_label.setPixmap(pixmap)

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

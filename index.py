from collections import OrderedDict
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
from imageProcessWorker import ImageProcessWorker

from dialogs.reorientImageDialog import ReorientImageDialog
from tools.brush_tool.brush import brush
from tools.curser_tool.curser import curser
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

        self.tools = OrderedDict({
            'curser': curser(),
            'brush': brush(),
        })

        self.tool_buttons = OrderedDict({
            'curser': self.ui.toolbar0_button,
            'brush': self.ui.toolbar1_button,
        })

        # Menubar actions
        self.ui.actionOpen_Image.triggered.connect(self.openImageAction)
        self.ui.actionSave_As.triggered.connect(self.saveAsImageAction)
        self.ui.actionReorient_Image.triggered.connect(self.openReorientDialog)
        self.ui.actionDebug.triggered.connect(self.debug)

        # Toolbar actions
        def set_tool(index, tool_name):
            self.TOOL_OBJ.ACTIVE_TOOL_NAME = tool_name
            self.TOOL_OBJ.ACTIVE_TOOL_INDEX = index
            print('switching tool to', tool_name, index)

        for index, tool_name in enumerate(self.tools):
            self.ui.stackedWidget.addWidget(self.tools[tool_name])

        self.tool_buttons['curser'].clicked.connect(lambda: set_tool(0, 'curser'))
        self.tool_buttons['curser'].clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.tool_buttons['curser'].clicked.connect(lambda: self.update())

        self.tool_buttons['brush'].clicked.connect(lambda: set_tool(1, 'brush'))
        self.tool_buttons['brush'].clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.tool_buttons['brush'].clicked.connect(lambda: self.update())

        # Window actions
        def show_all_frames():
            self.ui.topLeft_frame.show()
            self.ui.topRight_frame.show()
            self.ui.botLeft_frame.show()
            self.ui.botRight_frame.show()
            self.IMG_OBJ.VIEWER_TYPE = 4

        def show_topLeft_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.show()
                self.ui.topRight_frame.hide()
                self.ui.botLeft_frame.hide()
                self.ui.botRight_frame.hide()
                self.IMG_OBJ.VIEWER_TYPE = 0
            else:
                show_all_frames()
                

        def show_topRight_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.show()
                self.ui.botLeft_frame.hide()
                self.ui.botRight_frame.hide()
                self.IMG_OBJ.VIEWER_TYPE = 1
            else:
                show_all_frames()

        def show_botLeft_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.hide()
                self.ui.botLeft_frame.show()
                self.ui.botRight_frame.hide()
                self.IMG_OBJ.VIEWER_TYPE = 2
            else:
                show_all_frames()

        def show_botRight_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.hide()
                self.ui.botLeft_frame.hide()
                self.ui.botRight_frame.show()
                self.IMG_OBJ.VIEWER_TYPE = 3
            else:
                show_all_frames()

        self.ui.topLeft_label.setMouseTracking(True)
        self.ui.topRight_label.setMouseTracking(True)
        self.ui.botLeft_label.setMouseTracking(True)
        self.ui.botRight_label.setMouseTracking(True)
                
        self.ui.topLeft_button.clicked.connect(lambda: show_topLeft_frame())
        self.ui.topRight_button.clicked.connect(lambda: show_topRight_frame())
        self.ui.botLeft_button.clicked.connect(lambda: show_botLeft_frame())
        self.ui.botRight_button.clicked.connect(lambda: show_botRight_frame())

        def zoom_to_fit(axismapping):
            x, y = axismapping
            multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
            zoom_x = multi_size[0] / self.IMG_OBJ.SHAPE[x]
            zoom_y = multi_size[1] / self.IMG_OBJ.SHAPE[y] 
            self.IMG_OBJ.ZOOM_FACTOR = min(zoom_x, zoom_y)
            self.IMG_OBJ.SHIFT = [0, 0, 0]
            self.update()

        self.ui.topLeftZoomToFit_button.clicked.connect(lambda: zoom_to_fit(self.IMG_OBJ.AXISMAPPING['axi']))
        self.ui.topRightZoomToFit_button.clicked.connect(lambda: zoom_to_fit(self.IMG_OBJ.AXISMAPPING['sag']))
        self.ui.botRightZoomToFit_button.clicked.connect(lambda: zoom_to_fit(self.IMG_OBJ.AXISMAPPING['cor']))

        # QLabel actions
        self.ui.topLeft_label.mousePressEvent = self.topLeft_labelMousePressEvent
        self.ui.topRight_label.mousePressEvent = self.topRight_labelMousePressEvent
        self.ui.botLeft_label.mousePressEvent = self.botLeft_labelMousePressEvent
        self.ui.botRight_label.mousePressEvent = self.botRight_labelMousePressEvent

        self.ui.topLeft_label.mouseMoveEvent = self.topLeft_labelMouseMoveEvent
        self.ui.topRight_label.mouseMoveEvent = self.topRight_labelMouseMoveEvent
        self.ui.botLeft_label.mouseMoveEvent = self.botLeft_labelMouseMoveEvent
        self.ui.botRight_label.mouseMoveEvent = self.botRight_labelMouseMoveEvent

        self.ui.topLeft_label.wheelEvent = self.topLeft_labelWheelEvent
        self.ui.topRight_label.wheelEvent = self.topRight_labelWheelEvent
        self.ui.botLeft_label.wheelEvent = self.botLeft_labelWheelEvent
        self.ui.botRight_label.wheelEvent = self.botRight_labelWheelEvent

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
        fp = self.getValidFilePath(prompt='Open Image', is_save=False)[0]
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

    def saveAsImageAction(self):
        fp = self.getValidFilePath(prompt='Save Image', filter='*.nii.gz;;*.nii', is_save=True)[0]
        print('Saving image to:', fp)
        if not fp:
            return
        
        msk_nib = nib.Nifti1Image(self.MSK_OBJ.MSK, self.IMG_OBJ.AFFINE, self.IMG_OBJ.HEADER)
        nib.save(msk_nib, fp)

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

    def botLeft_labelMousePressEvent(self, event):
        pass

    def botRight_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['cor'] = [event.x(), event.y()]
        self.botRight_labelMouseMoveEvent(event)

    def labelMouseMoveEvent(self, event, axis):
        self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME].widgetMouseMoveEvent(event, axis)
        self.update_scrollBars()
        self.update()

    def topLeft_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'axi')
    def topRight_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'sag')
    def botLeft_labelMouseMoveEvent(self, event): pass
    def botRight_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'cor')

    # ================================================== #
    # Wheel Event ====================================== #
    # ================================================== #
    def increaseFocPos(self, axis):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] = clamp(0, self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] + 1, self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1)

    def decreaseFocPos(self, axis):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] = clamp(0, self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1, self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1)

    def topLeft_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.decreaseFocPos('topLeft')
        else:
            self.increaseFocPos('topLeft')

        self.update_scrollBars()
        self.update()

    def topRight_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.decreaseFocPos('topRight')
        else:
            self.increaseFocPos('topRight')

        self.update_scrollBars()
        self.update()

    def botLeft_labelWheelEvent(self, event):
        print('botLeft_labelWheelEvent', event.angleDelta())

    def botRight_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.decreaseFocPos('botRight')
        else:
            self.increaseFocPos('botRight')

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

        self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME].widgetUpdate()

        self.update_viewers()

    def update_viewers(self):
        x, y, z = self.IMG_OBJ.FOC_POS

        multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        if self.IMG_OBJ.VIEWER_TYPE == 4:
            multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        self.axi_worker.setArguments(
            img = self.IMG_OBJ.NP_IMG[:, :, z],
            msk = self.MSK_OBJ.MSK[:, :, z],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            val_win = self.IMG_OBJ.WINDOW_LEVEL,
            val_lev = self.IMG_OBJ.LEVEL_VALUE,
            img_flip = self.IMG_OBJ.IMG_FLIP['axi'],
            zoom = self.IMG_OBJ.ZOOM_FACTOR, 
            viewer_size = multi_size,
            rai_display_letters = self.IMG_OBJ.RAI_DISPLAY_LETTERS[2]
        )
        multi_size = (self.ui.topRight_frame.width()-self.ui.topRight_scrollBar.width(), self.ui.topRight_frame.height()-self.ui.topLeftZoomToFit_button.height())
        if self.IMG_OBJ.VIEWER_TYPE == 4:
            multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        self.sag_worker.setArguments(
            img = self.IMG_OBJ.NP_IMG[x, :, :],
            msk = self.MSK_OBJ.MSK[x, :, :],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            val_win = self.IMG_OBJ.WINDOW_LEVEL,
            val_lev = self.IMG_OBJ.LEVEL_VALUE,
            img_flip = self.IMG_OBJ.IMG_FLIP['sag'],
            zoom = self.IMG_OBJ.ZOOM_FACTOR, 
            viewer_size = multi_size,
            rai_display_letters = self.IMG_OBJ.RAI_DISPLAY_LETTERS[0]
        )
        multi_size = (self.ui.botRight_frame.width()-self.ui.botRight_scrollBar.width(), self.ui.botRight_frame.height()-self.ui.botRightZoomToFit_button.height())
        if self.IMG_OBJ.VIEWER_TYPE == 4:
            multi_size = (self.ui.topLeft_frame.width()-self.ui.topLeft_scrollBar.width(), self.ui.topLeft_frame.height()-self.ui.topLeftZoomToFit_button.height())
        self.cor_worker.setArguments(
            img = self.IMG_OBJ.NP_IMG[:, y, :],
            msk = self.MSK_OBJ.MSK[:, y, :],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            val_win = self.IMG_OBJ.WINDOW_LEVEL,
            val_lev = self.IMG_OBJ.LEVEL_VALUE,
            img_flip = self.IMG_OBJ.IMG_FLIP['cor'],
            zoom = self.IMG_OBJ.ZOOM_FACTOR, 
            viewer_size = multi_size,
            rai_display_letters = self.IMG_OBJ.RAI_DISPLAY_LETTERS[1]
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

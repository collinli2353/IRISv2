import sys
from collections import OrderedDict

import nibabel as nib
import numpy as np
import PySide6
from qt_material import *

from dialogs.reorientImageDialog import ReorientImageDialog
from imageProcessWorker import ImageProcessWorker
from tools.brainLesionCNN_tool.brainLesionCNN import brainLesionCNN
from tools.brush_tool.brush import brush
from tools.curser_tool.curser import curser
from tools.levelset_tool.levelset import levelset
from tools.smartclickCNN_tool.smartclickCNN import smartclickCNN
from tools.smartclickLevelset_tool.smartclickLevelset import smartclickLevelset
from ui_MainWindow import *
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
from utils.utils import clamp

class MainWindow(PySide6.QtWidgets.QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.__initState__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setAcceptDrops(True)

        self.theme_index = 0

        self.tools = OrderedDict({
            'curser': curser(),
            'brush': brush(),
            'levelset': levelset(),
            'brainLesionCNN': brainLesionCNN(),
            'smartclickCNN': smartclickCNN(),
            'smartclickLevelset': smartclickLevelset(),
        })

        self.tool_buttons = OrderedDict({
            'curser': self.ui.toolbar0_button,
            'brush': self.ui.toolbar1_button,
            'levelset': self.ui.toolbar2_button,
            'brainLesionCNN': self.ui.toolbar3_button,
            'smartclickCNN': self.ui.toolbar4_button,
            'smartclickLevelset': self.ui.toolbar5_button,
        })

        # Toolbar actions
        def set_tool(index, tool_name):
            self.TOOL_OBJ.ACTIVE_TOOL_NAME = tool_name
            self.TOOL_OBJ.ACTIVE_TOOL_INDEX = index
            self.ui.stackedWidget.setCurrentIndex(index)
            self.update()
            print('switching tool to', tool_name, index)

        for index, tool_name in enumerate(self.tools):
            self.ui.stackedWidget.addWidget(self.tools[tool_name])

        self.tool_buttons['curser'].clicked.connect(lambda: set_tool(0, 'curser'))
        self.tool_buttons['brush'].clicked.connect(lambda: set_tool(1, 'brush'))
        self.tool_buttons['levelset'].clicked.connect(lambda: set_tool(2, 'levelset'))
        self.tool_buttons['brainLesionCNN'].clicked.connect(lambda: set_tool(3, 'brainLesionCNN'))
        self.tool_buttons['smartclickCNN'].clicked.connect(lambda: set_tool(4, 'smartclickCNN'))
        self.tool_buttons['smartclickLevelset'].clicked.connect(lambda: set_tool(5, 'smartclickLevelset'))

        # Menubar actions
        self.ui.actionOpen_Image.triggered.connect(self.openImageAction)
        self.ui.actionOpen_Segmentation.triggered.connect(self.openSegmentationAction)
        self.ui.actionSave_As.triggered.connect(self.saveAsImageAction)
        self.ui.actionUndo.triggered.connect(self.undoAction)
        self.ui.actionRedo.triggered.connect(self.redoAction)
        self.ui.actionReorient_Image.triggered.connect(self.openReorientDialog)
        self.ui.actionDebug.triggered.connect(self.debug)
        self.ui.actionSelect_Theme.triggered.connect(self.selectTheme)

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
            else: show_all_frames()
                
        def show_topRight_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.show()
                self.ui.botLeft_frame.hide()
                self.ui.botRight_frame.hide()
                self.IMG_OBJ.VIEWER_TYPE = 1
            else: show_all_frames()

        def show_botLeft_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.hide()
                self.ui.botLeft_frame.show()
                self.ui.botRight_frame.hide()
                self.IMG_OBJ.VIEWER_TYPE = 2
            else: show_all_frames()

        def show_botRight_frame():
            if self.IMG_OBJ.VIEWER_TYPE == 4:
                self.ui.topLeft_frame.hide()
                self.ui.topRight_frame.hide()
                self.ui.botLeft_frame.hide()
                self.ui.botRight_frame.show()
                self.IMG_OBJ.VIEWER_TYPE = 3
            else: show_all_frames()

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

        self.ui.topLeft_label.mouseReleaseEvent = self.labelMouseReleaseevent
        self.ui.topRight_label.mouseReleaseEvent = self.labelMouseReleaseevent
        self.ui.botLeft_label.mouseReleaseEvent = self.labelMouseReleaseevent
        self.ui.botRight_label.mouseReleaseEvent = self.labelMouseReleaseevent

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

        # QSlider actions
        self.ui.segOpa_slider.valueChanged.connect(self.opa_sliderValueChanged)

        # Segmentation Label Actions
        self.ui.segActiveLabel_combobox.addItems(['Label ' + str(i) for i in self.MSK_OBJ.LBL_IDS])
        self.ui.segActiveLabel_combobox.setCurrentIndex(len(self.MSK_OBJ.LBL_IDS)-1)
        self.ui.segActiveLabel_combobox.currentIndexChanged.connect(self.segActiveLabelChanged)
        
        self.ui.segAddLabel_button.clicked.connect(self.segAddLabelPressed)
        self.ui.segRemoveLabel_button.clicked.connect(self.segRemoveLabelPressed)

        self.init_scrollBars()
        self.update_scrollBars()
        self.update()
        self.show()

    def __initState__(self):
        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()
        self.reorientDialog = ReorientImageDialog()

        self.IMG_OBJ.UPDATE_VIEWERS = self.update_viewers

        self.axi_worker = ImageProcessWorker()
        self.sag_worker = ImageProcessWorker()
        self.cor_worker = ImageProcessWorker()
        self.axi_worker.trigger.connect(self.setAxiPixmap)
        self.sag_worker.trigger.connect(self.setSagPixmap)
        self.cor_worker.trigger.connect(self.setCorPixmap)

    # ================================================== #
    # Menubar Actions ================================== #
    # ================================================== #
    def prompt(self, title='', msg='', msg2='', detail='', buttons=[], default: str=None, icon=PySide6.QtWidgets.QMessageBox.NoIcon):
        
        msgbox = PySide6.QtWidgets.QMessageBox(self)
        msgbox.setWindowTitle(title)
        msgbox.setText(msg)
        msg2 and msgbox.setInformativeText(msg2)
        detail and msgbox.setDetailedText(detail)
        for btntxt, btnrole in buttons: msgbox.addButton(btntxt, btnrole)
        icon and msgbox.setIcon(icon)
        response = ['']
        msgbox.buttonClicked.connect(lambda btn: response.__setitem__(0, btn.text()))
        msgbox.exec()
    
        return response

    def openImageAction(self):
        fp = self.getValidFilePath(prompt='Open Image', is_save=False)[0]
        if not fp:
            return
        self.openImage(fp)

    def openImage(self, fp):
        if self.MSK_OBJ.MSK.sum() > 0:
            ret = PySide6.QtWidgets.QMessageBox.question(self, '', 'Have you saved your current mask?' , PySide6.QtWidgets.QMessageBox.Yes | PySide6.QtWidgets.QMessageBox.No)

            if ret == PySide6.QtWidgets.QMessageBox.No:
                return
        self.IMG_OBJ.__loadImage__(fp)

        # TODO: new image, new mask, ask prompt to save old mask
        self.MSK_OBJ.MSK = np.zeros(self.IMG_OBJ.SHAPE)
        self.MSK_OBJ.TEMP_MSK = np.zeros(self.IMG_OBJ.SHAPE)

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

    def openSegmentationAction(self):
        fp = self.getValidFilePath(prompt='Open Image', is_save=False)[0]
        if not fp:
            return

        self.openSegmentation(fp)

    def openSegmentation(self, fp):
        msk = nib.load(fp).get_fdata()
        self.MSK_OBJ.newMsk(msk)
        self.ui.segActiveLabel_combobox.clear()
        self.ui.segActiveLabel_combobox.addItems(['Label ' + str(i) for i in self.MSK_OBJ.LBL_IDS])
        self.ui.segActiveLabel_combobox.setCurrentIndex(len(self.MSK_OBJ.LBL_IDS)-1)

    def saveAsImageAction(self):
        fp = self.getValidFilePath(prompt='Save Image', filter='*.nii.gz;;*.nii', is_save=True)[0]
        print('Saving image to:', fp)
        if not fp:
            return
        
        msk_nib = nib.Nifti1Image(self.MSK_OBJ.MSK, self.IMG_OBJ.AFFINE, self.IMG_OBJ.HEADER)
        nib.save(msk_nib, fp)

    def undoAction(self):
        self.MSK_OBJ.undo()
        self.update()

    def redoAction(self):
        self.MSK_OBJ.redo()
        self.update()

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

    def selectTheme(self):
        themes = [
            'light',
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

        self.theme_index = (self.theme_index + 1) % len(themes)
        apply_stylesheet(app, theme=themes[self.theme_index])

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
        self.TOOL_OBJ.INIT_MOUSE_POS['axi'] = [event.position().x(), event.position().y()]
        self.topLeft_labelMouseMoveEvent(event)

    def topRight_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['sag'] = [event.position().x(), event.position().y()]
        self.topRight_labelMouseMoveEvent(event)

    def botLeft_labelMousePressEvent(self, event):
        pass

    def botRight_labelMousePressEvent(self, event):
        self.TOOL_OBJ.INIT_MOUSE_POS['cor'] = [event.position().x(), event.position().y()]
        self.botRight_labelMouseMoveEvent(event)

    def labelMouseReleaseevent(self, event):
        if self.TOOL_OBJ.ACTIVE_TOOL_NAME != 'curser': self.MSK_OBJ.updateMaskManager(self.MSK_OBJ.MSK)

    def labelMouseMoveEvent(self, event, axis):
        self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME].widgetMouseMoveEvent(event, axis)
        self.update_scrollBars()
        self.update()

    def topLeft_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'axi')
    def topRight_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'sag')
    def botLeft_labelMouseMoveEvent(self, event): pass
    def botRight_labelMouseMoveEvent(self, event): self.labelMouseMoveEvent(event, 'cor')


    def dropEvent(self, event):
        event.accept()
        fp = event.mimeData().urls()[0].toLocalFile()

        (res,) = self.prompt(
            title='Load Image',
            msg='Which should be done with this image?',
            detail=fp,
            buttons=[
                ('Load as Main Image', PySide6.QtWidgets.QMessageBox.AcceptRole),
                ('Load as Segmentation', PySide6.QtWidgets.QMessageBox.AcceptRole),
                ('Cancel', PySide6.QtWidgets.QMessageBox.RejectRole),
            ], default='Load as Main Image'
        )

        if res in ('Cancel', ''):
            return
        elif res in ('Load as Main Image',''):
            self.openImage(fp)
        elif res in ('Load as Segmentation',''):
            self.openSegmentation(fp)

    def dragEnterEvent(self, event): event.accept()

    # ================================================== #
    # Wheel Event ====================================== #
    # ================================================== #
    def increaseFocPos(self, axis):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] = clamp(0, self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] + 1, self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1)

    def decreaseFocPos(self, axis):
        self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] = clamp(0, self.IMG_OBJ.FOC_POS[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1, self.IMG_OBJ.SHAPE[self.IMG_OBJ.VIEWER_INDEX_MAPPING[axis]] - 1)

    def topLeft_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0: self.decreaseFocPos('topLeft')
        else: self.increaseFocPos('topLeft')

        self.update_scrollBars()
        self.update()

    def topRight_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0: self.decreaseFocPos('topRight')
        else: self.increaseFocPos('topRight')

        self.update_scrollBars()
        self.update()

    def botLeft_labelWheelEvent(self, event):
        print('botLeft_labelWheelEvent', event.angleDelta())

    def botRight_labelWheelEvent(self, event):
        if event.angleDelta().y() > 0: self.decreaseFocPos('botRight')
        else: self.increaseFocPos('botRight')

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
    # Label Events ==================================== #
    # ================================================== #
    def opa_sliderValueChanged(self, value):
        self.MSK_OBJ.OPA = value
        self.ui.segOpa_label.setText(str(value))
        self.update()

    def segActiveLabelChanged(self, index):
        self.MSK_OBJ.CURRENT_LBL = int(self.ui.segActiveLabel_combobox.currentText().split(' ')[-1])
        self.update()

    def segAddLabelPressed(self):
        self.MSK_OBJ.addLabel()
        self.ui.segActiveLabel_combobox.addItem('Label ' + str(self.MSK_OBJ.LBL_IDS[-1]))
        self.ui.segActiveLabel_combobox.setCurrentIndex(len(self.MSK_OBJ.LBL_IDS)-1)
        self.update()

    def segRemoveLabelPressed(self):
        self.ui.segActiveLabel_combobox.removeItem(self.ui.segActiveLabel_combobox.currentIndex())
        self.MSK_OBJ.removeLabel()


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
            img = self.IMG_OBJ.ORIG_NP_IMG[:, :, z].copy(),
            msk = self.MSK_OBJ.MSK[:, :, z],
            temp_msk = self.MSK_OBJ.TEMP_MSK[:, :, z],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['axi'][1]]],
            val_win = self.IMG_OBJ.WINDOW_VALUE,
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
            img = self.IMG_OBJ.ORIG_NP_IMG[x, :, :].copy(),
            msk = self.MSK_OBJ.MSK[x, :, :],
            temp_msk = self.MSK_OBJ.TEMP_MSK[x, :, :],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['sag'][1]]],
            val_win = self.IMG_OBJ.WINDOW_VALUE,
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
            img = self.IMG_OBJ.ORIG_NP_IMG[:, y, :].copy(),
            msk = self.MSK_OBJ.MSK[:, y, :],
            temp_msk = self.MSK_OBJ.TEMP_MSK[:, y, :],
            opa = self.MSK_OBJ.OPA,
            foc_pos_2d = [self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.FOC_POS[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            point_pos_2d = [self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.POINT_POS[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            tool = self.tools[self.TOOL_OBJ.ACTIVE_TOOL_NAME],
            shift_2d = [self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][0]], self.IMG_OBJ.SHIFT[self.IMG_OBJ.AXISMAPPING['cor'][1]]],
            val_win = self.IMG_OBJ.WINDOW_VALUE,
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
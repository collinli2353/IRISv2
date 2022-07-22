import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from tools.brainLesionCNN_tool.CNN.run_segmentation import run_segmentation
from tools.brainLesionCNN_tool.CNN.run_separation import run_separation
from tools.brainLesionCNN_tool.ui_brainLesionCNN_widget import *
from tools.default_tool import Meta, default_tool
from utils.globalConstants import IMG_OBJ, MSK_OBJ

class brainLesionCNN(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_brainLesionCNN_widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()

        self.t1_fp = None
        self.t2_fp = None
        self.tl_fp = None

        self.ui.segment_button.clicked.connect(self.segment_button_clicked)
        self.ui.separate_button.clicked.connect(self.separate_button_clicked)
        self.ui.t1_button.clicked.connect(self.t1_button_clicked)
        self.ui.t2_button.clicked.connect(self.t2_button_clicked)
        self.ui.fl_button.clicked.connect(self.fl_button_clicked)

    def getValidFilePath(self, prompt='', filter='Default(*.nii *.nii.gz *.dcm);;*.nii.gz;;*.nii;;*dcm;;All Files(*)', is_save=False):
        if is_save:
            func = PySide6.QtWidgets.QFileDialog.getSaveFileName
        else:
            func = PySide6.QtWidgets.QFileDialog.getOpenFileName

        return func(
            caption=prompt,
            filter=filter,
        )

    def segment_button_clicked(self):
        self.IMG_OBJ.__loadImage__(self.tl_fp)
        self.MSK_OBJ.newMsk(run_segmentation(self.t1_fp, self.t2_fp, self.tl_fp, './models/seg_model.pth'))

    def separate_button_clicked(self):
        self.IMG_OBJ.__loadImage__(self.tl_fp)
        self.MSK_OBJ.newMsk(run_separation(self.t1_fp, self.t2_fp, self.tl_fp, self.MSK_OBJ.MSK, './models/sep_model.pth'))

    def t1_button_clicked(self):
        self.t1_fp = self.getValidFilePath(prompt='Select T1 image')[0]
        self.ui.t1_button.setText('Replace t1 image')

    def t2_button_clicked(self):
        self.t2_fp = self.getValidFilePath(prompt='Select T2 image')[0]
        self.ui.t2_button.setText('Replace t2 image')

    def fl_button_clicked(self):
        self.tl_fp = self.getValidFilePath(prompt='Select FL image')[0]
        self.ui.fl_button.setText('Replace fl image')
    
    def widgetMouseMoveEvent(self, event, axis):
        pass

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        return painter

    def widgetUpdate(self):
        pass
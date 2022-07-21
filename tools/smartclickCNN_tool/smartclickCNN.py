import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np
from tools.default_tool import Meta, default_tool
from tools.smartclickCNN_tool.CNN.tool import tool
from tools.smartclickCNN_tool.ui_smartclickCNN import *
from utils.globalConstants import IMG_OBJ, MSK_OBJ
from utils.utils import theBrushPen

class smartclickCNN(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_smartclickCNN_widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()

        self.tool = tool()

        self.reset()

        self.ui.segment_button.clicked.connect(self.segment)

    def reset(self):
        self.segmentation_seeds = []
        self.background_seeds = []
        self.foreground_seeds = []
        self.MSK_OBJ.TEMP_MSK = np.zeros_like(self.IMG_OBJ.NP_IMG)

    def segment(self):
        pred = self.tool.perform_segmentation(self.IMG_OBJ.NP_IMG[:, :, self.IMG_OBJ.FOC_POS[2]], self.segmentation_seeds)
        pos = (pred > 0)
        self.MSK_OBJ.MSK[:, :, self.IMG_OBJ.FOC_POS[2]][pos] = self.MSK_OBJ.CURRENT_LBL
        self.reset()

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        self.IMG_OBJ.POINT_POS = [x, y, z]

        if event.buttons() & PySide6.QtCore.Qt.LeftButton:
            if axis == 'axi':
                self.segmentation_seeds.append((xx, yy))
                self.MSK_OBJ.TEMP_MSK[x, y, z] = 2

                
    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theBrushPen(lbl=self.MSK_OBJ.CURRENT_LBL))
        
        painter.drawLine(new_point[0]+spacing/2-5, new_point[1]+spacing/2,
                            new_point[0]+spacing/2+5, new_point[1]+spacing/2)
        painter.drawLine(new_point[0]+spacing/2, new_point[1]+spacing/2-5,
                            new_point[0]+spacing/2, new_point[1]+spacing/2+5)
        
        return painter

    def widgetUpdate(self):
        pass
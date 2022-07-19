import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
import numpy as np
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

        self.brush_size = 5
        self.brush_type = 'auto'


    def widgetMouseMoveEvent(self, event, axis):
        x, y, z = self.computePosition(event, axis)
        self.IMG_OBJ.POINT_POS = [x, y, z]
        
        if event.buttons() & PySide6.QtCore.Qt.LeftButton:
            if axis == 'axi':
                self.MSK_OBJ.MSK[:, :, z] = self.handlePaint(self.MSK_OBJ.MSK[:, :, z], self.brush_type, [x, y], True)
            elif axis == 'sag':
                self.MSK_OBJ.MSK[x, :, :] = self.handlePaint(self.MSK_OBJ.MSK[x, :, :], self.brush_type, [y, z], True)
            elif axis == 'cor':
                self.MSK_OBJ.MSK[:, y, :] = self.handlePaint(self.MSK_OBJ.MSK[:, y, :], self.brush_type, [x, z], True)

        elif event.buttons() & PySide6.QtCore.Qt.RightButton:
            if axis == 'axi':
                self.MSK_OBJ.MSK[:, :, z] = self.handlePaint(self.MSK_OBJ.MSK[:, :, z], self.brush_type, [x, y], False)
            elif axis == 'sag':
                self.MSK_OBJ.MSK[x, :, :] = self.handlePaint(self.MSK_OBJ.MSK[x, :, :], self.brush_type, [y, z], False)
            elif axis == 'cor':
                self.MSK_OBJ.MSK[:, y, :] = self.handlePaint(self.MSK_OBJ.MSK[:, y, :], self.brush_type, [x, z], False)

        elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.x(), event.y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theBrushPen())
        cx, cy = new_point[0], new_point[1]          
        cx, cy = np.round((cx-margin[0])/zoom), np.round((cy-margin[1])/zoom)
        s_x, s_y = cx - self.brush_size // 2, cy - self.brush_size // 2 
        s_x = s_x * zoom + margin[0]
        s_y = s_y * zoom + margin[1]
        w = self.brush_size * zoom
        
        if self.brush_type == 'auto':
            painter.drawLine(new_point[0]-5, new_point[1],
                             new_point[0]+5, new_point[1])
            painter.drawLine(int(new_point[0]), int(margin[1]),
                             int(new_point[0]), int(margin[1]+newshape[1]))
        elif self.brush_type == 'square':
            painter.drawLine(s_x,s_y,s_x+w,s_y)
            painter.drawLine(s_x,s_y,s_x,s_y+w)
            painter.drawLine(s_x+w,s_y+w,s_x,s_y+w)
            painter.drawLine(s_x+w,s_y+w,s_x+w,s_y)

        elif self.brush_type == 'circle':
            painter.drawEllipse(s_x, s_y, w, w)

        return painter

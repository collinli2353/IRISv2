import numpy as np
import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from skimage.draw import circle_perimeter
from skimage.morphology import octagon
from tools.brush_tool.ui_brush_widget import *
from tools.default_tool import Meta, default_tool
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
from utils.utils import clamp, theBrushPen


class brush(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_brush_widget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()

        self.brush_size = 4
        self.brush_type = 'square'

        def setBrushStyleSquare():
            self.brush_type = 'square'

        def setBrushStyleCircle():
            self.brush_type = 'circle'

        self.ui.brushStyleSquare_button.clicked.connect(lambda: setBrushStyleSquare())
        self.ui.brushStyleCircle_button.clicked.connect(lambda: setBrushStyleCircle())

        self.ui.brushSize_slider.setValue(self.brush_size)
        self.ui.brushSize_slider.valueChanged.connect(self.setBrushSize)
        self.ui.brushSize_label.setText(str(self.brush_size))

    def setBrushSize(self, value):
        self.brush_size = int(value)
        self.ui.brushSize_label.setText(str(value))

    def handlePaint(self, msk, brush_type, pos, isPaint):
        s_x, s_y, w, lbl = pos[0]-self.brush_size//2, pos[1]-self.brush_size//2, self.brush_size, self.MSK_OBJ.CURRENT_LBL
        if brush_type == 'square':
            if isPaint: msk[s_x:s_x+w, s_y:s_y+w] = lbl
            else: isPaint: msk[s_x:s_x+w, s_y:s_y+w] = 0
        elif brush_type == 'circle':
            t_msk = np.zeros([w,w])
        
        if w <=10 or w%2==0:        
            if w<=1:
                t_msk[0,0] = 1
            elif w==3:
                t_msk = octagon(1,1)
            else:    
                p2 = int(np.floor(w/3))
                p1 = w-p2*2
                t_msk = octagon(p1,p2)    
            pos = (t_msk>0)
            s_msk = msk[s_x:s_x+w,s_y:s_y+w]
            if isPaint:
                s_msk[pos]=lbl
                msk[s_x:s_x+w,s_y:s_y+w] = s_msk 
            else:
                s_msk[pos]=0
                msk[s_x:s_x+w,s_y:s_y+w] = s_msk
        else:
            rr, cc = circle_perimeter(s_x+w//2, s_y+w//2, w//2+1)
            if isPaint:
                msk[rr, cc] = lbl 
            else: msk[rr, cc] = 0

        return msk

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
        
        if self.brush_type == 'square':
            painter.drawLine(s_x,s_y,s_x+w,s_y)
            painter.drawLine(s_x,s_y,s_x,s_y+w)
            painter.drawLine(s_x+w,s_y+w,s_x,s_y+w)
            painter.drawLine(s_x+w,s_y+w,s_x+w,s_y)

        elif self.brush_type == 'circle':
            painter.drawEllipse(s_x, s_y, w, w)

        return painter

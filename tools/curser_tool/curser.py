import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from tools.curser_tool.ui_curserWidget import *
from tools.default_tool import Meta, default_tool
from utils.globalConstants import IMG_OBJ, TOOL_OBJ
from utils.utils import clamp, theCrossPen


class curser(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_curserWidget()
        self.ui.setupUi(self)

        self.IMG_OBJ = IMG_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()

    def computePosition(self, ev_x, ev_y, zoom, margin, flip, img_size):
        new_x, new_y = ev_x - margin[0], ev_y - margin[1]
        
        new_foc_pos_2d = [new_x, new_y]
        new_foc_pos_2d = [int(pos / zoom) for pos in new_foc_pos_2d]
        new_foc_pos_2d = [clamp(0,val,img_size-1) for val, img_size in zip(new_foc_pos_2d, img_size)]

        for axis, bool_flip in enumerate(flip):
            if bool_flip:
                new_foc_pos_2d[axis] = img_size[axis] - new_foc_pos_2d[axis] - 1
        
        return new_foc_pos_2d

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z = None, None, None
        if axis == 'axi':
            [x, y] = self.computePosition(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['axi'],
                self.IMG_OBJ.IMG_FLIP['axi'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[1]]
            )
            [x, y, z] = [x, y, self.IMG_OBJ.FOC_POS[2]]
        elif axis == 'sag':
            [x, y] = self.computePosition(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['sag'],
                self.IMG_OBJ.IMG_FLIP['sag'], [self.IMG_OBJ.SHAPE[1], self.IMG_OBJ.SHAPE[2]]
            )
            [x, y, z] = [self.IMG_OBJ.FOC_POS[0], x, y]
        elif axis == 'cor':
            [x, y] = self.computePosition(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['cor'],
                self.IMG_OBJ.IMG_FLIP['cor'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[2]]
            )
            [x, y, z] = [x, self.IMG_OBJ.FOC_POS[1], y]
        else:
            raise ValueError('axis must be axi, sag or cor')

        if event.buttons() & PySide6.QtCore.Qt.LeftButton:
            self.IMG_OBJ.FOC_POS = [x, y, z]

        elif event.buttons() & PySide6.QtCore.Qt.RightButton:
            diff = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
            self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

        elif event.buttons() & PySide6.QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.x(), event.y()]

    def widgetDraw(self, pixmap, new_foc, new_point, margin, spacing, newshape):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(theCrossPen())
        painter.drawLine(int(margin[0]), int(new_foc[1]+spacing/2),
                         int(margin[0]+newshape[0]), int(new_foc[1]+spacing/2))
        painter.drawLine(int(new_foc[0]+spacing/2), int(margin[1]),
                         int(new_foc[0]+spacing/2), int(margin[1]+newshape[1]))

        return painter

    def widgetUpdate(self):
        self.ui.curserX_label.setNum(self.IMG_OBJ.FOC_POS[0]+1)
        self.ui.curserY_label.setNum(self.IMG_OBJ.FOC_POS[1]+1)
        self.ui.curserZ_label.setNum(self.IMG_OBJ.FOC_POS[2]+1)

    def exec(self):
        self.show()

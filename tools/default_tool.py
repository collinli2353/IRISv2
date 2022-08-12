from abc import ABC, abstractmethod
from PySide6 import QtGui, QtWidgets
from utils.globalConstants import IMG_OBJ, MSK_OBJ, TOOL_OBJ
import PySide6
import numpy as np

from utils.utils import clamp

#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods
class default_tool(ABC):
    def setupGlobalConstants(self):
        self.IMG_OBJ = IMG_OBJ()
        self.MSK_OBJ = MSK_OBJ()
        self.TOOL_OBJ = TOOL_OBJ()

    def computeCoords(self, pos_x, pos_y, w, h, img_size_2D):
        pos_x, pos_y = clamp(0, pos_x, img_size_2D[0]-1), clamp(0, pos_y, img_size_2D[1]-1)
        
        if pos_x - w < 0: w = pos_x
        if pos_y - h < 0: h = pos_y
        if pos_x + w >= img_size_2D[0]: w = img_size_2D[0] - pos_x
        if pos_y + h >= img_size_2D[1]: h = img_size_2D[1] - pos_y

        return pos_x, pos_y, w, h

    def computePosition(self, event, axis):    
        def computePosition2D(ev_x, ev_y, zoom, margin, flip, shape):
            new_x, new_y = ev_x - margin[0], ev_y - margin[1]
        
            new_foc_pos_2d = [int(pos / zoom) for pos in [new_x, new_y]]
            new_foc_pos_2d = [clamp(0,val,img_size-1) for val, img_size in zip(new_foc_pos_2d, shape)]

            for axis, bool_flip in enumerate(flip):
                if bool_flip: new_foc_pos_2d[axis] = shape[axis] - new_foc_pos_2d[axis] - 1

            return new_foc_pos_2d

        if axis == 'axi':
            [xx, yy] = computePosition2D(
                event.position().x(), event.position().y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['axi'],
                self.IMG_OBJ.IMG_FLIP['axi'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[1]]
            )
            x, y, z = xx, yy, self.IMG_OBJ.FOC_POS[2]
            margin, shape = self.IMG_OBJ.MARGIN['axi'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[1]]
        elif axis == 'sag':
            [xx, yy] = computePosition2D(
                event.position().x(), event.position().y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['sag'],
                self.IMG_OBJ.IMG_FLIP['sag'], [self.IMG_OBJ.SHAPE[1], self.IMG_OBJ.SHAPE[2]]
            )
            x, y, z = self.IMG_OBJ.FOC_POS[0], xx, yy
            margin, shape = self.IMG_OBJ.MARGIN['sag'], [self.IMG_OBJ.SHAPE[1], self.IMG_OBJ.SHAPE[2]]
        elif axis == 'cor':
            [xx, yy] = computePosition2D(
                event.position().x(), event.position().y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['cor'],
                self.IMG_OBJ.IMG_FLIP['cor'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[2]]
            )
            x, y, z = xx, self.IMG_OBJ.FOC_POS[1], yy
            margin, shape = self.IMG_OBJ.MARGIN['cor'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[2]]
        else:
            raise ValueError('axis must be axi, sag or cor')
        
        return x, y, z, xx, yy, margin, shape

    @abstractmethod
    def widgetMouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, axis: str) -> None: pass

    @abstractmethod
    def widgetDraw(self, pixmap: QtGui.QPixmap, new_foc: list, new_point: list, zoom: float, margin: list, spacing: list, newshape: list) -> PySide6.QtGui.QPainter: pass

    @abstractmethod
    def widgetUpdate(self) -> None: pass
    
class Meta(type(QtWidgets.QWidget), type(ABC)):
    pass
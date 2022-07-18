from abc import ABC, abstractmethod
from PySide6 import QtGui, QtWidgets
import PySide6

from utils.utils import clamp

#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods
class default_tool(ABC):

    def computePosition(self, event, axis):
        x, y, z = None, None, None
    
        def computePosition2D(ev_x, ev_y, zoom, margin, flip, shape):
            new_x, new_y = ev_x - margin[0], ev_y - margin[1]
        
            new_foc_pos_2d = [new_x, new_y]
            new_foc_pos_2d = [int(pos / zoom) for pos in new_foc_pos_2d]
            new_foc_pos_2d = [clamp(0,val,img_size-1) for val, img_size in zip(new_foc_pos_2d, shape)]

            for axis, bool_flip in enumerate(flip):
                if bool_flip:
                    new_foc_pos_2d[axis] = shape[axis] - new_foc_pos_2d[axis] - 1

            return new_foc_pos_2d

        if axis == 'axi':
            [x, y] = computePosition2D(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['axi'],
                self.IMG_OBJ.IMG_FLIP['axi'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[1]]
            )
            [x, y, z] = [x, y, self.IMG_OBJ.FOC_POS[2]]
        elif axis == 'sag':
            [x, y] = computePosition2D(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['sag'],
                self.IMG_OBJ.IMG_FLIP['sag'], [self.IMG_OBJ.SHAPE[1], self.IMG_OBJ.SHAPE[2]]
            )
            [x, y, z] = [self.IMG_OBJ.FOC_POS[0], x, y]
        elif axis == 'cor':
            [x, y] = computePosition2D(
                event.x(), event.y(), self.IMG_OBJ.ZOOM_FACTOR,
                self.IMG_OBJ.MARGIN['cor'],
                self.IMG_OBJ.IMG_FLIP['cor'], [self.IMG_OBJ.SHAPE[0], self.IMG_OBJ.SHAPE[2]]
            )
            [x, y, z] = [x, self.IMG_OBJ.FOC_POS[1], y]
        else:
            raise ValueError('axis must be axi, sag or cor')
        
        return x, y, z

    @abstractmethod
    def widgetMouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, axis: str) -> None: pass

    @abstractmethod
    def widgetDraw(self, pixmap: QtGui.QPixmap, new_foc: list, new_point: list, zoom: float, margin: list, spacing: list, newshape: list) -> PySide6.QtGui.QPainter: pass

    @abstractmethod
    def widgetUpdate(self) -> None: pass
    
class Meta(type(QtWidgets.QWidget), type(ABC)):
    pass
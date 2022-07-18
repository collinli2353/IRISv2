from abc import ABC, abstractmethod
from PySide6 import QtGui, QtWidgets
import PySide6

#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods
class default_tool(ABC):
    @abstractmethod
    def widgetMouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, axis: str) -> None: pass

    @abstractmethod
    def widgetDraw(self, pixmap: QtGui.QPixmap, new_foc: list, new_point: list, margin: list, spacing: list, newshape: list) -> PySide6.QtGui.QPainter: pass

    @abstractmethod
    def widgetUpdate(self) -> None: pass
    
class Meta(type(QtWidgets.QWidget), type(ABC)):
    pass
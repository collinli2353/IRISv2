from abc import ABC, abstractmethod
from PySide6 import QtWidgets
import PySide6

#TODO: this abstract class does not give any functionality... rippp please fix it so that all tools must include these methods
class default_tool(ABC):
    @abstractmethod
    def widgetMousePressEvent(self, event: PySide6.QtGui.QMouseEvent, axis: str) -> None: pass

    @abstractmethod
    def widgetMouseMoveEvent(self, event: PySide6.QtGui.QMouseEvent, axis: str) -> None: pass

class Meta(type(QtWidgets.QWidget), type(ABC)):
    pass
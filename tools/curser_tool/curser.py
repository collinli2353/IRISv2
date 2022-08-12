import PySide6
from PySide6 import QtCore, QtGui, QtWidgets
from tools.curser_tool.ui_curserWidget import Ui_curserWidget
from tools.default_tool import Meta, default_tool
from utils.utils import clamp, theCrossPen


class curser(QtWidgets.QWidget, default_tool, metaclass=Meta):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_curserWidget()
        self.ui.setupUi(self)
        self.setupGlobalConstants()

        self.ui.winVal_slider.valueChanged.connect(self.setWindowValue)
        self.ui.levVal_slider.valueChanged.connect(self.setLevelValue)

    def setWindowValue(self, value):
        self.IMG_OBJ.WINDOW_VALUE = value
        self.ui.winVal_slider.setValue(value)
        self.ui.winVal_label.setText(str(value))
        self.IMG_OBJ.UPDATE_VIEWERS()

    def setLevelValue(self, value):
        self.IMG_OBJ.LEVEL_VALUE = value
        self.ui.levVal_slider.setValue(value)
        self.ui.levVal_label.setText(str(value))
        self.IMG_OBJ.UPDATE_VIEWERS()

    def widgetMouseMoveEvent(self, event, axis):
        x, y, z, xx, yy, margin, shape = self.computePosition(event, axis)
        
        if event.buttons() & QtCore.Qt.LeftButton:
            self.IMG_OBJ.FOC_POS = [x, y, z]

        elif event.buttons() & QtCore.Qt.RightButton:
            diff = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            self.IMG_OBJ.ZOOM_FACTOR *= 1.01**(diff)
            self.IMG_OBJ.ZOOM_FACTOR = clamp(0.3, self.IMG_OBJ.ZOOM_FACTOR, 15)

        elif event.buttons() & QtCore.Qt.MiddleButton:
            diffX = self.TOOL_OBJ.INIT_MOUSE_POS[axis][0] - event.position().x()
            diffY = self.TOOL_OBJ.INIT_MOUSE_POS[axis][1] - event.y()
            if axis == 'axi': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, self.IMG_OBJ.SHIFT[1] - diffY, 0]
            elif axis == 'sag': self.IMG_OBJ.SHIFT = [0, self.IMG_OBJ.SHIFT[1] - diffX, self.IMG_OBJ.SHIFT[2] - diffY]
            elif axis == 'cor': self.IMG_OBJ.SHIFT = [self.IMG_OBJ.SHIFT[0] - diffX, 0, self.IMG_OBJ.SHIFT[2] - diffY]

        self.TOOL_OBJ.INIT_MOUSE_POS[axis] = [event.position().x(), event.position().y()]

    def widgetDraw(self, pixmap, new_foc, new_point, zoom, margin, spacing, newshape):
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

        self.ui.minIntensity_label.setNum(round(self.IMG_OBJ.MIN_MAX_INTENSITIES[0], 2))
        self.ui.maxIntensity_label.setNum(round(self.IMG_OBJ.MIN_MAX_INTENSITIES[1], 2))
        self.ui.curIntensity_label.setNum(round(self.IMG_OBJ.ORIG_NP_IMG[self.IMG_OBJ.FOC_POS[0], self.IMG_OBJ.FOC_POS[1], self.IMG_OBJ.FOC_POS[2]], 2))

        self.setWindowValue(int(self.IMG_OBJ.WINDOW_VALUE))
        self.setLevelValue(int(self.IMG_OBJ.LEVEL_VALUE))
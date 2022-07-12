import numpy as np
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QColor as rgb
from utils.colorTable import mapLabelID2RGB

def initImgParams(img):
    
    img_size = img.shape
    img_max = img.max()
    img_min = img.min()
    min_max = [img_min, img_max]
    
    val_win = img_max - img_min
    val_lev = (img_max + img_min) / 2
    
    foc_pos = [int(val/2) for val in img_size]
    foc_val = img[foc_pos[0],foc_pos[1],foc_pos[2]]
    
    return val_win, val_lev, foc_pos, foc_val, min_max, img_size

def clamp(small, value, large):
    return max(small, min(value, large))

def theCrossPen(width=2):
    
    pen = QtGui.QPen()
    pen.setColor(rgb(76, 76, 255))
    pen.setWidth(width)
    dashes = [1, 1]
    pen.setCapStyle(QtCore.Qt.FlatCap)
    pen.setDashPattern(dashes)
    
    return pen

def theBoundaryPen(width=1):
    
    pen = QtGui.QPen()
    pen.setColor(rgb(0, 0, 0))
    pen.setWidth(width)
    pen.setCapStyle(QtCore.Qt.FlatCap)
    
    return pen

def theBrushPen(width=2, lbl=None):
    
    pen = QtGui.QPen()
    if lbl is None:
        pen.setColor(rgb(255, 0, 51))
    else:
        r, g, b = mapLabelID2RGB(lbl)
        r, g, b = int(r*255), int(g*255), int(b*255)
        pen.setColor(rgb(r, g, b))
    
    pen.setWidth(width)

    dashes = [1, 1]
    pen.setCapStyle(QtCore.Qt.FlatCap)
    pen.setDashPattern(dashes)
    
    return pen

def lettersPen(color):

    pen = QtGui.QPen()
    pen.setColor(color)

    return pen


def cutv(small, value, large):

    return np.maximum(small, np.minimum(value, large))
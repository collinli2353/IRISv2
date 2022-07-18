# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brush_widgetGlJCBJ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_brush_widget(object):
    def setupUi(self, brush_widget):
        if not brush_widget.objectName():
            brush_widget.setObjectName(u"brush_widget")
        brush_widget.resize(248, 263)
        self.verticalLayout = QVBoxLayout(brush_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.brush_verticalSpacer = QSpacerItem(227, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.brush_verticalSpacer)

        self.brushStyle_label = QLabel(brush_widget)
        self.brushStyle_label.setObjectName(u"brushStyle_label")

        self.verticalLayout.addWidget(self.brushStyle_label)

        self.brushStyle_frame = QFrame(brush_widget)
        self.brushStyle_frame.setObjectName(u"brushStyle_frame")
        self.brushStyle_frame.setMaximumSize(QSize(16777215, 25))
        self.brushStyle_frame.setFrameShape(QFrame.StyledPanel)
        self.brushStyle_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.brushStyle_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.brushStyleSquare_button = QPushButton(self.brushStyle_frame)
        self.brushStyleSquare_button.setObjectName(u"brushStyleSquare_button")

        self.horizontalLayout_7.addWidget(self.brushStyleSquare_button)

        self.brushStyleCircle_button = QPushButton(self.brushStyle_frame)
        self.brushStyleCircle_button.setObjectName(u"brushStyleCircle_button")

        self.horizontalLayout_7.addWidget(self.brushStyleCircle_button)

        self.brushStyleMorph_button = QPushButton(self.brushStyle_frame)
        self.brushStyleMorph_button.setObjectName(u"brushStyleMorph_button")

        self.horizontalLayout_7.addWidget(self.brushStyleMorph_button)


        self.verticalLayout.addWidget(self.brushStyle_frame)

        self.brushSizeTag_label = QLabel(brush_widget)
        self.brushSizeTag_label.setObjectName(u"brushSizeTag_label")

        self.verticalLayout.addWidget(self.brushSizeTag_label)

        self.brushSize_frame = QFrame(brush_widget)
        self.brushSize_frame.setObjectName(u"brushSize_frame")
        self.brushSize_frame.setFrameShape(QFrame.StyledPanel)
        self.brushSize_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.brushSize_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.brushSize_label = QLabel(self.brushSize_frame)
        self.brushSize_label.setObjectName(u"brushSize_label")

        self.horizontalLayout_8.addWidget(self.brushSize_label)

        self.brushSize_slider = QSlider(self.brushSize_frame)
        self.brushSize_slider.setObjectName(u"brushSize_slider")
        self.brushSize_slider.setMaximum(200)
        self.brushSize_slider.setPageStep(1)
        self.brushSize_slider.setSliderPosition(0)
        self.brushSize_slider.setOrientation(Qt.Horizontal)
        self.brushSize_slider.setTickPosition(QSlider.TicksBothSides)
        self.brushSize_slider.setTickInterval(5)

        self.horizontalLayout_8.addWidget(self.brushSize_slider)


        self.verticalLayout.addWidget(self.brushSize_frame)

        self.brushOptions_label = QLabel(brush_widget)
        self.brushOptions_label.setObjectName(u"brushOptions_label")

        self.verticalLayout.addWidget(self.brushOptions_label)

        self.brushSettings_layout = QGridLayout()
        self.brushSettings_layout.setObjectName(u"brushSettings_layout")
        self.brushCursorChasesBrush_checkBox = QCheckBox(brush_widget)
        self.brushCursorChasesBrush_checkBox.setObjectName(u"brushCursorChasesBrush_checkBox")

        self.brushSettings_layout.addWidget(self.brushCursorChasesBrush_checkBox, 1, 0, 1, 1)

        self.brush3D_checkBox = QCheckBox(brush_widget)
        self.brush3D_checkBox.setObjectName(u"brush3D_checkBox")

        self.brushSettings_layout.addWidget(self.brush3D_checkBox, 0, 0, 1, 1)

        self.brushIsotroopic_checkBox = QCheckBox(brush_widget)
        self.brushIsotroopic_checkBox.setObjectName(u"brushIsotroopic_checkBox")

        self.brushSettings_layout.addWidget(self.brushIsotroopic_checkBox, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.brushSettings_layout)


        self.retranslateUi(brush_widget)

        QMetaObject.connectSlotsByName(brush_widget)
    # setupUi

    def retranslateUi(self, brush_widget):
        brush_widget.setWindowTitle(QCoreApplication.translate("brush_widget", u"Form", None))
        self.brushStyle_label.setText(QCoreApplication.translate("brush_widget", u"Brush Style:", None))
        self.brushStyleSquare_button.setText(QCoreApplication.translate("brush_widget", u"Square", None))
        self.brushStyleCircle_button.setText(QCoreApplication.translate("brush_widget", u"Circle", None))
        self.brushStyleMorph_button.setText(QCoreApplication.translate("brush_widget", u"3", None))
        self.brushSizeTag_label.setText(QCoreApplication.translate("brush_widget", u"Brush Size:", None))
        self.brushSize_label.setText(QCoreApplication.translate("brush_widget", u"#", None))
        self.brushOptions_label.setText(QCoreApplication.translate("brush_widget", u"Brush Options:", None))
        self.brushCursorChasesBrush_checkBox.setText(QCoreApplication.translate("brush_widget", u"Cursor chases brush", None))
        self.brush3D_checkBox.setText(QCoreApplication.translate("brush_widget", u"3D", None))
        self.brushIsotroopic_checkBox.setText(QCoreApplication.translate("brush_widget", u"Isotropic", None))
    # retranslateUi


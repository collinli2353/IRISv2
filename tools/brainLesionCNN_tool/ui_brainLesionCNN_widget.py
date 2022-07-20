# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'brainLesionCNN_widgetwTQpkz.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_brainLesionCNN_widget(object):
    def setupUi(self, brainLesionCNN_widget):
        if not brainLesionCNN_widget.objectName():
            brainLesionCNN_widget.setObjectName(u"brainLesionCNN_widget")
        brainLesionCNN_widget.resize(176, 134)
        self.verticalLayout = QVBoxLayout(brainLesionCNN_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.segment_button = QPushButton(brainLesionCNN_widget)
        self.segment_button.setObjectName(u"segment_button")

        self.horizontalLayout.addWidget(self.segment_button)

        self.separate_button = QPushButton(brainLesionCNN_widget)
        self.separate_button.setObjectName(u"separate_button")

        self.horizontalLayout.addWidget(self.separate_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.t1_button = QPushButton(brainLesionCNN_widget)
        self.t1_button.setObjectName(u"t1_button")

        self.verticalLayout.addWidget(self.t1_button)

        self.t2_button = QPushButton(brainLesionCNN_widget)
        self.t2_button.setObjectName(u"t2_button")

        self.verticalLayout.addWidget(self.t2_button)

        self.fl_button = QPushButton(brainLesionCNN_widget)
        self.fl_button.setObjectName(u"fl_button")

        self.verticalLayout.addWidget(self.fl_button)


        self.retranslateUi(brainLesionCNN_widget)

        QMetaObject.connectSlotsByName(brainLesionCNN_widget)
    # setupUi

    def retranslateUi(self, brainLesionCNN_widget):
        brainLesionCNN_widget.setWindowTitle(QCoreApplication.translate("brainLesionCNN_widget", u"Form", None))
        self.segment_button.setText(QCoreApplication.translate("brainLesionCNN_widget", u"Segment", None))
        self.separate_button.setText(QCoreApplication.translate("brainLesionCNN_widget", u"Separate", None))
        self.t1_button.setText(QCoreApplication.translate("brainLesionCNN_widget", u"Open T1", None))
        self.t2_button.setText(QCoreApplication.translate("brainLesionCNN_widget", u"Open T2", None))
        self.fl_button.setText(QCoreApplication.translate("brainLesionCNN_widget", u"Open FL", None))
    # retranslateUi


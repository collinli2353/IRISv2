# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'smartclickCNNfAhBET.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_smartclickCNN_widget(object):
    def setupUi(self, smartclickCNN_widget):
        if not smartclickCNN_widget.objectName():
            smartclickCNN_widget.setObjectName(u"smartclickCNN_widget")
        smartclickCNN_widget.resize(94, 102)
        self.verticalLayout = QVBoxLayout(smartclickCNN_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.segment_button = QPushButton(smartclickCNN_widget)
        self.segment_button.setObjectName(u"segment_button")

        self.verticalLayout.addWidget(self.segment_button)

        self.refine_button = QPushButton(smartclickCNN_widget)
        self.refine_button.setObjectName(u"refine_button")

        self.verticalLayout.addWidget(self.refine_button)

        self.clearSeeds_button = QPushButton(smartclickCNN_widget)
        self.clearSeeds_button.setObjectName(u"clearSeeds_button")

        self.verticalLayout.addWidget(self.clearSeeds_button)


        self.retranslateUi(smartclickCNN_widget)

        QMetaObject.connectSlotsByName(smartclickCNN_widget)
    # setupUi

    def retranslateUi(self, smartclickCNN_widget):
        smartclickCNN_widget.setWindowTitle(QCoreApplication.translate("smartclickCNN_widget", u"Form", None))
        self.segment_button.setText(QCoreApplication.translate("smartclickCNN_widget", u"Segment", None))
        self.refine_button.setText(QCoreApplication.translate("smartclickCNN_widget", u"Refine", None))
        self.clearSeeds_button.setText(QCoreApplication.translate("smartclickCNN_widget", u"Clear Seeds", None))
    # retranslateUi


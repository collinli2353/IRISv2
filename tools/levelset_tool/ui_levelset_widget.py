# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'levelset_widgetCfIPtp.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_levelset_widget(object):
    def setupUi(self, levelset_widget):
        if not levelset_widget.objectName():
            levelset_widget.setObjectName(u"levelset_widget")
        levelset_widget.resize(245, 391)
        self.verticalLayout = QVBoxLayout(levelset_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.levelset_verticalSpacer = QSpacerItem(227, 12, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.levelset_verticalSpacer)

        self.levelsetDefualtSettngs_label = QPushButton(levelset_widget)
        self.levelsetDefualtSettngs_label.setObjectName(u"levelsetDefualtSettngs_label")

        self.verticalLayout.addWidget(self.levelsetDefualtSettngs_label)

        self.levelsetType_label = QLabel(levelset_widget)
        self.levelsetType_label.setObjectName(u"levelsetType_label")
        self.levelsetType_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.levelsetType_label)

        self.levelsetType_layout = QHBoxLayout()
        self.levelsetType_layout.setObjectName(u"levelsetType_layout")
        self.levelset2D_button = QPushButton(levelset_widget)
        self.levelset2D_button.setObjectName(u"levelset2D_button")

        self.levelsetType_layout.addWidget(self.levelset2D_button)

        self.levelset3D_button = QPushButton(levelset_widget)
        self.levelset3D_button.setObjectName(u"levelset3D_button")

        self.levelsetType_layout.addWidget(self.levelset3D_button)


        self.verticalLayout.addLayout(self.levelsetType_layout)

        self.levelsetInvert_label = QLabel(levelset_widget)
        self.levelsetInvert_label.setObjectName(u"levelsetInvert_label")
        self.levelsetInvert_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout.addWidget(self.levelsetInvert_label)

        self.levelsetInvert_layout = QHBoxLayout()
        self.levelsetInvert_layout.setObjectName(u"levelsetInvert_layout")
        self.levelsetInvertTrue_button = QPushButton(levelset_widget)
        self.levelsetInvertTrue_button.setObjectName(u"levelsetInvertTrue_button")

        self.levelsetInvert_layout.addWidget(self.levelsetInvertTrue_button)

        self.levelsetInvertFalse_button = QPushButton(levelset_widget)
        self.levelsetInvertFalse_button.setObjectName(u"levelsetInvertFalse_button")

        self.levelsetInvert_layout.addWidget(self.levelsetInvertFalse_button)


        self.verticalLayout.addLayout(self.levelsetInvert_layout)

        self.levelsetMu_label = QLabel(levelset_widget)
        self.levelsetMu_label.setObjectName(u"levelsetMu_label")

        self.verticalLayout.addWidget(self.levelsetMu_label)

        self.levelsetMu_layout = QHBoxLayout()
        self.levelsetMu_layout.setObjectName(u"levelsetMu_layout")
        self.levelsetMu_textEdit = QTextEdit(levelset_widget)
        self.levelsetMu_textEdit.setObjectName(u"levelsetMu_textEdit")
        self.levelsetMu_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetMu_layout.addWidget(self.levelsetMu_textEdit)

        self.levelsetMu_slider = QSlider(levelset_widget)
        self.levelsetMu_slider.setObjectName(u"levelsetMu_slider")
        self.levelsetMu_slider.setOrientation(Qt.Horizontal)

        self.levelsetMu_layout.addWidget(self.levelsetMu_slider)


        self.verticalLayout.addLayout(self.levelsetMu_layout)

        self.levelsetNu_label = QLabel(levelset_widget)
        self.levelsetNu_label.setObjectName(u"levelsetNu_label")

        self.verticalLayout.addWidget(self.levelsetNu_label)

        self.levelsetNu_layout = QHBoxLayout()
        self.levelsetNu_layout.setObjectName(u"levelsetNu_layout")
        self.levelsetNu_textEdit = QTextEdit(levelset_widget)
        self.levelsetNu_textEdit.setObjectName(u"levelsetNu_textEdit")
        self.levelsetNu_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetNu_layout.addWidget(self.levelsetNu_textEdit)

        self.levelsetNu_slider = QSlider(levelset_widget)
        self.levelsetNu_slider.setObjectName(u"levelsetNu_slider")
        self.levelsetNu_slider.setOrientation(Qt.Horizontal)

        self.levelsetNu_layout.addWidget(self.levelsetNu_slider)


        self.verticalLayout.addLayout(self.levelsetNu_layout)

        self.levelsetMaxIter_label = QLabel(levelset_widget)
        self.levelsetMaxIter_label.setObjectName(u"levelsetMaxIter_label")

        self.verticalLayout.addWidget(self.levelsetMaxIter_label)

        self.levelsetMaxIter_layout = QHBoxLayout()
        self.levelsetMaxIter_layout.setObjectName(u"levelsetMaxIter_layout")
        self.levelsetMaxIter_textEdit = QTextEdit(levelset_widget)
        self.levelsetMaxIter_textEdit.setObjectName(u"levelsetMaxIter_textEdit")
        self.levelsetMaxIter_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetMaxIter_layout.addWidget(self.levelsetMaxIter_textEdit)

        self.levelsetMaxIter_slider = QSlider(levelset_widget)
        self.levelsetMaxIter_slider.setObjectName(u"levelsetMaxIter_slider")
        self.levelsetMaxIter_slider.setOrientation(Qt.Horizontal)

        self.levelsetMaxIter_layout.addWidget(self.levelsetMaxIter_slider)


        self.verticalLayout.addLayout(self.levelsetMaxIter_layout)

        self.levelsetEpison_label = QLabel(levelset_widget)
        self.levelsetEpison_label.setObjectName(u"levelsetEpison_label")

        self.verticalLayout.addWidget(self.levelsetEpison_label)

        self.levelsetEpison_layout = QHBoxLayout()
        self.levelsetEpison_layout.setObjectName(u"levelsetEpison_layout")
        self.levelsetEpison_textEdit = QTextEdit(levelset_widget)
        self.levelsetEpison_textEdit.setObjectName(u"levelsetEpison_textEdit")
        self.levelsetEpison_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetEpison_layout.addWidget(self.levelsetEpison_textEdit)

        self.levelsetEpison_slider = QSlider(levelset_widget)
        self.levelsetEpison_slider.setObjectName(u"levelsetEpison_slider")
        self.levelsetEpison_slider.setOrientation(Qt.Horizontal)

        self.levelsetEpison_layout.addWidget(self.levelsetEpison_slider)


        self.verticalLayout.addLayout(self.levelsetEpison_layout)

        self.levelsetStepValue_label = QLabel(levelset_widget)
        self.levelsetStepValue_label.setObjectName(u"levelsetStepValue_label")

        self.verticalLayout.addWidget(self.levelsetStepValue_label)

        self.levelsetStepValue_layout = QHBoxLayout()
        self.levelsetStepValue_layout.setObjectName(u"levelsetStepValue_layout")
        self.levelsetStepValue_textEdit = QTextEdit(levelset_widget)
        self.levelsetStepValue_textEdit.setObjectName(u"levelsetStepValue_textEdit")
        self.levelsetStepValue_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetStepValue_layout.addWidget(self.levelsetStepValue_textEdit)

        self.levelsetStepValue_slider = QSlider(levelset_widget)
        self.levelsetStepValue_slider.setObjectName(u"levelsetStepValue_slider")
        self.levelsetStepValue_slider.setOrientation(Qt.Horizontal)

        self.levelsetStepValue_layout.addWidget(self.levelsetStepValue_slider)


        self.verticalLayout.addLayout(self.levelsetStepValue_layout)


        self.retranslateUi(levelset_widget)

        QMetaObject.connectSlotsByName(levelset_widget)
    # setupUi

    def retranslateUi(self, levelset_widget):
        levelset_widget.setWindowTitle(QCoreApplication.translate("levelset_widget", u"Form", None))
        self.levelsetDefualtSettngs_label.setText(QCoreApplication.translate("levelset_widget", u"Default Settings", None))
        self.levelsetType_label.setText(QCoreApplication.translate("levelset_widget", u"Levelset Type", None))
        self.levelset2D_button.setText(QCoreApplication.translate("levelset_widget", u"2D", None))
        self.levelset3D_button.setText(QCoreApplication.translate("levelset_widget", u"3D", None))
        self.levelsetInvert_label.setText(QCoreApplication.translate("levelset_widget", u"Levelset Invert", None))
        self.levelsetInvertTrue_button.setText(QCoreApplication.translate("levelset_widget", u"True", None))
        self.levelsetInvertFalse_button.setText(QCoreApplication.translate("levelset_widget", u"False", None))
        self.levelsetMu_label.setText(QCoreApplication.translate("levelset_widget", u"\u03bc value: 1.0-5.0", None))
        self.levelsetMu_textEdit.setHtml(QCoreApplication.translate("levelset_widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>", None))
        self.levelsetNu_label.setText(QCoreApplication.translate("levelset_widget", u"n value: 0.0-5.0", None))
        self.levelsetMaxIter_label.setText(QCoreApplication.translate("levelset_widget", u"max iter: 0-100", None))
        self.levelsetEpison_label.setText(QCoreApplication.translate("levelset_widget", u"\u03b5 value 0.0-1.0", None))
        self.levelsetStepValue_label.setText(QCoreApplication.translate("levelset_widget", u"step value: 0-1", None))
    # retranslateUi


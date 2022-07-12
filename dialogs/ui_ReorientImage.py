# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ReorientImageqWXeOZ.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_ReorientImage_Widget(object):
    def setupUi(self, ReorientImage_Widget):
        if not ReorientImage_Widget.objectName():
            ReorientImage_Widget.setObjectName(u"ReorientImage_Widget")
        ReorientImage_Widget.resize(640, 420)
        ReorientImage_Widget.setMinimumSize(QSize(640, 420))
        self.verticalLayout = QVBoxLayout(ReorientImage_Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalSpacer_1 = QSpacerItem(200, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_1)

        self.currentOrientation_label = QLabel(ReorientImage_Widget)
        self.currentOrientation_label.setObjectName(u"currentOrientation_label")

        self.horizontalLayout_1.addWidget(self.currentOrientation_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_2)

        self.newOrientation_label = QLabel(ReorientImage_Widget)
        self.newOrientation_label.setObjectName(u"newOrientation_label")

        self.horizontalLayout_1.addWidget(self.newOrientation_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_1.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.raiCode_label = QLabel(ReorientImage_Widget)
        self.raiCode_label.setObjectName(u"raiCode_label")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raiCode_label.sizePolicy().hasHeightForWidth())
        self.raiCode_label.setSizePolicy(sizePolicy)
        self.raiCode_label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_2.addWidget(self.raiCode_label)

        self.currentRaiCode_textEdit = QTextEdit(ReorientImage_Widget)
        self.currentRaiCode_textEdit.setObjectName(u"currentRaiCode_textEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.currentRaiCode_textEdit.sizePolicy().hasHeightForWidth())
        self.currentRaiCode_textEdit.setSizePolicy(sizePolicy1)
        self.currentRaiCode_textEdit.setMinimumSize(QSize(0, 25))
        self.currentRaiCode_textEdit.setMaximumSize(QSize(16777215, 25))
        self.currentRaiCode_textEdit.setInputMethodHints(Qt.ImhMultiLine)
        self.currentRaiCode_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.currentRaiCode_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_2.addWidget(self.currentRaiCode_textEdit)

        self.newRaiCode_textEdit = QTextEdit(ReorientImage_Widget)
        self.newRaiCode_textEdit.setObjectName(u"newRaiCode_textEdit")
        sizePolicy1.setHeightForWidth(self.newRaiCode_textEdit.sizePolicy().hasHeightForWidth())
        self.newRaiCode_textEdit.setSizePolicy(sizePolicy1)
        self.newRaiCode_textEdit.setMinimumSize(QSize(0, 25))
        self.newRaiCode_textEdit.setMaximumSize(QSize(16777215, 25))
        self.newRaiCode_textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.newRaiCode_textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_2.addWidget(self.newRaiCode_textEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.voxelXAxis_label = QLabel(ReorientImage_Widget)
        self.voxelXAxis_label.setObjectName(u"voxelXAxis_label")
        sizePolicy.setHeightForWidth(self.voxelXAxis_label.sizePolicy().hasHeightForWidth())
        self.voxelXAxis_label.setSizePolicy(sizePolicy)
        self.voxelXAxis_label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_3.addWidget(self.voxelXAxis_label)

        self.currentVoxelXAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.currentVoxelXAxis_comboBox.setObjectName(u"currentVoxelXAxis_comboBox")

        self.horizontalLayout_3.addWidget(self.currentVoxelXAxis_comboBox)

        self.newVoxelXAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.newVoxelXAxis_comboBox.setObjectName(u"newVoxelXAxis_comboBox")

        self.horizontalLayout_3.addWidget(self.newVoxelXAxis_comboBox)

        self.voxelXAxis_button = QPushButton(ReorientImage_Widget)
        self.voxelXAxis_button.setObjectName(u"voxelXAxis_button")
        self.voxelXAxis_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_3.addWidget(self.voxelXAxis_button)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.voxelYAxis_comboBox = QLabel(ReorientImage_Widget)
        self.voxelYAxis_comboBox.setObjectName(u"voxelYAxis_comboBox")
        sizePolicy.setHeightForWidth(self.voxelYAxis_comboBox.sizePolicy().hasHeightForWidth())
        self.voxelYAxis_comboBox.setSizePolicy(sizePolicy)
        self.voxelYAxis_comboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_4.addWidget(self.voxelYAxis_comboBox)

        self.currentVoxelYAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.currentVoxelYAxis_comboBox.setObjectName(u"currentVoxelYAxis_comboBox")

        self.horizontalLayout_4.addWidget(self.currentVoxelYAxis_comboBox)

        self.newVoxelYAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.newVoxelYAxis_comboBox.setObjectName(u"newVoxelYAxis_comboBox")

        self.horizontalLayout_4.addWidget(self.newVoxelYAxis_comboBox)

        self.voxelYAxis_button = QPushButton(ReorientImage_Widget)
        self.voxelYAxis_button.setObjectName(u"voxelYAxis_button")
        self.voxelYAxis_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_4.addWidget(self.voxelYAxis_button)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.voxelZAxis_label = QLabel(ReorientImage_Widget)
        self.voxelZAxis_label.setObjectName(u"voxelZAxis_label")
        sizePolicy.setHeightForWidth(self.voxelZAxis_label.sizePolicy().hasHeightForWidth())
        self.voxelZAxis_label.setSizePolicy(sizePolicy)
        self.voxelZAxis_label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_5.addWidget(self.voxelZAxis_label)

        self.currentVoxelZAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.currentVoxelZAxis_comboBox.setObjectName(u"currentVoxelZAxis_comboBox")

        self.horizontalLayout_5.addWidget(self.currentVoxelZAxis_comboBox)

        self.newVoxelZAxis_comboBox = QComboBox(ReorientImage_Widget)
        self.newVoxelZAxis_comboBox.setObjectName(u"newVoxelZAxis_comboBox")

        self.horizontalLayout_5.addWidget(self.newVoxelZAxis_comboBox)

        self.voxelZAxis_button = QPushButton(ReorientImage_Widget)
        self.voxelZAxis_button.setObjectName(u"voxelZAxis_button")
        self.voxelZAxis_button.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_5.addWidget(self.voxelZAxis_button)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.NIFTI_label = QLabel(ReorientImage_Widget)
        self.NIFTI_label.setObjectName(u"NIFTI_label")
        sizePolicy.setHeightForWidth(self.NIFTI_label.sizePolicy().hasHeightForWidth())
        self.NIFTI_label.setSizePolicy(sizePolicy)
        self.NIFTI_label.setMinimumSize(QSize(200, 0))

        self.horizontalLayout_6.addWidget(self.NIFTI_label)

        self.tableWidget_2 = QTableWidget(ReorientImage_Widget)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_6.addWidget(self.tableWidget_2)

        self.newNIFTI_tableView = QTableWidget(ReorientImage_Widget)
        self.newNIFTI_tableView.setObjectName(u"newNIFTI_tableView")

        self.horizontalLayout_6.addWidget(self.newNIFTI_tableView)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")

        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.retranslateUi(ReorientImage_Widget)

        QMetaObject.connectSlotsByName(ReorientImage_Widget)
    # setupUi

    def retranslateUi(self, ReorientImage_Widget):
        ReorientImage_Widget.setWindowTitle(QCoreApplication.translate("ReorientImage_Widget", u"Reorient Image", None))
        self.currentOrientation_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"Current Orientation:", None))
        self.newOrientation_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"New Orientation", None))
        self.raiCode_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"RAI code:", None))
        self.voxelXAxis_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"Voxel X Axis:", None))
        self.voxelXAxis_button.setText("")
        self.voxelYAxis_comboBox.setText(QCoreApplication.translate("ReorientImage_Widget", u"Voxel Y Axis:", None))
        self.voxelYAxis_button.setText("")
        self.voxelZAxis_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"Voxel Z Axis:", None))
        self.voxelZAxis_button.setText("")
        self.NIFTI_label.setText(QCoreApplication.translate("ReorientImage_Widget", u"Voxel to World Matrix (NIFTI):", None))
    # retranslateUi


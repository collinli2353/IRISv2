# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowviyCGA.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 640)
        MainWindow.setMinimumSize(QSize(960, 640))
        icon = QIcon()
        icon.addFile(u"../../../../.designer/backup/icons/Cornell_University_seal.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.actionOpen_Image = QAction(MainWindow)
        self.actionOpen_Image.setObjectName(u"actionOpen_Image")
        self.actionOpen_Segmentation = QAction(MainWindow)
        self.actionOpen_Segmentation.setObjectName(u"actionOpen_Segmentation")
        self.actionOpen_Organ = QAction(MainWindow)
        self.actionOpen_Organ.setObjectName(u"actionOpen_Organ")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_As = QAction(MainWindow)
        self.actionSave_As.setObjectName(u"actionSave_As")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionHide_Segmentation = QAction(MainWindow)
        self.actionHide_Segmentation.setObjectName(u"actionHide_Segmentation")
        self.actionClear_All = QAction(MainWindow)
        self.actionClear_All.setObjectName(u"actionClear_All")
        self.actionExcluding_Organ = QAction(MainWindow)
        self.actionExcluding_Organ.setObjectName(u"actionExcluding_Organ")
        self.actionVolume_and_Statistics = QAction(MainWindow)
        self.actionVolume_and_Statistics.setObjectName(u"actionVolume_and_Statistics")
        self.actionReorient_Image = QAction(MainWindow)
        self.actionReorient_Image.setObjectName(u"actionReorient_Image")
        self.actionDice_Score = QAction(MainWindow)
        self.actionDice_Score.setObjectName(u"actionDice_Score")
        self.actionAbout_IRIS = QAction(MainWindow)
        self.actionAbout_IRIS.setObjectName(u"actionAbout_IRIS")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setAutoFillBackground(False)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.left_frame.sizePolicy().hasHeightForWidth())
        self.left_frame.setSizePolicy(sizePolicy1)
        self.left_frame.setMinimumSize(QSize(250, 0))
        self.left_frame.setMaximumSize(QSize(250, 16777215))
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolbar_frame = QGridLayout()
        self.toolbar_frame.setObjectName(u"toolbar_frame")
        self.toolbar_frame.setSizeConstraint(QLayout.SetFixedSize)
        self.toolbar_frame.setHorizontalSpacing(0)
        self.toolbar4_button = QPushButton(self.left_frame)
        self.toolbar4_button.setObjectName(u"toolbar4_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toolbar4_button.sizePolicy().hasHeightForWidth())
        self.toolbar4_button.setSizePolicy(sizePolicy2)
        self.toolbar4_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar4_button, 0, 4, 1, 1)

        self.toolbar6_button = QPushButton(self.left_frame)
        self.toolbar6_button.setObjectName(u"toolbar6_button")
        sizePolicy2.setHeightForWidth(self.toolbar6_button.sizePolicy().hasHeightForWidth())
        self.toolbar6_button.setSizePolicy(sizePolicy2)
        self.toolbar6_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar6_button, 2, 1, 1, 1)

        self.toolbar5_button = QPushButton(self.left_frame)
        self.toolbar5_button.setObjectName(u"toolbar5_button")
        sizePolicy2.setHeightForWidth(self.toolbar5_button.sizePolicy().hasHeightForWidth())
        self.toolbar5_button.setSizePolicy(sizePolicy2)
        self.toolbar5_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar5_button, 2, 0, 1, 1)

        self.toolbar0_button = QPushButton(self.left_frame)
        self.toolbar0_button.setObjectName(u"toolbar0_button")
        sizePolicy2.setHeightForWidth(self.toolbar0_button.sizePolicy().hasHeightForWidth())
        self.toolbar0_button.setSizePolicy(sizePolicy2)
        self.toolbar0_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar0_button, 0, 0, 1, 1)

        self.toolbar1_button = QPushButton(self.left_frame)
        self.toolbar1_button.setObjectName(u"toolbar1_button")
        sizePolicy2.setHeightForWidth(self.toolbar1_button.sizePolicy().hasHeightForWidth())
        self.toolbar1_button.setSizePolicy(sizePolicy2)
        self.toolbar1_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar1_button, 0, 1, 1, 1)

        self.toolbar3_button = QPushButton(self.left_frame)
        self.toolbar3_button.setObjectName(u"toolbar3_button")
        sizePolicy2.setHeightForWidth(self.toolbar3_button.sizePolicy().hasHeightForWidth())
        self.toolbar3_button.setSizePolicy(sizePolicy2)
        self.toolbar3_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar3_button, 0, 3, 1, 1)

        self.toolbar9_button = QPushButton(self.left_frame)
        self.toolbar9_button.setObjectName(u"toolbar9_button")
        sizePolicy2.setHeightForWidth(self.toolbar9_button.sizePolicy().hasHeightForWidth())
        self.toolbar9_button.setSizePolicy(sizePolicy2)
        self.toolbar9_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar9_button, 2, 4, 1, 1)

        self.toolbar8_button = QPushButton(self.left_frame)
        self.toolbar8_button.setObjectName(u"toolbar8_button")
        sizePolicy2.setHeightForWidth(self.toolbar8_button.sizePolicy().hasHeightForWidth())
        self.toolbar8_button.setSizePolicy(sizePolicy2)
        self.toolbar8_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar8_button, 2, 3, 1, 1)

        self.toolbar7_button = QPushButton(self.left_frame)
        self.toolbar7_button.setObjectName(u"toolbar7_button")
        sizePolicy2.setHeightForWidth(self.toolbar7_button.sizePolicy().hasHeightForWidth())
        self.toolbar7_button.setSizePolicy(sizePolicy2)
        self.toolbar7_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar7_button, 2, 2, 1, 1)

        self.toolbar2_button = QPushButton(self.left_frame)
        self.toolbar2_button.setObjectName(u"toolbar2_button")
        sizePolicy2.setHeightForWidth(self.toolbar2_button.sizePolicy().hasHeightForWidth())
        self.toolbar2_button.setSizePolicy(sizePolicy2)
        self.toolbar2_button.setMinimumSize(QSize(25, 25))

        self.toolbar_frame.addWidget(self.toolbar2_button, 0, 2, 1, 1)


        self.verticalLayout.addLayout(self.toolbar_frame)

        self.stackedWidget = QStackedWidget(self.left_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 16777215))
        self.curser_widget_0 = QWidget()
        self.curser_widget_0.setObjectName(u"curser_widget_0")
        self.verticalLayout_2 = QVBoxLayout(self.curser_widget_0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.curser_verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.curser_verticalSpacer)

        self.curserPos_label = QLabel(self.curser_widget_0)
        self.curserPos_label.setObjectName(u"curserPos_label")
        self.curserPos_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_2.addWidget(self.curserPos_label)

        self.cursorPos_frame = QFrame(self.curser_widget_0)
        self.cursorPos_frame.setObjectName(u"cursorPos_frame")
        self.cursorPos_frame.setMaximumSize(QSize(16777215, 35))
        self.cursorPos_frame.setFrameShape(QFrame.StyledPanel)
        self.cursorPos_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.cursorPos_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.curserX_label = QLabel(self.cursorPos_frame)
        self.curserX_label.setObjectName(u"curserX_label")

        self.horizontalLayout_2.addWidget(self.curserX_label)

        self.curserY_label = QLabel(self.cursorPos_frame)
        self.curserY_label.setObjectName(u"curserY_label")

        self.horizontalLayout_2.addWidget(self.curserY_label)

        self.curserZ_label = QLabel(self.cursorPos_frame)
        self.curserZ_label.setObjectName(u"curserZ_label")

        self.horizontalLayout_2.addWidget(self.curserZ_label)


        self.verticalLayout_2.addWidget(self.cursorPos_frame)

        self.curserIntensity_label = QLabel(self.curser_widget_0)
        self.curserIntensity_label.setObjectName(u"curserIntensity_label")
        self.curserIntensity_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_2.addWidget(self.curserIntensity_label)

        self.frame_4 = QFrame(self.curser_widget_0)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.curser_widget_0)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.curser_widget_0)
        self.smartClick_widget_3 = QWidget()
        self.smartClick_widget_3.setObjectName(u"smartClick_widget_3")
        self.verticalLayout_7 = QVBoxLayout(self.smartClick_widget_3)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.smartClick_verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_7.addItem(self.smartClick_verticalSpacer)

        self.smartClickType_label = QLabel(self.smartClick_widget_3)
        self.smartClickType_label.setObjectName(u"smartClickType_label")
        self.smartClickType_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_7.addWidget(self.smartClickType_label)

        self.smartClickType_layout = QHBoxLayout()
        self.smartClickType_layout.setObjectName(u"smartClickType_layout")
        self.smartClickType2D_button = QPushButton(self.smartClick_widget_3)
        self.smartClickType2D_button.setObjectName(u"smartClickType2D_button")

        self.smartClickType_layout.addWidget(self.smartClickType2D_button)

        self.smartClickType3D_button = QPushButton(self.smartClick_widget_3)
        self.smartClickType3D_button.setObjectName(u"smartClickType3D_button")

        self.smartClickType_layout.addWidget(self.smartClickType3D_button)


        self.verticalLayout_7.addLayout(self.smartClickType_layout)

        self.smartClickFillHoles_label = QLabel(self.smartClick_widget_3)
        self.smartClickFillHoles_label.setObjectName(u"smartClickFillHoles_label")
        self.smartClickFillHoles_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_7.addWidget(self.smartClickFillHoles_label)

        self.smartClickFillHoles_layout = QHBoxLayout()
        self.smartClickFillHoles_layout.setObjectName(u"smartClickFillHoles_layout")
        self.enable_button = QPushButton(self.smartClick_widget_3)
        self.enable_button.setObjectName(u"enable_button")

        self.smartClickFillHoles_layout.addWidget(self.enable_button)

        self.disable_button = QPushButton(self.smartClick_widget_3)
        self.disable_button.setObjectName(u"disable_button")

        self.smartClickFillHoles_layout.addWidget(self.disable_button)


        self.verticalLayout_7.addLayout(self.smartClickFillHoles_layout)

        self.sensitivity_label = QLabel(self.smartClick_widget_3)
        self.sensitivity_label.setObjectName(u"sensitivity_label")
        self.sensitivity_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_7.addWidget(self.sensitivity_label)

        self.smartClickSensitivity_layout = QHBoxLayout()
        self.smartClickSensitivity_layout.setSpacing(6)
        self.smartClickSensitivity_layout.setObjectName(u"smartClickSensitivity_layout")
        self.smartClickSensitivity_textEdit = QTextEdit(self.smartClick_widget_3)
        self.smartClickSensitivity_textEdit.setObjectName(u"smartClickSensitivity_textEdit")
        self.smartClickSensitivity_textEdit.setMaximumSize(QSize(15, 15))

        self.smartClickSensitivity_layout.addWidget(self.smartClickSensitivity_textEdit)

        self.smartClickSensitivity_slider = QSlider(self.smartClick_widget_3)
        self.smartClickSensitivity_slider.setObjectName(u"smartClickSensitivity_slider")
        self.smartClickSensitivity_slider.setOrientation(Qt.Horizontal)

        self.smartClickSensitivity_layout.addWidget(self.smartClickSensitivity_slider)


        self.verticalLayout_7.addLayout(self.smartClickSensitivity_layout)

        self.stackedWidget.addWidget(self.smartClick_widget_3)
        self.levelset_widget_4 = QWidget()
        self.levelset_widget_4.setObjectName(u"levelset_widget_4")
        self.verticalLayout_6 = QVBoxLayout(self.levelset_widget_4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.levelset_verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_6.addItem(self.levelset_verticalSpacer)

        self.levelsetDefualtSettngs_label = QPushButton(self.levelset_widget_4)
        self.levelsetDefualtSettngs_label.setObjectName(u"levelsetDefualtSettngs_label")

        self.verticalLayout_6.addWidget(self.levelsetDefualtSettngs_label)

        self.levelsetType_label = QLabel(self.levelset_widget_4)
        self.levelsetType_label.setObjectName(u"levelsetType_label")
        self.levelsetType_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_6.addWidget(self.levelsetType_label)

        self.levelsetType_layout = QHBoxLayout()
        self.levelsetType_layout.setObjectName(u"levelsetType_layout")
        self.levelset2D_button = QPushButton(self.levelset_widget_4)
        self.levelset2D_button.setObjectName(u"levelset2D_button")

        self.levelsetType_layout.addWidget(self.levelset2D_button)

        self.levelset3D_button = QPushButton(self.levelset_widget_4)
        self.levelset3D_button.setObjectName(u"levelset3D_button")

        self.levelsetType_layout.addWidget(self.levelset3D_button)


        self.verticalLayout_6.addLayout(self.levelsetType_layout)

        self.levelsetInvert_label = QLabel(self.levelset_widget_4)
        self.levelsetInvert_label.setObjectName(u"levelsetInvert_label")
        self.levelsetInvert_label.setMaximumSize(QSize(16777215, 15))

        self.verticalLayout_6.addWidget(self.levelsetInvert_label)

        self.levelsetInvert_layout = QHBoxLayout()
        self.levelsetInvert_layout.setObjectName(u"levelsetInvert_layout")
        self.levelsetInvertTrue_button = QPushButton(self.levelset_widget_4)
        self.levelsetInvertTrue_button.setObjectName(u"levelsetInvertTrue_button")

        self.levelsetInvert_layout.addWidget(self.levelsetInvertTrue_button)

        self.levelsetInvertFalse_button = QPushButton(self.levelset_widget_4)
        self.levelsetInvertFalse_button.setObjectName(u"levelsetInvertFalse_button")

        self.levelsetInvert_layout.addWidget(self.levelsetInvertFalse_button)


        self.verticalLayout_6.addLayout(self.levelsetInvert_layout)

        self.levelsetMu_label = QLabel(self.levelset_widget_4)
        self.levelsetMu_label.setObjectName(u"levelsetMu_label")

        self.verticalLayout_6.addWidget(self.levelsetMu_label)

        self.levelsetMu_layout = QHBoxLayout()
        self.levelsetMu_layout.setObjectName(u"levelsetMu_layout")
        self.levelsetMu_textEdit = QTextEdit(self.levelset_widget_4)
        self.levelsetMu_textEdit.setObjectName(u"levelsetMu_textEdit")
        self.levelsetMu_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetMu_layout.addWidget(self.levelsetMu_textEdit)

        self.levelsetMu_slider = QSlider(self.levelset_widget_4)
        self.levelsetMu_slider.setObjectName(u"levelsetMu_slider")
        self.levelsetMu_slider.setOrientation(Qt.Horizontal)

        self.levelsetMu_layout.addWidget(self.levelsetMu_slider)


        self.verticalLayout_6.addLayout(self.levelsetMu_layout)

        self.levelsetNu_label = QLabel(self.levelset_widget_4)
        self.levelsetNu_label.setObjectName(u"levelsetNu_label")

        self.verticalLayout_6.addWidget(self.levelsetNu_label)

        self.levelsetNu_layout = QHBoxLayout()
        self.levelsetNu_layout.setObjectName(u"levelsetNu_layout")
        self.levelsetNu_textEdit = QTextEdit(self.levelset_widget_4)
        self.levelsetNu_textEdit.setObjectName(u"levelsetNu_textEdit")
        self.levelsetNu_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetNu_layout.addWidget(self.levelsetNu_textEdit)

        self.levelsetNu_slider = QSlider(self.levelset_widget_4)
        self.levelsetNu_slider.setObjectName(u"levelsetNu_slider")
        self.levelsetNu_slider.setOrientation(Qt.Horizontal)

        self.levelsetNu_layout.addWidget(self.levelsetNu_slider)


        self.verticalLayout_6.addLayout(self.levelsetNu_layout)

        self.levelsetMaxIter_label = QLabel(self.levelset_widget_4)
        self.levelsetMaxIter_label.setObjectName(u"levelsetMaxIter_label")

        self.verticalLayout_6.addWidget(self.levelsetMaxIter_label)

        self.levelsetMaxIter_layout = QHBoxLayout()
        self.levelsetMaxIter_layout.setObjectName(u"levelsetMaxIter_layout")
        self.levelsetMaxIter_textEdit = QTextEdit(self.levelset_widget_4)
        self.levelsetMaxIter_textEdit.setObjectName(u"levelsetMaxIter_textEdit")
        self.levelsetMaxIter_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetMaxIter_layout.addWidget(self.levelsetMaxIter_textEdit)

        self.levelsetMaxIter_slider = QSlider(self.levelset_widget_4)
        self.levelsetMaxIter_slider.setObjectName(u"levelsetMaxIter_slider")
        self.levelsetMaxIter_slider.setOrientation(Qt.Horizontal)

        self.levelsetMaxIter_layout.addWidget(self.levelsetMaxIter_slider)


        self.verticalLayout_6.addLayout(self.levelsetMaxIter_layout)

        self.levelsetEpison_label = QLabel(self.levelset_widget_4)
        self.levelsetEpison_label.setObjectName(u"levelsetEpison_label")

        self.verticalLayout_6.addWidget(self.levelsetEpison_label)

        self.levelsetEpison_layout = QHBoxLayout()
        self.levelsetEpison_layout.setObjectName(u"levelsetEpison_layout")
        self.levelsetEpison_textEdit = QTextEdit(self.levelset_widget_4)
        self.levelsetEpison_textEdit.setObjectName(u"levelsetEpison_textEdit")
        self.levelsetEpison_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetEpison_layout.addWidget(self.levelsetEpison_textEdit)

        self.levelsetEpison_slider = QSlider(self.levelset_widget_4)
        self.levelsetEpison_slider.setObjectName(u"levelsetEpison_slider")
        self.levelsetEpison_slider.setOrientation(Qt.Horizontal)

        self.levelsetEpison_layout.addWidget(self.levelsetEpison_slider)


        self.verticalLayout_6.addLayout(self.levelsetEpison_layout)

        self.levelsetStepValue_label = QLabel(self.levelset_widget_4)
        self.levelsetStepValue_label.setObjectName(u"levelsetStepValue_label")

        self.verticalLayout_6.addWidget(self.levelsetStepValue_label)

        self.levelsetStepValue_layout = QHBoxLayout()
        self.levelsetStepValue_layout.setObjectName(u"levelsetStepValue_layout")
        self.levelsetStepValue_textEdit = QTextEdit(self.levelset_widget_4)
        self.levelsetStepValue_textEdit.setObjectName(u"levelsetStepValue_textEdit")
        self.levelsetStepValue_textEdit.setMaximumSize(QSize(15, 15))

        self.levelsetStepValue_layout.addWidget(self.levelsetStepValue_textEdit)

        self.levelsetStepValue_slider = QSlider(self.levelset_widget_4)
        self.levelsetStepValue_slider.setObjectName(u"levelsetStepValue_slider")
        self.levelsetStepValue_slider.setOrientation(Qt.Horizontal)

        self.levelsetStepValue_layout.addWidget(self.levelsetStepValue_slider)


        self.verticalLayout_6.addLayout(self.levelsetStepValue_layout)

        self.stackedWidget.addWidget(self.levelset_widget_4)
        self.zoom_widget_1 = QWidget()
        self.zoom_widget_1.setObjectName(u"zoom_widget_1")
        self.verticalLayout_3 = QVBoxLayout(self.zoom_widget_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.zoom_verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.zoom_verticalSpacer)

        self.zoomLinked_frame = QFrame(self.zoom_widget_1)
        self.zoomLinked_frame.setObjectName(u"zoomLinked_frame")
        self.zoomLinked_frame.setMaximumSize(QSize(16777215, 50))
        self.zoomLinked_frame.setFrameShape(QFrame.StyledPanel)
        self.zoomLinked_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.zoomLinked_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.zoomLinked_checkBox = QCheckBox(self.zoomLinked_frame)
        self.zoomLinked_checkBox.setObjectName(u"zoomLinked_checkBox")

        self.horizontalLayout_3.addWidget(self.zoomLinked_checkBox)

        self.zoomLinked_textEdit = QTextEdit(self.zoomLinked_frame)
        self.zoomLinked_textEdit.setObjectName(u"zoomLinked_textEdit")
        self.zoomLinked_textEdit.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_3.addWidget(self.zoomLinked_textEdit)


        self.verticalLayout_3.addWidget(self.zoomLinked_frame)

        self.zoomSettings_frame = QFrame(self.zoom_widget_1)
        self.zoomSettings_frame.setObjectName(u"zoomSettings_frame")
        self.zoomSettings_frame.setFrameShape(QFrame.StyledPanel)
        self.zoomSettings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.zoomSettings_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.zoomSettings_label = QLabel(self.zoomSettings_frame)
        self.zoomSettings_label.setObjectName(u"zoomSettings_label")

        self.horizontalLayout_4.addWidget(self.zoomSettings_label)

        self.zoomSettings_frame2 = QFrame(self.zoomSettings_frame)
        self.zoomSettings_frame2.setObjectName(u"zoomSettings_frame2")
        self.zoomSettings_frame2.setFrameShape(QFrame.StyledPanel)
        self.zoomSettings_frame2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.zoomSettings_frame2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.zoomSettings_topFrame = QFrame(self.zoomSettings_frame2)
        self.zoomSettings_topFrame.setObjectName(u"zoomSettings_topFrame")
        self.zoomSettings_topFrame.setFrameShape(QFrame.StyledPanel)
        self.zoomSettings_topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.zoomSettings_topFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.zoomSettingsValue_textEdit = QTextEdit(self.zoomSettings_topFrame)
        self.zoomSettingsValue_textEdit.setObjectName(u"zoomSettingsValue_textEdit")
        sizePolicy2.setHeightForWidth(self.zoomSettingsValue_textEdit.sizePolicy().hasHeightForWidth())
        self.zoomSettingsValue_textEdit.setSizePolicy(sizePolicy2)
        self.zoomSettingsValue_textEdit.setMaximumSize(QSize(16777215, 15))

        self.horizontalLayout_6.addWidget(self.zoomSettingsValue_textEdit)

        self.zoomSettingsValueMetric_textEdit = QTextEdit(self.zoomSettings_topFrame)
        self.zoomSettingsValueMetric_textEdit.setObjectName(u"zoomSettingsValueMetric_textEdit")
        sizePolicy2.setHeightForWidth(self.zoomSettingsValueMetric_textEdit.sizePolicy().hasHeightForWidth())
        self.zoomSettingsValueMetric_textEdit.setSizePolicy(sizePolicy2)
        self.zoomSettingsValueMetric_textEdit.setMaximumSize(QSize(50, 15))

        self.horizontalLayout_6.addWidget(self.zoomSettingsValueMetric_textEdit)


        self.verticalLayout_4.addWidget(self.zoomSettings_topFrame)

        self.zoomSettings_botFrame = QFrame(self.zoomSettings_frame2)
        self.zoomSettings_botFrame.setObjectName(u"zoomSettings_botFrame")
        self.zoomSettings_botFrame.setFrameShape(QFrame.StyledPanel)
        self.zoomSettings_botFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.zoomSettings_botFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.zoomSettings1x_button = QPushButton(self.zoomSettings_botFrame)
        self.zoomSettings1x_button.setObjectName(u"zoomSettings1x_button")

        self.horizontalLayout_5.addWidget(self.zoomSettings1x_button)

        self.zoomSettings2x_button = QPushButton(self.zoomSettings_botFrame)
        self.zoomSettings2x_button.setObjectName(u"zoomSettings2x_button")

        self.horizontalLayout_5.addWidget(self.zoomSettings2x_button)

        self.zoomSettings4x_button = QPushButton(self.zoomSettings_botFrame)
        self.zoomSettings4x_button.setObjectName(u"zoomSettings4x_button")

        self.horizontalLayout_5.addWidget(self.zoomSettings4x_button)


        self.verticalLayout_4.addWidget(self.zoomSettings_botFrame)


        self.horizontalLayout_4.addWidget(self.zoomSettings_frame2)


        self.verticalLayout_3.addWidget(self.zoomSettings_frame)

        self.zoomToFit_button = QPushButton(self.zoom_widget_1)
        self.zoomToFit_button.setObjectName(u"zoomToFit_button")

        self.verticalLayout_3.addWidget(self.zoomToFit_button)

        self.zoomCenterOnCursor_button = QPushButton(self.zoom_widget_1)
        self.zoomCenterOnCursor_button.setObjectName(u"zoomCenterOnCursor_button")

        self.verticalLayout_3.addWidget(self.zoomCenterOnCursor_button)

        self.stackedWidget.addWidget(self.zoom_widget_1)
        self.brush_widget_2 = QWidget()
        self.brush_widget_2.setObjectName(u"brush_widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.brush_widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.brush_verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.brush_verticalSpacer)

        self.brushStyle_label = QLabel(self.brush_widget_2)
        self.brushStyle_label.setObjectName(u"brushStyle_label")

        self.verticalLayout_5.addWidget(self.brushStyle_label)

        self.brushStyle_frame = QFrame(self.brush_widget_2)
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


        self.verticalLayout_5.addWidget(self.brushStyle_frame)

        self.brushSize_label = QLabel(self.brush_widget_2)
        self.brushSize_label.setObjectName(u"brushSize_label")

        self.verticalLayout_5.addWidget(self.brushSize_label)

        self.brushSize_frame = QFrame(self.brush_widget_2)
        self.brushSize_frame.setObjectName(u"brushSize_frame")
        self.brushSize_frame.setFrameShape(QFrame.StyledPanel)
        self.brushSize_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.brushSize_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.brushSize_textEdit = QTextEdit(self.brushSize_frame)
        self.brushSize_textEdit.setObjectName(u"brushSize_textEdit")
        self.brushSize_textEdit.setMaximumSize(QSize(15, 16777215))

        self.horizontalLayout_8.addWidget(self.brushSize_textEdit)

        self.brushSize_slider = QSlider(self.brushSize_frame)
        self.brushSize_slider.setObjectName(u"brushSize_slider")
        self.brushSize_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.brushSize_slider)


        self.verticalLayout_5.addWidget(self.brushSize_frame)

        self.brushOptions_labe = QLabel(self.brush_widget_2)
        self.brushOptions_labe.setObjectName(u"brushOptions_labe")

        self.verticalLayout_5.addWidget(self.brushOptions_labe)

        self.brushSettings_layout = QGridLayout()
        self.brushSettings_layout.setObjectName(u"brushSettings_layout")
        self.brushCursorChasesBrush_checkBox = QCheckBox(self.brush_widget_2)
        self.brushCursorChasesBrush_checkBox.setObjectName(u"brushCursorChasesBrush_checkBox")

        self.brushSettings_layout.addWidget(self.brushCursorChasesBrush_checkBox, 1, 0, 1, 1)

        self.brush3D_checkBox = QCheckBox(self.brush_widget_2)
        self.brush3D_checkBox.setObjectName(u"brush3D_checkBox")

        self.brushSettings_layout.addWidget(self.brush3D_checkBox, 0, 0, 1, 1)

        self.brushIsotroopic_checkBox = QCheckBox(self.brush_widget_2)
        self.brushIsotroopic_checkBox.setObjectName(u"brushIsotroopic_checkBox")

        self.brushSettings_layout.addWidget(self.brushIsotroopic_checkBox, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.brushSettings_layout)

        self.stackedWidget.addWidget(self.brush_widget_2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.seg_frame = QFrame(self.left_frame)
        self.seg_frame.setObjectName(u"seg_frame")
        self.seg_frame.setMinimumSize(QSize(0, 75))
        self.seg_frame.setFrameShape(QFrame.StyledPanel)
        self.seg_frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.seg_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 71, 16))

        self.verticalLayout.addWidget(self.seg_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.right_frame = QFrame(self.centralwidget)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.right_frame_2 = QGridLayout(self.right_frame)
        self.right_frame_2.setSpacing(0)
        self.right_frame_2.setObjectName(u"right_frame_2")
        self.right_frame_2.setContentsMargins(0, 0, 0, 0)
        self.viewer_stackedWidget = QStackedWidget(self.right_frame)
        self.viewer_stackedWidget.setObjectName(u"viewer_stackedWidget")
        self.multiViewer = QWidget()
        self.multiViewer.setObjectName(u"multiViewer")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.multiViewer.sizePolicy().hasHeightForWidth())
        self.multiViewer.setSizePolicy(sizePolicy3)
        self.multiViewer.setBaseSize(QSize(50, 50))
        self.gridLayout = QGridLayout(self.multiViewer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.botRight_frame = QFrame(self.multiViewer)
        self.botRight_frame.setObjectName(u"botRight_frame")
        self.botRight_frame.setMinimumSize(QSize(200, 200))
        self.botRight_frame.setFrameShape(QFrame.StyledPanel)
        self.botRight_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.botRight_frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.botRightTop_layout = QHBoxLayout()
        self.botRightTop_layout.setSpacing(0)
        self.botRightTop_layout.setObjectName(u"botRightTop_layout")
        self.botRight_label = QLabel(self.botRight_frame)
        self.botRight_label.setObjectName(u"botRight_label")
        sizePolicy.setHeightForWidth(self.botRight_label.sizePolicy().hasHeightForWidth())
        self.botRight_label.setSizePolicy(sizePolicy)

        self.botRightTop_layout.addWidget(self.botRight_label)

        self.botRightTop_frame = QVBoxLayout()
        self.botRightTop_frame.setObjectName(u"botRightTop_frame")
        self.botRight_button = QPushButton(self.botRight_frame)
        self.botRight_button.setObjectName(u"botRight_button")
        sizePolicy2.setHeightForWidth(self.botRight_button.sizePolicy().hasHeightForWidth())
        self.botRight_button.setSizePolicy(sizePolicy2)
        self.botRight_button.setMaximumSize(QSize(25, 25))

        self.botRightTop_frame.addWidget(self.botRight_button)

        self.botRight_scrollBar = QScrollBar(self.botRight_frame)
        self.botRight_scrollBar.setObjectName(u"botRight_scrollBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.botRight_scrollBar.sizePolicy().hasHeightForWidth())
        self.botRight_scrollBar.setSizePolicy(sizePolicy4)
        self.botRight_scrollBar.setMaximumSize(QSize(25, 16777215))
        self.botRight_scrollBar.setOrientation(Qt.Vertical)

        self.botRightTop_frame.addWidget(self.botRight_scrollBar)


        self.botRightTop_layout.addLayout(self.botRightTop_frame)


        self.verticalLayout_10.addLayout(self.botRightTop_layout)

        self.botRightBot_layout = QHBoxLayout()
        self.botRightBot_layout.setObjectName(u"botRightBot_layout")
        self.botRightBot_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.botRightBot_layout.addItem(self.botRightBot_spacer)

        self.botRightZoomToFit_button = QPushButton(self.botRight_frame)
        self.botRightZoomToFit_button.setObjectName(u"botRightZoomToFit_button")

        self.botRightBot_layout.addWidget(self.botRightZoomToFit_button)

        self.botRightZoomToFit_label = QLabel(self.botRight_frame)
        self.botRightZoomToFit_label.setObjectName(u"botRightZoomToFit_label")
        self.botRightZoomToFit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.botRightBot_layout.addWidget(self.botRightZoomToFit_label)


        self.verticalLayout_10.addLayout(self.botRightBot_layout)


        self.gridLayout.addWidget(self.botRight_frame, 1, 1, 1, 1)

        self.topLeft_frame = QFrame(self.multiViewer)
        self.topLeft_frame.setObjectName(u"topLeft_frame")
        self.topLeft_frame.setMinimumSize(QSize(200, 200))
        self.topLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.topLeft_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topLeft_frame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.topLeftTop_layout = QHBoxLayout()
        self.topLeftTop_layout.setSpacing(0)
        self.topLeftTop_layout.setObjectName(u"topLeftTop_layout")
        self.topLeft_label = QLabel(self.topLeft_frame)
        self.topLeft_label.setObjectName(u"topLeft_label")
        sizePolicy.setHeightForWidth(self.topLeft_label.sizePolicy().hasHeightForWidth())
        self.topLeft_label.setSizePolicy(sizePolicy)

        self.topLeftTop_layout.addWidget(self.topLeft_label)

        self.topLeftTop_frame = QVBoxLayout()
        self.topLeftTop_frame.setObjectName(u"topLeftTop_frame")
        self.topLeft_button = QPushButton(self.topLeft_frame)
        self.topLeft_button.setObjectName(u"topLeft_button")
        sizePolicy2.setHeightForWidth(self.topLeft_button.sizePolicy().hasHeightForWidth())
        self.topLeft_button.setSizePolicy(sizePolicy2)
        self.topLeft_button.setMaximumSize(QSize(25, 25))

        self.topLeftTop_frame.addWidget(self.topLeft_button)

        self.topLeft_scrollBar = QScrollBar(self.topLeft_frame)
        self.topLeft_scrollBar.setObjectName(u"topLeft_scrollBar")
        sizePolicy4.setHeightForWidth(self.topLeft_scrollBar.sizePolicy().hasHeightForWidth())
        self.topLeft_scrollBar.setSizePolicy(sizePolicy4)
        self.topLeft_scrollBar.setMaximumSize(QSize(25, 16777215))
        self.topLeft_scrollBar.setOrientation(Qt.Vertical)

        self.topLeftTop_frame.addWidget(self.topLeft_scrollBar)


        self.topLeftTop_layout.addLayout(self.topLeftTop_frame)


        self.verticalLayout_8.addLayout(self.topLeftTop_layout)

        self.topLeftBot_layout = QHBoxLayout()
        self.topLeftBot_layout.setObjectName(u"topLeftBot_layout")
        self.topLeftBot_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topLeftBot_layout.addItem(self.topLeftBot_spacer)

        self.topLeftZoomToFit_button = QPushButton(self.topLeft_frame)
        self.topLeftZoomToFit_button.setObjectName(u"topLeftZoomToFit_button")

        self.topLeftBot_layout.addWidget(self.topLeftZoomToFit_button)

        self.topLeftZoomToFit_label = QLabel(self.topLeft_frame)
        self.topLeftZoomToFit_label.setObjectName(u"topLeftZoomToFit_label")
        self.topLeftZoomToFit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topLeftBot_layout.addWidget(self.topLeftZoomToFit_label)


        self.verticalLayout_8.addLayout(self.topLeftBot_layout)


        self.gridLayout.addWidget(self.topLeft_frame, 0, 0, 1, 1)

        self.botLeft_frame = QFrame(self.multiViewer)
        self.botLeft_frame.setObjectName(u"botLeft_frame")
        self.botLeft_frame.setMinimumSize(QSize(200, 200))
        self.botLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.botLeft_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.botLeft_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.botLeftTop_layout = QHBoxLayout()
        self.botLeftTop_layout.setSpacing(0)
        self.botLeftTop_layout.setObjectName(u"botLeftTop_layout")
        self.botLeft_label = QLabel(self.botLeft_frame)
        self.botLeft_label.setObjectName(u"botLeft_label")
        sizePolicy.setHeightForWidth(self.botLeft_label.sizePolicy().hasHeightForWidth())
        self.botLeft_label.setSizePolicy(sizePolicy)
        self.botLeft_label.setAutoFillBackground(False)

        self.botLeftTop_layout.addWidget(self.botLeft_label)

        self.botLeftTop_frame = QVBoxLayout()
        self.botLeftTop_frame.setObjectName(u"botLeftTop_frame")
        self.botLeft_button = QPushButton(self.botLeft_frame)
        self.botLeft_button.setObjectName(u"botLeft_button")
        sizePolicy2.setHeightForWidth(self.botLeft_button.sizePolicy().hasHeightForWidth())
        self.botLeft_button.setSizePolicy(sizePolicy2)
        self.botLeft_button.setMaximumSize(QSize(25, 25))

        self.botLeftTop_frame.addWidget(self.botLeft_button)

        self.botLeft_scrollBar = QScrollBar(self.botLeft_frame)
        self.botLeft_scrollBar.setObjectName(u"botLeft_scrollBar")
        sizePolicy4.setHeightForWidth(self.botLeft_scrollBar.sizePolicy().hasHeightForWidth())
        self.botLeft_scrollBar.setSizePolicy(sizePolicy4)
        self.botLeft_scrollBar.setMaximumSize(QSize(25, 16777215))
        self.botLeft_scrollBar.setOrientation(Qt.Vertical)

        self.botLeftTop_frame.addWidget(self.botLeft_scrollBar)


        self.botLeftTop_layout.addLayout(self.botLeftTop_frame)


        self.verticalLayout_11.addLayout(self.botLeftTop_layout)

        self.botLeftBot_layout = QHBoxLayout()
        self.botLeftBot_layout.setObjectName(u"botLeftBot_layout")
        self.botLeftBot_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.botLeftBot_layout.addItem(self.botLeftBot_spacer)

        self.botLeftZoomToFit_button = QPushButton(self.botLeft_frame)
        self.botLeftZoomToFit_button.setObjectName(u"botLeftZoomToFit_button")

        self.botLeftBot_layout.addWidget(self.botLeftZoomToFit_button)

        self.botLeftZoomToFit_label = QLabel(self.botLeft_frame)
        self.botLeftZoomToFit_label.setObjectName(u"botLeftZoomToFit_label")
        self.botLeftZoomToFit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.botLeftBot_layout.addWidget(self.botLeftZoomToFit_label)


        self.verticalLayout_11.addLayout(self.botLeftBot_layout)


        self.gridLayout.addWidget(self.botLeft_frame, 1, 0, 1, 1)

        self.topRight_frame = QFrame(self.multiViewer)
        self.topRight_frame.setObjectName(u"topRight_frame")
        self.topRight_frame.setMinimumSize(QSize(200, 200))
        self.topRight_frame.setFrameShape(QFrame.StyledPanel)
        self.topRight_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.topRight_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.topRightTop_layout = QHBoxLayout()
        self.topRightTop_layout.setSpacing(0)
        self.topRightTop_layout.setObjectName(u"topRightTop_layout")
        self.topRight_label = QLabel(self.topRight_frame)
        self.topRight_label.setObjectName(u"topRight_label")
        sizePolicy.setHeightForWidth(self.topRight_label.sizePolicy().hasHeightForWidth())
        self.topRight_label.setSizePolicy(sizePolicy)

        self.topRightTop_layout.addWidget(self.topRight_label)

        self.topRightTop_frame = QVBoxLayout()
        self.topRightTop_frame.setObjectName(u"topRightTop_frame")
        self.topRight_button = QPushButton(self.topRight_frame)
        self.topRight_button.setObjectName(u"topRight_button")
        sizePolicy2.setHeightForWidth(self.topRight_button.sizePolicy().hasHeightForWidth())
        self.topRight_button.setSizePolicy(sizePolicy2)
        self.topRight_button.setMaximumSize(QSize(25, 25))

        self.topRightTop_frame.addWidget(self.topRight_button)

        self.topRight_scrollBar = QScrollBar(self.topRight_frame)
        self.topRight_scrollBar.setObjectName(u"topRight_scrollBar")
        sizePolicy4.setHeightForWidth(self.topRight_scrollBar.sizePolicy().hasHeightForWidth())
        self.topRight_scrollBar.setSizePolicy(sizePolicy4)
        self.topRight_scrollBar.setMaximumSize(QSize(25, 16777215))
        self.topRight_scrollBar.setOrientation(Qt.Vertical)

        self.topRightTop_frame.addWidget(self.topRight_scrollBar)


        self.topRightTop_layout.addLayout(self.topRightTop_frame)


        self.verticalLayout_9.addLayout(self.topRightTop_layout)

        self.topRightBot_layout = QHBoxLayout()
        self.topRightBot_layout.setObjectName(u"topRightBot_layout")
        self.topRightBot_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.topRightBot_layout.addItem(self.topRightBot_spacer)

        self.topRightZoomToFit_button = QPushButton(self.topRight_frame)
        self.topRightZoomToFit_button.setObjectName(u"topRightZoomToFit_button")

        self.topRightBot_layout.addWidget(self.topRightZoomToFit_button)

        self.topRightZoomToFit_label = QLabel(self.topRight_frame)
        self.topRightZoomToFit_label.setObjectName(u"topRightZoomToFit_label")
        self.topRightZoomToFit_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.topRightBot_layout.addWidget(self.topRightZoomToFit_label)


        self.verticalLayout_9.addLayout(self.topRightBot_layout)


        self.gridLayout.addWidget(self.topRight_frame, 0, 1, 1, 1)

        self.viewer_stackedWidget.addWidget(self.multiViewer)
        self.singleViewer = QWidget()
        self.singleViewer.setObjectName(u"singleViewer")
        self.verticalLayout_14 = QVBoxLayout(self.singleViewer)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.singleTop_layout = QHBoxLayout()
        self.singleTop_layout.setObjectName(u"singleTop_layout")
        self.singleTop_graphicsView = QLabel(self.singleViewer)
        self.singleTop_graphicsView.setObjectName(u"singleTop_graphicsView")

        self.singleTop_layout.addWidget(self.singleTop_graphicsView)

        self.singleTop_frame = QVBoxLayout()
        self.singleTop_frame.setObjectName(u"singleTop_frame")
        self.single_button = QPushButton(self.singleViewer)
        self.single_button.setObjectName(u"single_button")
        self.single_button.setMaximumSize(QSize(25, 25))

        self.singleTop_frame.addWidget(self.single_button)

        self.singleTop_scrollBar = QScrollBar(self.singleViewer)
        self.singleTop_scrollBar.setObjectName(u"singleTop_scrollBar")
        self.singleTop_scrollBar.setMaximumSize(QSize(25, 16777215))
        self.singleTop_scrollBar.setOrientation(Qt.Vertical)

        self.singleTop_frame.addWidget(self.singleTop_scrollBar)


        self.singleTop_layout.addLayout(self.singleTop_frame)


        self.verticalLayout_14.addLayout(self.singleTop_layout)

        self.singleBot_layout = QHBoxLayout()
        self.singleBot_layout.setObjectName(u"singleBot_layout")
        self.singleBot_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.singleBot_layout.addItem(self.singleBot_spacer)

        self.singleBot_button = QPushButton(self.singleViewer)
        self.singleBot_button.setObjectName(u"singleBot_button")

        self.singleBot_layout.addWidget(self.singleBot_button)

        self.singleBot_label = QLabel(self.singleViewer)
        self.singleBot_label.setObjectName(u"singleBot_label")

        self.singleBot_layout.addWidget(self.singleBot_label)


        self.verticalLayout_14.addLayout(self.singleBot_layout)

        self.viewer_stackedWidget.addWidget(self.singleViewer)

        self.right_frame_2.addWidget(self.viewer_stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.right_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 960, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuSave_Segmentation = QMenu(self.menuFile)
        self.menuSave_Segmentation.setObjectName(u"menuSave_Segmentation")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuSegmentation = QMenu(self.menubar)
        self.menuSegmentation.setObjectName(u"menuSegmentation")
        self.menuClear_Segmentation = QMenu(self.menuSegmentation)
        self.menuClear_Segmentation.setObjectName(u"menuClear_Segmentation")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSegmentation.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_Segmentation)
        self.menuFile.addAction(self.actionOpen_Organ)
        self.menuFile.addAction(self.menuSave_Segmentation.menuAction())
        self.menuSave_Segmentation.addAction(self.actionSave)
        self.menuSave_Segmentation.addAction(self.actionSave_As)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionHide_Segmentation)
        self.menuSegmentation.addAction(self.menuClear_Segmentation.menuAction())
        self.menuSegmentation.addAction(self.actionVolume_and_Statistics)
        self.menuClear_Segmentation.addAction(self.actionClear_All)
        self.menuClear_Segmentation.addAction(self.actionExcluding_Organ)
        self.menuTools.addAction(self.actionReorient_Image)
        self.menuTools.addAction(self.actionDice_Score)
        self.menuHelp.addAction(self.actionAbout_IRIS)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.viewer_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IRIS by Collin Li", None))
        self.actionOpen_Image.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.actionOpen_Segmentation.setText(QCoreApplication.translate("MainWindow", u"Open Segmentation", None))
        self.actionOpen_Organ.setText(QCoreApplication.translate("MainWindow", u"Open Organ", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionHide_Segmentation.setText(QCoreApplication.translate("MainWindow", u"Hide Segmentation", None))
        self.actionClear_All.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionExcluding_Organ.setText(QCoreApplication.translate("MainWindow", u"Excluding Organ", None))
        self.actionVolume_and_Statistics.setText(QCoreApplication.translate("MainWindow", u"Volume and Statistics", None))
        self.actionReorient_Image.setText(QCoreApplication.translate("MainWindow", u"Reorient Image", None))
        self.actionDice_Score.setText(QCoreApplication.translate("MainWindow", u"Dice Score", None))
        self.actionAbout_IRIS.setText(QCoreApplication.translate("MainWindow", u"About IRIS", None))
        self.toolbar4_button.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.toolbar6_button.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.toolbar5_button.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.toolbar0_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.toolbar1_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.toolbar3_button.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.toolbar9_button.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.toolbar8_button.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.toolbar7_button.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.toolbar2_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.curserPos_label.setText(QCoreApplication.translate("MainWindow", u"Curser Position (x,y,z)", None))
        self.curserX_label.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.curserY_label.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.curserZ_label.setText(QCoreApplication.translate("MainWindow", u"#", None))
        self.curserIntensity_label.setText(QCoreApplication.translate("MainWindow", u"Intensity (min,max,cur):", None))
        self.smartClickType_label.setText(QCoreApplication.translate("MainWindow", u"SmartClick Type", None))
        self.smartClickType2D_button.setText(QCoreApplication.translate("MainWindow", u"2D", None))
        self.smartClickType3D_button.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.smartClickFillHoles_label.setText(QCoreApplication.translate("MainWindow", u"Fill Holes:", None))
        self.enable_button.setText(QCoreApplication.translate("MainWindow", u"enable", None))
        self.disable_button.setText(QCoreApplication.translate("MainWindow", u"disable", None))
        self.sensitivity_label.setText(QCoreApplication.translate("MainWindow", u"Sensitivity:", None))
        self.levelsetDefualtSettngs_label.setText(QCoreApplication.translate("MainWindow", u"Default Settings", None))
        self.levelsetType_label.setText(QCoreApplication.translate("MainWindow", u"Levelset Type", None))
        self.levelset2D_button.setText(QCoreApplication.translate("MainWindow", u"2D", None))
        self.levelset3D_button.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.levelsetInvert_label.setText(QCoreApplication.translate("MainWindow", u"Levelset Invert", None))
        self.levelsetInvertTrue_button.setText(QCoreApplication.translate("MainWindow", u"True", None))
        self.levelsetInvertFalse_button.setText(QCoreApplication.translate("MainWindow", u"False", None))
        self.levelsetMu_label.setText(QCoreApplication.translate("MainWindow", u"\u03bc value: 1.0-5.0", None))
        self.levelsetMu_textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8pt;\"><br /></p></body></html>", None))
        self.levelsetNu_label.setText(QCoreApplication.translate("MainWindow", u"n value: 0.0-5.0", None))
        self.levelsetMaxIter_label.setText(QCoreApplication.translate("MainWindow", u"max iter: 0-100", None))
        self.levelsetEpison_label.setText(QCoreApplication.translate("MainWindow", u"\u03b5 value 0.0-1.0", None))
        self.levelsetStepValue_label.setText(QCoreApplication.translate("MainWindow", u"step value: 0-1", None))
        self.zoomLinked_checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.zoomLinked_textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">Linked zoom</span></p></body></html>", None))
        self.zoomSettings_label.setText(QCoreApplication.translate("MainWindow", u"Zoom:", None))
        self.zoomSettingsValueMetric_textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt;\">px/mm</span></p></body></html>", None))
        self.zoomSettings1x_button.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.zoomSettings2x_button.setText(QCoreApplication.translate("MainWindow", u"2x", None))
        self.zoomSettings4x_button.setText(QCoreApplication.translate("MainWindow", u"4x", None))
        self.zoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"Zoom to fit", None))
        self.zoomCenterOnCursor_button.setText(QCoreApplication.translate("MainWindow", u"Center on cursor", None))
        self.brushStyle_label.setText(QCoreApplication.translate("MainWindow", u"Brush Style:", None))
        self.brushStyleSquare_button.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.brushStyleCircle_button.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.brushStyleMorph_button.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.brushSize_label.setText(QCoreApplication.translate("MainWindow", u"Brush Size:", None))
        self.brushOptions_labe.setText(QCoreApplication.translate("MainWindow", u"Brush Options:", None))
        self.brushCursorChasesBrush_checkBox.setText(QCoreApplication.translate("MainWindow", u"Cursor chases brush", None))
        self.brush3D_checkBox.setText(QCoreApplication.translate("MainWindow", u"3D", None))
        self.brushIsotroopic_checkBox.setText(QCoreApplication.translate("MainWindow", u"Isotropic", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Active Label", None))
        self.botRight_label.setText("")
        self.botRight_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.botRightZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.botRightZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.topLeft_label.setText("")
        self.topLeft_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.topLeftZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.topLeftZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.botLeft_label.setText("")
        self.botLeft_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.botLeftZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.botLeftZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.topRight_label.setText("")
        self.topRight_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.topRightZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.topRightZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.singleTop_graphicsView.setText("")
        self.single_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.singleBot_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.singleBot_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave_Segmentation.setTitle(QCoreApplication.translate("MainWindow", u"Save Segmentation", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSegmentation.setTitle(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.menuClear_Segmentation.setTitle(QCoreApplication.translate("MainWindow", u"Clear Segmentation", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


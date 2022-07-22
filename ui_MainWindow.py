# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindowrvxsDm.ui'
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
        icon.addFile(u"./icons/Cornell_University_seal.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.actionDebug = QAction(MainWindow)
        self.actionDebug.setObjectName(u"actionDebug")
        self.actionSelect_Theme = QAction(MainWindow)
        self.actionSelect_Theme.setObjectName(u"actionSelect_Theme")
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

        self.verticalLayout.addWidget(self.stackedWidget)

        self.seg_frame = QFrame(self.left_frame)
        self.seg_frame.setObjectName(u"seg_frame")
        self.seg_frame.setMinimumSize(QSize(0, 150))
        self.seg_frame.setFrameShape(QFrame.StyledPanel)
        self.seg_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.seg_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.segActiveLabel_layout = QHBoxLayout()
        self.segActiveLabel_layout.setObjectName(u"segActiveLabel_layout")
        self.setActiveLabel_label = QLabel(self.seg_frame)
        self.setActiveLabel_label.setObjectName(u"setActiveLabel_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.setActiveLabel_label.sizePolicy().hasHeightForWidth())
        self.setActiveLabel_label.setSizePolicy(sizePolicy3)
        self.setActiveLabel_label.setMinimumSize(QSize(0, 0))
        self.setActiveLabel_label.setMaximumSize(QSize(80, 16777215))

        self.segActiveLabel_layout.addWidget(self.setActiveLabel_label)

        self.segActiveLabel_combobox = QComboBox(self.seg_frame)
        self.segActiveLabel_combobox.setObjectName(u"segActiveLabel_combobox")

        self.segActiveLabel_layout.addWidget(self.segActiveLabel_combobox)


        self.verticalLayout_2.addLayout(self.segActiveLabel_layout)

        self.insertLabel_layout = QHBoxLayout()
        self.insertLabel_layout.setObjectName(u"insertLabel_layout")
        self.segAddLabel_button = QPushButton(self.seg_frame)
        self.segAddLabel_button.setObjectName(u"segAddLabel_button")

        self.insertLabel_layout.addWidget(self.segAddLabel_button)

        self.segRemoveLabel_button = QPushButton(self.seg_frame)
        self.segRemoveLabel_button.setObjectName(u"segRemoveLabel_button")

        self.insertLabel_layout.addWidget(self.segRemoveLabel_button)


        self.verticalLayout_2.addLayout(self.insertLabel_layout)

        self.segOpa_layout = QHBoxLayout()
        self.segOpa_layout.setObjectName(u"segOpa_layout")
        self.segOpa_label = QLabel(self.seg_frame)
        self.segOpa_label.setObjectName(u"segOpa_label")

        self.segOpa_layout.addWidget(self.segOpa_label)

        self.segOpa_spacer = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.segOpa_layout.addItem(self.segOpa_spacer)

        self.segOpa_slider = QSlider(self.seg_frame)
        self.segOpa_slider.setObjectName(u"segOpa_slider")
        self.segOpa_slider.setMaximum(100)
        self.segOpa_slider.setSliderPosition(50)
        self.segOpa_slider.setOrientation(Qt.Horizontal)
        self.segOpa_slider.setTickPosition(QSlider.NoTicks)

        self.segOpa_layout.addWidget(self.segOpa_slider)


        self.verticalLayout_2.addLayout(self.segOpa_layout)


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
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.multiViewer.sizePolicy().hasHeightForWidth())
        self.multiViewer.setSizePolicy(sizePolicy4)
        self.multiViewer.setBaseSize(QSize(50, 50))
        self.gridLayout = QGridLayout(self.multiViewer)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.topLeft_scrollBar.sizePolicy().hasHeightForWidth())
        self.topLeft_scrollBar.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.topRight_scrollBar.sizePolicy().hasHeightForWidth())
        self.topRight_scrollBar.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.botRight_scrollBar.sizePolicy().hasHeightForWidth())
        self.botRight_scrollBar.setSizePolicy(sizePolicy5)
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
        sizePolicy5.setHeightForWidth(self.botLeft_scrollBar.sizePolicy().hasHeightForWidth())
        self.botLeft_scrollBar.setSizePolicy(sizePolicy5)
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

        self.viewer_stackedWidget.addWidget(self.multiViewer)

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
        self.menuHelp.addAction(self.actionDebug)
        self.menuHelp.addAction(self.actionSelect_Theme)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(-1)
        self.viewer_stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IRIS by Collin Li", None))
        self.actionOpen_Image.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
#if QT_CONFIG(shortcut)
        self.actionOpen_Image.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen_Segmentation.setText(QCoreApplication.translate("MainWindow", u"Open Segmentation", None))
        self.actionOpen_Organ.setText(QCoreApplication.translate("MainWindow", u"Open Organ", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_As.setText(QCoreApplication.translate("MainWindow", u"Save As", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
#if QT_CONFIG(shortcut)
        self.actionUndo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
#if QT_CONFIG(shortcut)
        self.actionRedo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionHide_Segmentation.setText(QCoreApplication.translate("MainWindow", u"Hide Segmentation", None))
#if QT_CONFIG(shortcut)
        self.actionHide_Segmentation.setShortcut(QCoreApplication.translate("MainWindow", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.actionClear_All.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.actionExcluding_Organ.setText(QCoreApplication.translate("MainWindow", u"Excluding Organ", None))
        self.actionVolume_and_Statistics.setText(QCoreApplication.translate("MainWindow", u"Volume and Statistics", None))
        self.actionReorient_Image.setText(QCoreApplication.translate("MainWindow", u"Reorient Image", None))
        self.actionDice_Score.setText(QCoreApplication.translate("MainWindow", u"Dice Score", None))
        self.actionAbout_IRIS.setText(QCoreApplication.translate("MainWindow", u"About IRIS", None))
        self.actionDebug.setText(QCoreApplication.translate("MainWindow", u"Debug", None))
        self.actionSelect_Theme.setText(QCoreApplication.translate("MainWindow", u"Select Theme", None))
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
        self.setActiveLabel_label.setText(QCoreApplication.translate("MainWindow", u"Active Label:", None))
        self.segAddLabel_button.setText(QCoreApplication.translate("MainWindow", u"Add Label", None))
        self.segRemoveLabel_button.setText(QCoreApplication.translate("MainWindow", u"Remove Label", None))
        self.segOpa_label.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.topLeft_label.setText("")
        self.topLeft_button.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.topLeftZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.topLeftZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.topRight_label.setText("")
        self.topRight_button.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.topRightZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.topRightZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.botRight_label.setText("")
        self.botRight_button.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.botRightZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.botRightZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.botLeft_label.setText("")
        self.botLeft_button.setText("")
        self.botLeftZoomToFit_button.setText(QCoreApplication.translate("MainWindow", u"zoom to fit", None))
        self.botLeftZoomToFit_label.setText(QCoreApplication.translate("MainWindow", u"# of #", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuSave_Segmentation.setTitle(QCoreApplication.translate("MainWindow", u"Save Segmentation", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuSegmentation.setTitle(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.menuClear_Segmentation.setTitle(QCoreApplication.translate("MainWindow", u"Clear Segmentation", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi


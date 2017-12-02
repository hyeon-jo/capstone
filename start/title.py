# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'title.ui'
#
# Created by: PyQt5 UI code generator 5.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(1324, 790)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setIconSize(QtCore.QSize(0, 0))
        MainWindow.setAnimated(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(370, 660, 511, 111))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setStyleSheet("color: rgb(78, 182, 255);")
        self.pushButton_3.setText("세팅 버튼")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet("color: rgb(78, 182, 255);")
        self.pushButton_2.setText("시작 버튼")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.AWS_logo = QtWidgets.QLabel(self.centralwidget)
        self.AWS_logo.setGeometry(QtCore.QRect(30, 559, 221, 221))
        self.AWS_logo.setText("")
        self.AWS_logo.setPixmap(QtGui.QPixmap(":/drone/logo.png"))
        self.AWS_logo.setScaledContents(True)
        self.AWS_logo.setObjectName("AWS_logo")
        self.warehouse_Name = QtWidgets.QLabel(self.centralwidget)
        self.warehouse_Name.setGeometry(QtCore.QRect(400, 60, 491, 41))
        self.warehouse_Name.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.warehouse_Name.setStyleSheet("color: rgb(78, 182, 255);\n"
"font: 18pt \"HY중고딕\";\n"
"")
        self.warehouse_Name.setText("1공장 창고 2")
        self.warehouse_Name.setTextFormat(QtCore.Qt.AutoText)
        self.warehouse_Name.setAlignment(QtCore.Qt.AlignCenter)
        self.warehouse_Name.setObjectName("warehouse_Name")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 70, 214, 178))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_drone = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_drone.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_drone.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_drone.setSpacing(0)
        self.verticalLayout_drone.setObjectName("verticalLayout_drone")
        self.drone_label1 = QtWidgets.QPushButton(self.layoutWidget)
        self.drone_label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drone_label1.setAutoFillBackground(False)
        self.drone_label1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/drone_label/drone_label.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(":/drone_label/drone_label_clicked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.drone_label1.setIcon(icon)
        self.drone_label1.setIconSize(QtCore.QSize(200, 80))
        self.drone_label1.setCheckable(True)
        self.drone_label1.setChecked(True)
        self.drone_label1.setAutoRepeat(False)
        self.drone_label1.setAutoDefault(False)
        self.drone_label1.setObjectName("drone_label1")
        self.dronegroup = QtWidgets.QButtonGroup(MainWindow)
        self.dronegroup.setObjectName("dronegroup")
        self.dronegroup.addButton(self.drone_label1)
        self.verticalLayout_drone.addWidget(self.drone_label1)
        self.drone_pluslabel = QtWidgets.QPushButton(self.layoutWidget)
        self.drone_pluslabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.drone_pluslabel.setAutoFillBackground(False)
        self.drone_pluslabel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/drone_label/drone_pluselabel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/drone_label/drone_pluselabel_clicked.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.drone_pluslabel.setIcon(icon1)
        self.drone_pluslabel.setIconSize(QtCore.QSize(200, 80))
        self.drone_pluslabel.setCheckable(True)
        self.drone_pluslabel.setChecked(False)
        self.drone_pluslabel.setAutoRepeat(False)
        self.drone_pluslabel.setAutoDefault(False)
        self.drone_pluslabel.setObjectName("drone_pluslabel")
        self.dronegroup.addButton(self.drone_pluslabel)
        self.verticalLayout_drone.addWidget(self.drone_pluslabel)
        self.batteryGuage = QtWidgets.QOpenGLWidget(self.centralwidget)
        self.batteryGuage.setGeometry(QtCore.QRect(1010, 510, 260, 260))
        self.batteryGuage.setObjectName("batteryGuage")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(1000, 300, 291, 191))
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("GOODS")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(QtGui.QColor(0, 100, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("EAC")
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("하이하이루")
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setText("하이")
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.tableWidget.setItem(0, 1, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.video_frame = QtWidgets.QLabel(self.centralwidget)
        self.video_frame.setGeometry(QtCore.QRect(290, 120, 680, 490))
        self.video_frame.setText("")
        self.video_frame.setPixmap(QtGui.QPixmap(":/drone/그림1.png"))
        self.video_frame.setScaledContents(True)
        self.video_frame.setObjectName("video_frame")
        self.tempMap = QtWidgets.QTableWidget(self.centralwidget)
        self.tempMap.setGeometry(QtCore.QRect(1000, 20, 291, 261))
        self.tempMap.setStyleSheet("border: 0.5px solid rgb(78, 182, 255);\n"
"border-radius: 10px;")
        self.tempMap.setFrameShape(QtWidgets.QFrame.Box)
        self.tempMap.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tempMap.setLineWidth(10)
        self.tempMap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempMap.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tempMap.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tempMap.setTabKeyNavigation(False)
        self.tempMap.setProperty("showDropIndicator", False)
        self.tempMap.setDragDropOverwriteMode(False)
        self.tempMap.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tempMap.setGridStyle(QtCore.Qt.SolidLine)
        self.tempMap.setCornerButtonEnabled(False)
        self.tempMap.setObjectName("tempMap")
        self.tempMap.setColumnCount(2)
        self.tempMap.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tempMap.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tempMap.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tempMap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tempMap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(182, 78, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        self.tempMap.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tempMap.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tempMap.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.tempMap.setItem(1, 1, item)
        self.tempMap.horizontalHeader().setVisible(False)
        self.tempMap.horizontalHeader().setCascadingSectionResizes(True)
        self.tempMap.verticalHeader().setVisible(False)
        self.tempMap.verticalHeader().setCascadingSectionResizes(True)
        self.tempMap.verticalHeader().setSortIndicatorShown(False)
        self.tempMap.verticalHeader().setStretchLastSection(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 51, 41))
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/button/turnoff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1010, 330, 201, 151))
        self.label.setStyleSheet("border: 0.5px solid rgb(78, 182, 255);\n"
"border-radius: 10px;")
        self.label.setObjectName("label")
        self.tableWidget.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.AWS_logo.raise_()
        self.warehouse_Name.raise_()
        self.layoutWidget.raise_()
        self.batteryGuage.raise_()
        self.video_frame.raise_()
        self.tempMap.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1324, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.temp)
        self.drone_pluslabel.clicked.connect(MainWindow.add_drone)
        self.pushButton_2.clicked.connect(MainWindow.start_drone)
        self.pushButton.clicked.connect(MainWindow.turnOffAWS)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AWS"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tempMap.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tempMap.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Row"))
        item = self.tempMap.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tempMap.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "New Column"))
        __sortingEnabled = self.tempMap.isSortingEnabled()
        self.tempMap.setSortingEnabled(False)
        self.tempMap.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "TextLabel"))

import drone_rc

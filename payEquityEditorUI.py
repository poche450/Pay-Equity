# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'payEquityEditor1.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 975)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1600, 975))
        MainWindow.setMaximumSize(QSize(1600, 975))
        font = QFont()
        font.setFamily(u"Noto Sans Mono CJK KR")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"3442056-head-hunting/png/041-legal.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setTabShape(QTabWidget.Triangular)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1600, 975))
        self.centralwidget.setMaximumSize(QSize(1600, 975))
        self.centralwidget.setCursor(QCursor(Qt.ArrowCursor))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(48, 32))
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setTabsClosable(False)
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.groupBox_27 = QGroupBox(self.tab_21)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.groupBox_27.setGeometry(QRect(20, 160, 471, 671))
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_27)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget = QTableWidget(self.groupBox_27)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 10):
            self.tableWidget.setRowCount(10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.DotLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.horizontalLayout_2.addWidget(self.tableWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_7 = QPushButton(self.groupBox_27)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton = QPushButton(self.groupBox_27)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.groupBox_27)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.groupBox_27)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.pushButton_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.groupBox_28 = QGroupBox(self.tab_21)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.groupBox_28.setGeometry(QRect(20, 10, 1141, 136))
        self.gridLayout_13 = QGridLayout(self.groupBox_28)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.lineEdit_3 = QLineEdit(self.groupBox_28)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_11.addWidget(self.lineEdit_3, 0, 3, 1, 1)

        self.label_48 = QLabel(self.groupBox_28)
        self.label_48.setObjectName(u"label_48")

        self.gridLayout_11.addWidget(self.label_48, 0, 0, 1, 1)

        self.label_78 = QLabel(self.groupBox_28)
        self.label_78.setObjectName(u"label_78")

        self.gridLayout_11.addWidget(self.label_78, 1, 0, 1, 1)

        self.lineEdit_15 = QLineEdit(self.groupBox_28)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.gridLayout_11.addWidget(self.lineEdit_15, 1, 3, 1, 1)

        self.label_79 = QLabel(self.groupBox_28)
        self.label_79.setObjectName(u"label_79")

        self.gridLayout_11.addWidget(self.label_79, 0, 2, 1, 1)

        self.lineEdit_14 = QLineEdit(self.groupBox_28)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.gridLayout_11.addWidget(self.lineEdit_14, 0, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_28)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_11.addWidget(self.lineEdit_4, 1, 1, 1, 1)

        self.label_80 = QLabel(self.groupBox_28)
        self.label_80.setObjectName(u"label_80")

        self.gridLayout_11.addWidget(self.label_80, 1, 2, 1, 1)

        self.label_81 = QLabel(self.groupBox_28)
        self.label_81.setObjectName(u"label_81")

        self.gridLayout_11.addWidget(self.label_81, 2, 0, 1, 1)

        self.comboBox = QComboBox(self.groupBox_28)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_11.addWidget(self.comboBox, 2, 1, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_11, 0, 0, 1, 1)

        self.groupBox_29 = QGroupBox(self.tab_21)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.groupBox_29.setGeometry(QRect(510, 160, 651, 228))
        self.groupBox_29.setFlat(False)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_29)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableView_4 = QTableView(self.groupBox_29)
        self.tableView_4.setObjectName(u"tableView_4")

        self.verticalLayout_6.addWidget(self.tableView_4)

        self.groupBox_30 = QGroupBox(self.tab_21)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.groupBox_30.setGeometry(QRect(510, 399, 651, 305))
        self.gridLayout_14 = QGridLayout(self.groupBox_30)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_46 = QLabel(self.groupBox_30)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_46, 0, 2, 1, 1)

        self.spinBox_4 = QSpinBox(self.groupBox_30)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setReadOnly(True)
        self.spinBox_4.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_4.setMaximum(999999999)

        self.gridLayout_10.addWidget(self.spinBox_4, 1, 0, 1, 1)

        self.spinBox_5 = QSpinBox(self.groupBox_30)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setReadOnly(True)
        self.spinBox_5.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_5.setMaximum(999999999)

        self.gridLayout_10.addWidget(self.spinBox_5, 1, 2, 1, 1)

        self.label_45 = QLabel(self.groupBox_30)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_45, 0, 0, 1, 1)

        self.label_47 = QLabel(self.groupBox_30)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setWordWrap(True)

        self.gridLayout_10.addWidget(self.label_47, 0, 4, 1, 1)

        self.spinBox_6 = QSpinBox(self.groupBox_30)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setReadOnly(True)
        self.spinBox_6.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_6.setMaximum(999999999)

        self.gridLayout_10.addWidget(self.spinBox_6, 1, 4, 1, 1)


        self.gridLayout_14.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.tableView_3 = QTableView(self.groupBox_30)
        self.tableView_3.setObjectName(u"tableView_3")

        self.gridLayout_14.addWidget(self.tableView_3, 1, 0, 1, 1)

        self.groupBox_31 = QGroupBox(self.tab_21)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.groupBox_31.setGeometry(QRect(510, 720, 661, 108))
        self.gridLayout_9 = QGridLayout(self.groupBox_31)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_5 = QPushButton(self.groupBox_31)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_9.addWidget(self.pushButton_5, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_31)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_9.addWidget(self.pushButton_6, 1, 0, 2, 1)

        self.pushButton_3 = QPushButton(self.groupBox_31)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_9.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.groupBox_31)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_9.addWidget(self.pushButton_4, 1, 2, 2, 1)

        self.tabWidget.addTab(self.tab_21, icon, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 10, 512, 792))
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_3.addWidget(self.label_40, 0, 0, 1, 1)

        self.entryPayScaleName = QLineEdit(self.groupBox)
        self.entryPayScaleName.setObjectName(u"entryPayScaleName")

        self.gridLayout_3.addWidget(self.entryPayScaleName, 0, 1, 1, 1)

        self.pushButtonFetchPayScale = QPushButton(self.groupBox)
        self.pushButtonFetchPayScale.setObjectName(u"pushButtonFetchPayScale")

        self.gridLayout_3.addWidget(self.pushButtonFetchPayScale, 0, 2, 1, 1)

        self.pushButtonSavePayScale = QPushButton(self.groupBox)
        self.pushButtonSavePayScale.setObjectName(u"pushButtonSavePayScale")

        self.gridLayout_3.addWidget(self.pushButtonSavePayScale, 0, 3, 1, 1)

        self.label_41 = QLabel(self.groupBox)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_3.addWidget(self.label_41, 1, 0, 1, 1)

        self.entryPayScaleID = QLineEdit(self.groupBox)
        self.entryPayScaleID.setObjectName(u"entryPayScaleID")

        self.gridLayout_3.addWidget(self.entryPayScaleID, 1, 1, 1, 1)

        self.label_39 = QLabel(self.groupBox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_3.addWidget(self.label_39, 2, 0, 1, 1)

        self.entryDateFrom = QDateEdit(self.groupBox)
        self.entryDateFrom.setObjectName(u"entryDateFrom")

        self.gridLayout_3.addWidget(self.entryDateFrom, 2, 1, 1, 1)

        self.label_42 = QLabel(self.groupBox)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_42, 2, 2, 1, 1)

        self.entryDateTo = QDateEdit(self.groupBox)
        self.entryDateTo.setObjectName(u"entryDateTo")

        self.gridLayout_3.addWidget(self.entryDateTo, 2, 3, 1, 1)

        self.label_36 = QLabel(self.groupBox)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_3.addWidget(self.label_36, 3, 1, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_3.addWidget(self.label_37, 3, 2, 1, 1)

        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_3.addWidget(self.label_38, 3, 3, 1, 1)

        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.gridLayout_3.addWidget(self.doubleSpinBox, 4, 1, 1, 1)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")

        self.gridLayout_3.addWidget(self.doubleSpinBox_3, 4, 3, 1, 1)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)

        self.doubleSpinBox_4 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setObjectName(u"doubleSpinBox_4")

        self.gridLayout_3.addWidget(self.doubleSpinBox_4, 5, 1, 1, 1)

        self.doubleSpinBox_6 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setObjectName(u"doubleSpinBox_6")

        self.gridLayout_3.addWidget(self.doubleSpinBox_6, 5, 3, 1, 1)

        self.label_18 = QLabel(self.groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 6, 0, 1, 1)

        self.doubleSpinBox_7 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setObjectName(u"doubleSpinBox_7")

        self.gridLayout_3.addWidget(self.doubleSpinBox_7, 6, 1, 1, 1)

        self.doubleSpinBox_9 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_9.setObjectName(u"doubleSpinBox_9")

        self.gridLayout_3.addWidget(self.doubleSpinBox_9, 6, 3, 1, 1)

        self.label_19 = QLabel(self.groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 7, 0, 1, 1)

        self.doubleSpinBox_11 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_11.setObjectName(u"doubleSpinBox_11")

        self.gridLayout_3.addWidget(self.doubleSpinBox_11, 7, 1, 1, 1)

        self.doubleSpinBox_12 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_12.setObjectName(u"doubleSpinBox_12")

        self.gridLayout_3.addWidget(self.doubleSpinBox_12, 7, 3, 1, 1)

        self.label_20 = QLabel(self.groupBox)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_3.addWidget(self.label_20, 8, 0, 1, 1)

        self.doubleSpinBox_13 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_13.setObjectName(u"doubleSpinBox_13")

        self.gridLayout_3.addWidget(self.doubleSpinBox_13, 8, 1, 1, 1)

        self.doubleSpinBox_15 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_15.setObjectName(u"doubleSpinBox_15")

        self.gridLayout_3.addWidget(self.doubleSpinBox_15, 8, 3, 1, 1)

        self.label_21 = QLabel(self.groupBox)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_3.addWidget(self.label_21, 9, 0, 1, 1)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.gridLayout_3.addWidget(self.doubleSpinBox_2, 9, 1, 1, 1)

        self.doubleSpinBox_35 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_35.setObjectName(u"doubleSpinBox_35")

        self.gridLayout_3.addWidget(self.doubleSpinBox_35, 9, 3, 1, 1)

        self.label_22 = QLabel(self.groupBox)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_3.addWidget(self.label_22, 10, 0, 1, 1)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")

        self.gridLayout_3.addWidget(self.doubleSpinBox_5, 10, 1, 1, 1)

        self.doubleSpinBox_36 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_36.setObjectName(u"doubleSpinBox_36")

        self.gridLayout_3.addWidget(self.doubleSpinBox_36, 10, 3, 1, 1)

        self.label_23 = QLabel(self.groupBox)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_3.addWidget(self.label_23, 11, 0, 1, 1)

        self.doubleSpinBox_8 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_8.setObjectName(u"doubleSpinBox_8")

        self.gridLayout_3.addWidget(self.doubleSpinBox_8, 11, 1, 1, 1)

        self.doubleSpinBox_37 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_37.setObjectName(u"doubleSpinBox_37")

        self.gridLayout_3.addWidget(self.doubleSpinBox_37, 11, 3, 1, 1)

        self.label_24 = QLabel(self.groupBox)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_3.addWidget(self.label_24, 12, 0, 1, 1)

        self.doubleSpinBox_10 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_10.setObjectName(u"doubleSpinBox_10")

        self.gridLayout_3.addWidget(self.doubleSpinBox_10, 12, 1, 1, 1)

        self.doubleSpinBox_38 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_38.setObjectName(u"doubleSpinBox_38")

        self.gridLayout_3.addWidget(self.doubleSpinBox_38, 12, 3, 1, 1)

        self.label_25 = QLabel(self.groupBox)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_3.addWidget(self.label_25, 13, 0, 1, 1)

        self.doubleSpinBox_14 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_14.setObjectName(u"doubleSpinBox_14")

        self.gridLayout_3.addWidget(self.doubleSpinBox_14, 13, 1, 1, 1)

        self.doubleSpinBox_39 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_39.setObjectName(u"doubleSpinBox_39")

        self.gridLayout_3.addWidget(self.doubleSpinBox_39, 13, 3, 1, 1)

        self.label_26 = QLabel(self.groupBox)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_3.addWidget(self.label_26, 14, 0, 1, 1)

        self.doubleSpinBox_16 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_16.setObjectName(u"doubleSpinBox_16")

        self.gridLayout_3.addWidget(self.doubleSpinBox_16, 14, 1, 1, 1)

        self.doubleSpinBox_40 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_40.setObjectName(u"doubleSpinBox_40")

        self.gridLayout_3.addWidget(self.doubleSpinBox_40, 14, 3, 1, 1)

        self.label_27 = QLabel(self.groupBox)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_3.addWidget(self.label_27, 15, 0, 1, 1)

        self.doubleSpinBox_17 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_17.setObjectName(u"doubleSpinBox_17")

        self.gridLayout_3.addWidget(self.doubleSpinBox_17, 15, 1, 1, 1)

        self.doubleSpinBox_26 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_26.setObjectName(u"doubleSpinBox_26")

        self.gridLayout_3.addWidget(self.doubleSpinBox_26, 15, 2, 1, 1)

        self.doubleSpinBox_41 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_41.setObjectName(u"doubleSpinBox_41")

        self.gridLayout_3.addWidget(self.doubleSpinBox_41, 15, 3, 1, 1)

        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_3.addWidget(self.label_28, 16, 0, 1, 1)

        self.doubleSpinBox_18 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_18.setObjectName(u"doubleSpinBox_18")

        self.gridLayout_3.addWidget(self.doubleSpinBox_18, 16, 1, 1, 1)

        self.doubleSpinBox_27 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_27.setObjectName(u"doubleSpinBox_27")

        self.gridLayout_3.addWidget(self.doubleSpinBox_27, 16, 2, 1, 1)

        self.doubleSpinBox_42 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_42.setObjectName(u"doubleSpinBox_42")

        self.gridLayout_3.addWidget(self.doubleSpinBox_42, 16, 3, 1, 1)

        self.label_29 = QLabel(self.groupBox)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_3.addWidget(self.label_29, 17, 0, 1, 1)

        self.doubleSpinBox_19 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_19.setObjectName(u"doubleSpinBox_19")

        self.gridLayout_3.addWidget(self.doubleSpinBox_19, 17, 1, 1, 1)

        self.doubleSpinBox_28 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_28.setObjectName(u"doubleSpinBox_28")

        self.gridLayout_3.addWidget(self.doubleSpinBox_28, 17, 2, 1, 1)

        self.doubleSpinBox_43 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_43.setObjectName(u"doubleSpinBox_43")

        self.gridLayout_3.addWidget(self.doubleSpinBox_43, 17, 3, 1, 1)

        self.label_30 = QLabel(self.groupBox)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_3.addWidget(self.label_30, 18, 0, 1, 1)

        self.doubleSpinBox_20 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_20.setObjectName(u"doubleSpinBox_20")

        self.gridLayout_3.addWidget(self.doubleSpinBox_20, 18, 1, 1, 1)

        self.doubleSpinBox_29 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_29.setObjectName(u"doubleSpinBox_29")

        self.gridLayout_3.addWidget(self.doubleSpinBox_29, 18, 2, 1, 1)

        self.doubleSpinBox_44 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_44.setObjectName(u"doubleSpinBox_44")

        self.gridLayout_3.addWidget(self.doubleSpinBox_44, 18, 3, 1, 1)

        self.label_31 = QLabel(self.groupBox)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_3.addWidget(self.label_31, 19, 0, 1, 1)

        self.doubleSpinBox_21 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_21.setObjectName(u"doubleSpinBox_21")

        self.gridLayout_3.addWidget(self.doubleSpinBox_21, 19, 1, 1, 1)

        self.doubleSpinBox_30 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_30.setObjectName(u"doubleSpinBox_30")

        self.gridLayout_3.addWidget(self.doubleSpinBox_30, 19, 2, 1, 1)

        self.doubleSpinBox_45 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_45.setObjectName(u"doubleSpinBox_45")

        self.gridLayout_3.addWidget(self.doubleSpinBox_45, 19, 3, 1, 1)

        self.label_32 = QLabel(self.groupBox)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_3.addWidget(self.label_32, 20, 0, 1, 1)

        self.doubleSpinBox_22 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_22.setObjectName(u"doubleSpinBox_22")

        self.gridLayout_3.addWidget(self.doubleSpinBox_22, 20, 1, 1, 1)

        self.doubleSpinBox_31 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_31.setObjectName(u"doubleSpinBox_31")

        self.gridLayout_3.addWidget(self.doubleSpinBox_31, 20, 2, 1, 1)

        self.doubleSpinBox_46 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_46.setObjectName(u"doubleSpinBox_46")

        self.gridLayout_3.addWidget(self.doubleSpinBox_46, 20, 3, 1, 1)

        self.label_33 = QLabel(self.groupBox)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_3.addWidget(self.label_33, 21, 0, 1, 1)

        self.doubleSpinBox_23 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_23.setObjectName(u"doubleSpinBox_23")

        self.gridLayout_3.addWidget(self.doubleSpinBox_23, 21, 1, 1, 1)

        self.doubleSpinBox_32 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_32.setObjectName(u"doubleSpinBox_32")

        self.gridLayout_3.addWidget(self.doubleSpinBox_32, 21, 2, 1, 1)

        self.doubleSpinBox_47 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_47.setObjectName(u"doubleSpinBox_47")

        self.gridLayout_3.addWidget(self.doubleSpinBox_47, 21, 3, 1, 1)

        self.label_34 = QLabel(self.groupBox)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_3.addWidget(self.label_34, 22, 0, 1, 1)

        self.doubleSpinBox_24 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_24.setObjectName(u"doubleSpinBox_24")

        self.gridLayout_3.addWidget(self.doubleSpinBox_24, 22, 1, 1, 1)

        self.doubleSpinBox_33 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_33.setObjectName(u"doubleSpinBox_33")

        self.gridLayout_3.addWidget(self.doubleSpinBox_33, 22, 2, 1, 1)

        self.doubleSpinBox_48 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_48.setObjectName(u"doubleSpinBox_48")

        self.gridLayout_3.addWidget(self.doubleSpinBox_48, 22, 3, 1, 1)

        self.label_35 = QLabel(self.groupBox)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_3.addWidget(self.label_35, 23, 0, 1, 1)

        self.doubleSpinBox_25 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_25.setObjectName(u"doubleSpinBox_25")

        self.gridLayout_3.addWidget(self.doubleSpinBox_25, 23, 1, 1, 1)

        self.doubleSpinBox_34 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_34.setObjectName(u"doubleSpinBox_34")

        self.gridLayout_3.addWidget(self.doubleSpinBox_34, 23, 2, 1, 1)

        self.doubleSpinBox_49 = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_49.setObjectName(u"doubleSpinBox_49")

        self.gridLayout_3.addWidget(self.doubleSpinBox_49, 23, 3, 1, 1)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(660, 13, 426, 391))
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.doubleSpinBox_52 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_52.setObjectName(u"doubleSpinBox_52")

        self.gridLayout_8.addWidget(self.doubleSpinBox_52, 1, 1, 1, 1)

        self.doubleSpinBox_51 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_51.setObjectName(u"doubleSpinBox_51")

        self.gridLayout_8.addWidget(self.doubleSpinBox_51, 1, 3, 1, 1)

        self.label_70 = QLabel(self.groupBox_2)
        self.label_70.setObjectName(u"label_70")

        self.gridLayout_8.addWidget(self.label_70, 3, 0, 1, 1)

        self.label_72 = QLabel(self.groupBox_2)
        self.label_72.setObjectName(u"label_72")

        self.gridLayout_8.addWidget(self.label_72, 5, 0, 1, 1)

        self.label_76 = QLabel(self.groupBox_2)
        self.label_76.setObjectName(u"label_76")

        self.gridLayout_8.addWidget(self.label_76, 9, 0, 1, 1)

        self.label_74 = QLabel(self.groupBox_2)
        self.label_74.setObjectName(u"label_74")

        self.gridLayout_8.addWidget(self.label_74, 7, 0, 1, 1)

        self.label_67 = QLabel(self.groupBox_2)
        self.label_67.setObjectName(u"label_67")

        self.gridLayout_8.addWidget(self.label_67, 0, 3, 1, 1)

        self.label_65 = QLabel(self.groupBox_2)
        self.label_65.setObjectName(u"label_65")

        self.gridLayout_8.addWidget(self.label_65, 1, 0, 1, 1)

        self.label_66 = QLabel(self.groupBox_2)
        self.label_66.setObjectName(u"label_66")

        self.gridLayout_8.addWidget(self.label_66, 0, 2, 1, 1)

        self.lineEdit_11 = QLineEdit(self.groupBox_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.gridLayout_8.addWidget(self.lineEdit_11, 0, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_2)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_8.addWidget(self.label_68, 0, 0, 1, 1)

        self.label_73 = QLabel(self.groupBox_2)
        self.label_73.setObjectName(u"label_73")

        self.gridLayout_8.addWidget(self.label_73, 6, 0, 1, 1)

        self.doubleSpinBox_50 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_50.setObjectName(u"doubleSpinBox_50")

        self.gridLayout_8.addWidget(self.doubleSpinBox_50, 1, 2, 1, 1)

        self.label_71 = QLabel(self.groupBox_2)
        self.label_71.setObjectName(u"label_71")

        self.gridLayout_8.addWidget(self.label_71, 4, 0, 1, 1)

        self.label_69 = QLabel(self.groupBox_2)
        self.label_69.setObjectName(u"label_69")

        self.gridLayout_8.addWidget(self.label_69, 2, 0, 1, 1)

        self.label_75 = QLabel(self.groupBox_2)
        self.label_75.setObjectName(u"label_75")

        self.gridLayout_8.addWidget(self.label_75, 8, 0, 1, 1)

        self.label_77 = QLabel(self.groupBox_2)
        self.label_77.setObjectName(u"label_77")

        self.gridLayout_8.addWidget(self.label_77, 10, 0, 1, 1)

        self.doubleSpinBox_53 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_53.setObjectName(u"doubleSpinBox_53")

        self.gridLayout_8.addWidget(self.doubleSpinBox_53, 2, 1, 1, 1)

        self.doubleSpinBox_54 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_54.setObjectName(u"doubleSpinBox_54")

        self.gridLayout_8.addWidget(self.doubleSpinBox_54, 2, 2, 1, 1)

        self.doubleSpinBox_55 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_55.setObjectName(u"doubleSpinBox_55")

        self.gridLayout_8.addWidget(self.doubleSpinBox_55, 2, 3, 1, 1)

        self.doubleSpinBox_56 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_56.setObjectName(u"doubleSpinBox_56")

        self.gridLayout_8.addWidget(self.doubleSpinBox_56, 3, 1, 1, 1)

        self.doubleSpinBox_57 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_57.setObjectName(u"doubleSpinBox_57")

        self.gridLayout_8.addWidget(self.doubleSpinBox_57, 3, 2, 1, 1)

        self.doubleSpinBox_58 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_58.setObjectName(u"doubleSpinBox_58")

        self.gridLayout_8.addWidget(self.doubleSpinBox_58, 3, 3, 1, 1)

        self.doubleSpinBox_59 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_59.setObjectName(u"doubleSpinBox_59")

        self.gridLayout_8.addWidget(self.doubleSpinBox_59, 4, 1, 1, 1)

        self.doubleSpinBox_60 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_60.setObjectName(u"doubleSpinBox_60")

        self.gridLayout_8.addWidget(self.doubleSpinBox_60, 4, 2, 1, 1)

        self.doubleSpinBox_61 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_61.setObjectName(u"doubleSpinBox_61")

        self.gridLayout_8.addWidget(self.doubleSpinBox_61, 4, 3, 1, 1)

        self.doubleSpinBox_62 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_62.setObjectName(u"doubleSpinBox_62")

        self.gridLayout_8.addWidget(self.doubleSpinBox_62, 5, 1, 1, 1)

        self.doubleSpinBox_63 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_63.setObjectName(u"doubleSpinBox_63")

        self.gridLayout_8.addWidget(self.doubleSpinBox_63, 5, 2, 1, 1)

        self.doubleSpinBox_64 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_64.setObjectName(u"doubleSpinBox_64")

        self.gridLayout_8.addWidget(self.doubleSpinBox_64, 5, 3, 1, 1)

        self.doubleSpinBox_65 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_65.setObjectName(u"doubleSpinBox_65")

        self.gridLayout_8.addWidget(self.doubleSpinBox_65, 6, 1, 1, 1)

        self.doubleSpinBox_66 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_66.setObjectName(u"doubleSpinBox_66")

        self.gridLayout_8.addWidget(self.doubleSpinBox_66, 6, 2, 1, 1)

        self.doubleSpinBox_67 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_67.setObjectName(u"doubleSpinBox_67")

        self.gridLayout_8.addWidget(self.doubleSpinBox_67, 6, 3, 1, 1)

        self.doubleSpinBox_68 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_68.setObjectName(u"doubleSpinBox_68")

        self.gridLayout_8.addWidget(self.doubleSpinBox_68, 7, 1, 1, 1)

        self.doubleSpinBox_69 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_69.setObjectName(u"doubleSpinBox_69")

        self.gridLayout_8.addWidget(self.doubleSpinBox_69, 7, 2, 1, 1)

        self.doubleSpinBox_70 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_70.setObjectName(u"doubleSpinBox_70")

        self.gridLayout_8.addWidget(self.doubleSpinBox_70, 7, 3, 1, 1)

        self.doubleSpinBox_71 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_71.setObjectName(u"doubleSpinBox_71")

        self.gridLayout_8.addWidget(self.doubleSpinBox_71, 8, 1, 1, 1)

        self.doubleSpinBox_72 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_72.setObjectName(u"doubleSpinBox_72")

        self.gridLayout_8.addWidget(self.doubleSpinBox_72, 8, 2, 1, 1)

        self.doubleSpinBox_73 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_73.setObjectName(u"doubleSpinBox_73")

        self.gridLayout_8.addWidget(self.doubleSpinBox_73, 8, 3, 1, 1)

        self.doubleSpinBox_74 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_74.setObjectName(u"doubleSpinBox_74")

        self.gridLayout_8.addWidget(self.doubleSpinBox_74, 9, 1, 1, 1)

        self.doubleSpinBox_75 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_75.setObjectName(u"doubleSpinBox_75")

        self.gridLayout_8.addWidget(self.doubleSpinBox_75, 9, 2, 1, 1)

        self.doubleSpinBox_76 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_76.setObjectName(u"doubleSpinBox_76")

        self.gridLayout_8.addWidget(self.doubleSpinBox_76, 9, 3, 1, 1)

        self.doubleSpinBox_77 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_77.setObjectName(u"doubleSpinBox_77")

        self.gridLayout_8.addWidget(self.doubleSpinBox_77, 10, 1, 1, 1)

        self.doubleSpinBox_78 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_78.setObjectName(u"doubleSpinBox_78")

        self.gridLayout_8.addWidget(self.doubleSpinBox_78, 10, 2, 1, 1)

        self.doubleSpinBox_79 = QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_79.setObjectName(u"doubleSpinBox_79")

        self.gridLayout_8.addWidget(self.doubleSpinBox_79, 10, 3, 1, 1)

        self.groupBox_26 = QGroupBox(self.tab)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.groupBox_26.setGeometry(QRect(660, 430, 431, 371))
        icon1 = QIcon()
        icon1.addFile(u"3442056-head-hunting/png/003-salary.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayoutWidget_4 = QWidget(self.tab_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(10, 20, 1561, 861))
        self.jobDescriptionMain = QGridLayout(self.gridLayoutWidget_4)
        self.jobDescriptionMain.setObjectName(u"jobDescriptionMain")
        self.jobDescriptionMain.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20 = QGridLayout()
        self.gridLayout_20.setObjectName(u"gridLayout_20")

        self.jobDescriptionMain.addLayout(self.gridLayout_20, 0, 1, 2, 1)

        self.tableView_2 = QTableView(self.gridLayoutWidget_4)
        self.tableView_2.setObjectName(u"tableView_2")

        self.jobDescriptionMain.addWidget(self.tableView_2, 1, 0, 1, 1)

        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.pushButton_10 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_19.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_19.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.label_86 = QLabel(self.gridLayoutWidget_4)
        self.label_86.setObjectName(u"label_86")

        self.gridLayout_19.addWidget(self.label_86, 0, 0, 1, 2)

        self.label_87 = QLabel(self.gridLayoutWidget_4)
        self.label_87.setObjectName(u"label_87")

        self.gridLayout_19.addWidget(self.label_87, 1, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.gridLayoutWidget_4)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_19.addWidget(self.comboBox_2, 1, 1, 1, 1)


        self.jobDescriptionMain.addLayout(self.gridLayout_19, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_32 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.gridLayout_6 = QGridLayout(self.groupBox_32)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_63 = QLabel(self.groupBox_32)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_6.addWidget(self.label_63, 1, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.groupBox_32)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_6.addWidget(self.pushButton_13, 1, 2, 1, 1)

        self.entryJobDescriptionResponsabilities = QTextEdit(self.groupBox_32)
        self.entryJobDescriptionResponsabilities.setObjectName(u"entryJobDescriptionResponsabilities")

        self.gridLayout_6.addWidget(self.entryJobDescriptionResponsabilities, 3, 0, 1, 3)

        self.lineEdit_5 = QLineEdit(self.groupBox_32)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_6.addWidget(self.lineEdit_5, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.label_88 = QLabel(self.groupBox_32)
        self.label_88.setObjectName(u"label_88")

        self.gridLayout_6.addWidget(self.label_88, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_32)

        self.groupBox_4 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_5 = QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.lineEdit_6 = QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 2, 1, 1)

        self.pushButton_11 = QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_5.addWidget(self.pushButton_11, 1, 2, 1, 1)

        self.label_62 = QLabel(self.groupBox_4)
        self.label_62.setObjectName(u"label_62")

        self.gridLayout_5.addWidget(self.label_62, 1, 0, 1, 1)

        self.label_89 = QLabel(self.groupBox_4)
        self.label_89.setObjectName(u"label_89")

        self.gridLayout_5.addWidget(self.label_89, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.entryJobDescriptionQualifications = QTextEdit(self.groupBox_4)
        self.entryJobDescriptionQualifications.setObjectName(u"entryJobDescriptionQualifications")

        self.gridLayout_5.addWidget(self.entryJobDescriptionQualifications, 2, 0, 1, 3)


        self.verticalLayout_5.addWidget(self.groupBox_4)

        self.groupBox_33 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_33.setObjectName(u"groupBox_33")
        self.gridLayout_7 = QGridLayout(self.groupBox_33)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_7 = QLineEdit(self.groupBox_33)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.gridLayout_7.addWidget(self.lineEdit_7, 1, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.groupBox_33)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_7.addWidget(self.pushButton_12, 2, 2, 1, 1)

        self.label_90 = QLabel(self.groupBox_33)
        self.label_90.setObjectName(u"label_90")

        self.gridLayout_7.addWidget(self.label_90, 1, 1, 1, 1)

        self.entryJobDescriptionWorkingConditions = QTextEdit(self.groupBox_33)
        self.entryJobDescriptionWorkingConditions.setObjectName(u"entryJobDescriptionWorkingConditions")

        self.gridLayout_7.addWidget(self.entryJobDescriptionWorkingConditions, 3, 0, 1, 3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)

        self.label_64 = QLabel(self.groupBox_33)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_7.addWidget(self.label_64, 2, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.groupBox_33)


        self.jobDescriptionMain.addLayout(self.verticalLayout_5, 1, 2, 2, 1)

        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_3 = QGroupBox(self.gridLayoutWidget_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.entryJobLevelCode = QLineEdit(self.groupBox_3)
        self.entryJobLevelCode.setObjectName(u"entryJobLevelCode")

        self.gridLayout_4.addWidget(self.entryJobLevelCode, 3, 7, 1, 1)

        self.entryJobLevel = QLineEdit(self.groupBox_3)
        self.entryJobLevel.setObjectName(u"entryJobLevel")

        self.gridLayout_4.addWidget(self.entryJobLevel, 2, 7, 1, 1)

        self.entryJobID = QLineEdit(self.groupBox_3)
        self.entryJobID.setObjectName(u"entryJobID")

        self.gridLayout_4.addWidget(self.entryJobID, 0, 7, 1, 1)

        self.isUnionisable = QCheckBox(self.groupBox_3)
        self.isUnionisable.setObjectName(u"isUnionisable")

        self.gridLayout_4.addWidget(self.isUnionisable, 4, 7, 1, 1)

        self.entryPayScaleID_2 = QLineEdit(self.groupBox_3)
        self.entryPayScaleID_2.setObjectName(u"entryPayScaleID_2")

        self.gridLayout_4.addWidget(self.entryPayScaleID_2, 1, 7, 1, 1)

        self.pushButtonCreateJobDescription = QPushButton(self.groupBox_3)
        self.pushButtonCreateJobDescription.setObjectName(u"pushButtonCreateJobDescription")

        self.gridLayout_4.addWidget(self.pushButtonCreateJobDescription, 4, 5, 1, 1)

        self.label_61 = QLabel(self.groupBox_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_61, 2, 0, 1, 1)

        self.label_57 = QLabel(self.groupBox_3)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_57, 1, 0, 1, 1)

        self.label_43 = QLabel(self.groupBox_3)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_43, 2, 5, 1, 1)

        self.label_44 = QLabel(self.groupBox_3)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_44, 3, 5, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_60 = QLabel(self.groupBox_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_60, 1, 5, 1, 1)

        self.label_59 = QLabel(self.groupBox_3)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_59, 3, 0, 1, 1)

        self.label_58 = QLabel(self.groupBox_3)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.label_58, 0, 5, 1, 1)

        self.pushButtonFetchJobDescription = QPushButton(self.groupBox_3)
        self.pushButtonFetchJobDescription.setObjectName(u"pushButtonFetchJobDescription")

        self.gridLayout_4.addWidget(self.pushButtonFetchJobDescription, 4, 4, 1, 1)

        self.entryJobTitle = QLineEdit(self.groupBox_3)
        self.entryJobTitle.setObjectName(u"entryJobTitle")

        self.gridLayout_4.addWidget(self.entryJobTitle, 0, 1, 1, 4)

        self.entryFirstLevelManager = QLineEdit(self.groupBox_3)
        self.entryFirstLevelManager.setObjectName(u"entryFirstLevelManager")

        self.gridLayout_4.addWidget(self.entryFirstLevelManager, 1, 1, 1, 4)

        self.entryBusinessUnit = QLineEdit(self.groupBox_3)
        self.entryBusinessUnit.setObjectName(u"entryBusinessUnit")

        self.gridLayout_4.addWidget(self.entryBusinessUnit, 2, 1, 1, 4)

        self.entryFunctionUnit = QLineEdit(self.groupBox_3)
        self.entryFunctionUnit.setObjectName(u"entryFunctionUnit")

        self.gridLayout_4.addWidget(self.entryFunctionUnit, 3, 1, 1, 4)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 4, 3, 1, 1)


        self.gridLayout_18.addWidget(self.groupBox_3, 0, 0, 1, 1)


        self.jobDescriptionMain.addLayout(self.gridLayout_18, 0, 2, 1, 1)

        icon2 = QIcon()
        icon2.addFile(u"3442056-head-hunting/png/013-skills.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.currentJobEvaluation = QGroupBox(self.tab_3)
        self.currentJobEvaluation.setObjectName(u"currentJobEvaluation")
        self.currentJobEvaluation.setGeometry(QRect(10, 10, 291, 821))
        self.horizontalLayoutWidget = QWidget(self.currentJobEvaluation)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 29, 271, 761))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_2 = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(85)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setDefaultSectionSize(30)

        self.horizontalLayout_3.addWidget(self.tableWidget_2)

        self.jobToEvaluate = QGroupBox(self.tab_3)
        self.jobToEvaluate.setObjectName(u"jobToEvaluate")
        self.jobToEvaluate.setGeometry(QRect(310, 10, 191, 101))
        self.gridLayout = QGridLayout(self.jobToEvaluate)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.jobToEvaluate)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.jobToEvaluate)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_6 = QLabel(self.jobToEvaluate)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.jobToEvaluate)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.newJobEvaluation = QGroupBox(self.tab_3)
        self.newJobEvaluation.setObjectName(u"newJobEvaluation")
        self.newJobEvaluation.setGeometry(QRect(310, 120, 861, 711))
        self.jobFactor = QTabWidget(self.newJobEvaluation)
        self.jobFactor.setObjectName(u"jobFactor")
        self.jobFactor.setGeometry(QRect(10, 30, 841, 651))
        self.jobFactor.setTabShape(QTabWidget.Triangular)
        self.factor1 = QWidget()
        self.factor1.setObjectName(u"factor1")
        self.tabWidget_3 = QTabWidget(self.factor1)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 0, 811, 601))
        self.tabWidget_3.setTabShape(QTabWidget.Triangular)
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.layoutWidget = QWidget(self.tab_8)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 721, 541))
        self.gridLayout_16 = QGridLayout(self.layoutWidget)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.layoutWidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.textBrowser = QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 30, 691, 201))

        self.gridLayout_16.addWidget(self.groupBox_5, 0, 0, 1, 4)

        self.lcdNumber_3 = QLCDNumber(self.layoutWidget)
        self.lcdNumber_3.setObjectName(u"lcdNumber_3")
        font1 = QFont()
        font1.setFamily(u"Noto Sans Mono CJK KR")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setItalic(True)
        font1.setWeight(50)
        self.lcdNumber_3.setFont(font1)

        self.gridLayout_16.addWidget(self.lcdNumber_3, 2, 1, 1, 1)

        self.label_15 = QLabel(self.layoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_16.addWidget(self.label_15, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.layoutWidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.listView = QListView(self.groupBox_6)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(10, 30, 691, 191))

        self.gridLayout_16.addWidget(self.groupBox_6, 1, 0, 1, 4)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_16.addWidget(self.label_5, 2, 2, 1, 1)

        self.spinBox_3 = QSpinBox(self.layoutWidget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setFont(font1)

        self.gridLayout_16.addWidget(self.spinBox_3, 2, 3, 1, 1)

        self.tabWidget_3.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.formLayoutWidget = QWidget(self.tab_9)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 851, 768))
        self.gridLayout_17 = QGridLayout(self.formLayoutWidget)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.spinBox_2 = QSpinBox(self.formLayoutWidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font1)

        self.gridLayout_17.addWidget(self.spinBox_2, 4, 3, 1, 1)

        self.lcdNumber_4 = QLCDNumber(self.formLayoutWidget)
        self.lcdNumber_4.setObjectName(u"lcdNumber_4")
        self.lcdNumber_4.setFont(font1)

        self.gridLayout_17.addWidget(self.lcdNumber_4, 4, 1, 1, 1)

        self.label_16 = QLabel(self.formLayoutWidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_17.addWidget(self.label_16, 4, 0, 1, 1)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_17.addWidget(self.label_7, 4, 2, 1, 1)

        self.textBrowser_4 = QTextBrowser(self.formLayoutWidget)
        self.textBrowser_4.setObjectName(u"textBrowser_4")

        self.gridLayout_17.addWidget(self.textBrowser_4, 3, 0, 1, 4)

        self.textBrowser_2 = QTextBrowser(self.formLayoutWidget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_17.addWidget(self.textBrowser_2, 1, 0, 1, 4)

        self.label_84 = QLabel(self.formLayoutWidget)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_84, 0, 2, 1, 1)

        self.lineEdit_16 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.gridLayout_17.addWidget(self.lineEdit_16, 0, 3, 1, 1)

        self.label_83 = QLabel(self.formLayoutWidget)
        self.label_83.setObjectName(u"label_83")

        self.gridLayout_17.addWidget(self.label_83, 2, 0, 1, 2)

        self.label_85 = QLabel(self.formLayoutWidget)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_17.addWidget(self.label_85, 2, 2, 1, 1)

        self.lineEdit_17 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.gridLayout_17.addWidget(self.lineEdit_17, 2, 3, 1, 1)

        self.label_82 = QLabel(self.formLayoutWidget)
        self.label_82.setObjectName(u"label_82")

        self.gridLayout_17.addWidget(self.label_82, 0, 0, 1, 2)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.groupBox_9 = QGroupBox(self.tab_17)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_3 = QTextBrowser(self.groupBox_9)
        self.textBrowser_3.setObjectName(u"textBrowser_3")
        self.textBrowser_3.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_10 = QGroupBox(self.tab_17)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 190, 681, 231))
        self.listView_3 = QListView(self.groupBox_10)
        self.listView_3.setObjectName(u"listView_3")
        self.listView_3.setGeometry(QRect(10, 20, 651, 192))
        self.label_17 = QLabel(self.tab_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 450, 261, 41))
        self.label_17.setFont(font1)
        self.spinBox = QSpinBox(self.tab_17)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(600, 440, 91, 51))
        self.spinBox.setFont(font1)
        self.lcdNumber_5 = QLCDNumber(self.tab_17)
        self.lcdNumber_5.setObjectName(u"lcdNumber_5")
        self.lcdNumber_5.setGeometry(QRect(270, 440, 101, 51))
        self.lcdNumber_5.setFont(font1)
        self.label_8 = QLabel(self.tab_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(380, 450, 221, 31))
        self.label_8.setFont(font1)
        self.tabWidget_3.addTab(self.tab_17, "")
        self.jobFactor.addTab(self.factor1, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_4 = QTabWidget(self.tab_4)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setGeometry(QRect(10, 0, 811, 601))
        self.tabWidget_4.setTabShape(QTabWidget.Triangular)
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.groupBox_11 = QGroupBox(self.tab_10)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_5 = QTextBrowser(self.groupBox_11)
        self.textBrowser_5.setObjectName(u"textBrowser_5")
        self.textBrowser_5.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_12 = QGroupBox(self.tab_10)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(10, 190, 681, 231))
        self.listView_5 = QListView(self.groupBox_12)
        self.listView_5.setObjectName(u"listView_5")
        self.listView_5.setGeometry(QRect(10, 20, 651, 192))
        self.label_49 = QLabel(self.tab_10)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(30, 500, 261, 41))
        self.label_49.setFont(font1)
        self.lcdNumber_9 = QLCDNumber(self.tab_10)
        self.lcdNumber_9.setObjectName(u"lcdNumber_9")
        self.lcdNumber_9.setGeometry(QRect(290, 490, 101, 51))
        self.lcdNumber_9.setFont(font1)
        self.label_50 = QLabel(self.tab_10)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(400, 500, 221, 31))
        self.label_50.setFont(font1)
        self.spinBox_11 = QSpinBox(self.tab_10)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setGeometry(QRect(620, 490, 91, 51))
        self.spinBox_11.setFont(font1)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.groupBox_13 = QGroupBox(self.tab_11)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_6 = QTextBrowser(self.groupBox_13)
        self.textBrowser_6.setObjectName(u"textBrowser_6")
        self.textBrowser_6.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_14 = QGroupBox(self.tab_11)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(10, 190, 681, 231))
        self.listView_6 = QListView(self.groupBox_14)
        self.listView_6.setObjectName(u"listView_6")
        self.listView_6.setGeometry(QRect(10, 20, 651, 192))
        self.label_51 = QLabel(self.tab_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(50, 500, 261, 41))
        self.label_51.setFont(font1)
        self.lcdNumber_10 = QLCDNumber(self.tab_11)
        self.lcdNumber_10.setObjectName(u"lcdNumber_10")
        self.lcdNumber_10.setGeometry(QRect(310, 490, 101, 51))
        self.lcdNumber_10.setFont(font1)
        self.label_52 = QLabel(self.tab_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(420, 500, 221, 31))
        self.label_52.setFont(font1)
        self.spinBox_12 = QSpinBox(self.tab_11)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setGeometry(QRect(640, 490, 91, 51))
        self.spinBox_12.setFont(font1)
        self.tabWidget_4.addTab(self.tab_11, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.groupBox_15 = QGroupBox(self.tab_16)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_7 = QTextBrowser(self.groupBox_15)
        self.textBrowser_7.setObjectName(u"textBrowser_7")
        self.textBrowser_7.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_16 = QGroupBox(self.tab_16)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(10, 190, 681, 231))
        self.listView_7 = QListView(self.groupBox_16)
        self.listView_7.setObjectName(u"listView_7")
        self.listView_7.setGeometry(QRect(10, 20, 651, 192))
        self.label_53 = QLabel(self.tab_16)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setGeometry(QRect(50, 500, 261, 41))
        self.label_53.setFont(font1)
        self.lcdNumber_11 = QLCDNumber(self.tab_16)
        self.lcdNumber_11.setObjectName(u"lcdNumber_11")
        self.lcdNumber_11.setGeometry(QRect(310, 490, 101, 51))
        self.lcdNumber_11.setFont(font1)
        self.label_54 = QLabel(self.tab_16)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setGeometry(QRect(420, 500, 221, 31))
        self.label_54.setFont(font1)
        self.spinBox_13 = QSpinBox(self.tab_16)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setGeometry(QRect(640, 490, 91, 51))
        self.spinBox_13.setFont(font1)
        self.tabWidget_4.addTab(self.tab_16, "")
        self.jobFactor.addTab(self.tab_4, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget_5 = QTabWidget(self.tab_7)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setGeometry(QRect(10, 0, 811, 601))
        self.tabWidget_5.setTabShape(QTabWidget.Triangular)
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.groupBox_17 = QGroupBox(self.tab_12)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_8 = QTextBrowser(self.groupBox_17)
        self.textBrowser_8.setObjectName(u"textBrowser_8")
        self.textBrowser_8.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_18 = QGroupBox(self.tab_12)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(10, 190, 681, 231))
        self.listView_8 = QListView(self.groupBox_18)
        self.listView_8.setObjectName(u"listView_8")
        self.listView_8.setGeometry(QRect(10, 20, 651, 192))
        self.label_55 = QLabel(self.tab_12)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setGeometry(QRect(50, 480, 261, 41))
        self.label_55.setFont(font1)
        self.lcdNumber_12 = QLCDNumber(self.tab_12)
        self.lcdNumber_12.setObjectName(u"lcdNumber_12")
        self.lcdNumber_12.setGeometry(QRect(310, 470, 101, 51))
        self.lcdNumber_12.setFont(font1)
        self.label_11 = QLabel(self.tab_12)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(420, 480, 221, 31))
        self.label_11.setFont(font1)
        self.spinBox_7 = QSpinBox(self.tab_12)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(640, 470, 91, 51))
        self.spinBox_7.setFont(font1)
        self.tabWidget_5.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.groupBox_19 = QGroupBox(self.tab_13)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_9 = QTextBrowser(self.groupBox_19)
        self.textBrowser_9.setObjectName(u"textBrowser_9")
        self.textBrowser_9.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_20 = QGroupBox(self.tab_13)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(10, 190, 681, 231))
        self.listView_9 = QListView(self.groupBox_20)
        self.listView_9.setObjectName(u"listView_9")
        self.listView_9.setGeometry(QRect(10, 20, 651, 192))
        self.label_56 = QLabel(self.tab_13)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(50, 480, 261, 41))
        self.label_56.setFont(font1)
        self.lcdNumber_13 = QLCDNumber(self.tab_13)
        self.lcdNumber_13.setObjectName(u"lcdNumber_13")
        self.lcdNumber_13.setGeometry(QRect(310, 470, 101, 51))
        self.lcdNumber_13.setFont(font1)
        self.label_12 = QLabel(self.tab_13)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(420, 480, 221, 31))
        self.label_12.setFont(font1)
        self.spinBox_8 = QSpinBox(self.tab_13)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setGeometry(QRect(640, 470, 91, 51))
        self.spinBox_8.setFont(font1)
        self.tabWidget_5.addTab(self.tab_13, "")
        self.jobFactor.addTab(self.tab_7, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget_6 = QTabWidget(self.tab_6)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setGeometry(QRect(10, 0, 811, 601))
        self.tabWidget_6.setTabShape(QTabWidget.Triangular)
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.groupBox_21 = QGroupBox(self.tab_14)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(10, 10, 671, 151))
        self.textBrowser_10 = QTextBrowser(self.groupBox_21)
        self.textBrowser_10.setObjectName(u"textBrowser_10")
        self.textBrowser_10.setGeometry(QRect(5, 30, 651, 111))
        self.groupBox_22 = QGroupBox(self.tab_14)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(10, 190, 681, 231))
        self.listView_10 = QListView(self.groupBox_22)
        self.listView_10.setObjectName(u"listView_10")
        self.listView_10.setGeometry(QRect(10, 20, 651, 192))
        self.tabWidget_6.addTab(self.tab_14, "")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.groupBox_23 = QGroupBox(self.tab_15)
        self.groupBox_23.setObjectName(u"groupBox_23")
        self.groupBox_23.setGeometry(QRect(10, 10, 671, 151))
        self.f4s2TextDescription = QTextEdit(self.groupBox_23)
        self.f4s2TextDescription.setObjectName(u"f4s2TextDescription")
        self.f4s2TextDescription.setGeometry(QRect(10, 20, 661, 121))
        self.f4s2TextDescription.setFrameShadow(QFrame.Sunken)
        self.f4s2TextDescription.setAutoFormatting(QTextEdit.AutoAll)
        self.f4s2TextDescription.setReadOnly(True)
        self.spinBox_10 = QSpinBox(self.tab_15)
        self.spinBox_10.setObjectName(u"spinBox_10")
        self.spinBox_10.setGeometry(QRect(515, 440, 91, 51))
        self.spinBox_10.setFont(font1)
        self.label_14 = QLabel(self.tab_15)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(350, 450, 161, 31))
        self.label_14.setFont(font1)
        self.groupBox_24 = QGroupBox(self.tab_15)
        self.groupBox_24.setObjectName(u"groupBox_24")
        self.groupBox_24.setGeometry(QRect(10, 190, 681, 231))
        self.textEdit_2 = QTextEdit(self.groupBox_24)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 30, 661, 191))
        self.tabWidget_6.addTab(self.tab_15, "")
        self.jobFactor.addTab(self.tab_6, "")
        self.evaluationResult = QGroupBox(self.tab_3)
        self.evaluationResult.setObjectName(u"evaluationResult")
        self.evaluationResult.setGeometry(QRect(670, 10, 481, 101))
        self.evaluationResult.setAutoFillBackground(False)
        self.evaluationResult.setFlat(False)
        self.label_2 = QLabel(self.evaluationResult)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 191, 21))
        self.lcdNumber = QLCDNumber(self.evaluationResult)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(273, 25, 91, 31))
        font2 = QFont()
        font2.setFamily(u"Noto Sans Mono CJK KR")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.lcdNumber.setFont(font2)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.label_3 = QLabel(self.evaluationResult)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 30, 81, 31))
        self.label_4 = QLabel(self.evaluationResult)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 70, 71, 31))
        self.label_4.setTextFormat(Qt.PlainText)
        self.lcdNumber_2 = QLCDNumber(self.evaluationResult)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(273, 65, 91, 31))
        font3 = QFont()
        font3.setFamily(u"Noto Sans Mono CJK KR")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setWeight(75)
        self.lcdNumber_2.setFont(font3)
        self.verticalLayoutWidget_2 = QWidget(self.tab_3)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(520, 30, 141, 85))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButtonFetchJE = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonFetchJE.setObjectName(u"pushButtonFetchJE")

        self.verticalLayout_2.addWidget(self.pushButtonFetchJE)

        self.pushButtonEvaluate = QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonEvaluate.setObjectName(u"pushButtonEvaluate")

        self.verticalLayout_2.addWidget(self.pushButtonEvaluate)

        icon3 = QIcon()
        icon3.addFile(u"3442056-head-hunting/png/019-rating.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        icon4 = QIcon()
        icon4.addFile(u"3442056-head-hunting/png/050-performance.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_5, icon4, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        icon5 = QIcon()
        icon5.addFile(u"3190606-finance/png/044-bar chart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_18, icon5, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(2)
        self.pushButton_8.setDefault(False)
        self.jobFactor.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(2)
        self.tabWidget_5.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Pay Equity Programe Creator", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"Job Title", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"111", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nouvelle colonne", None));
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Add A New Job ", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save job Selection", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Delete Selected Job", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"Pay Equity Program Information", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"Total Compensation", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Pay Equity Results", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Individual Method With Grades", None))
        self.spinBox_4.setSuffix("")
        self.spinBox_4.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.spinBox_5.setSuffix("")
        self.spinBox_5.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Individual Method With Points</p></body></html>", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Global Method With Pairs", None))
        self.spinBox_6.setSuffix("")
        self.spinBox_6.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.groupBox_31.setTitle("")
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Save Pay Equity Program", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Export Pay Equity program as PDF", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Load Existing Program", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Create New Program", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_21), QCoreApplication.translate("MainWindow", u"Pay Equity Program", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Pay Scale Group", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Pay Scale Name", None))
        self.pushButtonFetchPayScale.setText(QCoreApplication.translate("MainWindow", u"Fetch Pay Scale", None))
        self.pushButtonSavePayScale.setText(QCoreApplication.translate("MainWindow", u"Save Pay Scale", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Pay Scale ID", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Effective Date From", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Minimum Wage", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Standard Wage", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Maximum Wage", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Grade 1", None))
        self.doubleSpinBox.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox.setSuffix("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Grade 2", None))
        self.doubleSpinBox_4.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Grade 3", None))
        self.doubleSpinBox_7.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Grade 4", None))
        self.doubleSpinBox_11.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Grade 5", None))
        self.doubleSpinBox_13.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Grade 6", None))
        self.doubleSpinBox_2.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Grade 7", None))
        self.doubleSpinBox_5.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Grade 8", None))
        self.doubleSpinBox_8.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Grade 9", None))
        self.doubleSpinBox_10.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Grade 10", None))
        self.doubleSpinBox_14.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Grade 11", None))
        self.doubleSpinBox_16.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Grade 12", None))
        self.doubleSpinBox_17.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_26.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Grade 13", None))
        self.doubleSpinBox_18.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_27.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Grade 14", None))
        self.doubleSpinBox_19.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_28.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Grade 15", None))
        self.doubleSpinBox_20.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_29.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Grade 16", None))
        self.doubleSpinBox_21.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_30.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Grade 17", None))
        self.doubleSpinBox_22.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_31.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Grade 18", None))
        self.doubleSpinBox_23.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_32.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Grade 19", None))
        self.doubleSpinBox_24.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_33.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Grade 20", None))
        self.doubleSpinBox_25.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.doubleSpinBox_34.setPrefix(QCoreApplication.translate("MainWindow", u"$", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Minimum Wage by Province", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Alberta", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Manitoba", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"P-E-I", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"New-Brunswick", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"2021 Estimate", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Quebec", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"2020", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Year", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"British-Columbia", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Saskatchewan", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Ontario", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Nova-Scotia", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Newfoundland", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"Pay Scale Designer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Pay Scale Group", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"Responsabilities", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Please insert a short description of the responsabilities ", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Responsabilities ID", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Qualifications", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Please insert a short description of the required qualification", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"Working Conditions", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Please insert a short description of the working conditions", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Job Information", None))
        self.isUnionisable.setText(QCoreApplication.translate("MainWindow", u"Job Is Unionisable", None))
        self.pushButtonCreateJobDescription.setText(QCoreApplication.translate("MainWindow", u"Create Job Description", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Business Unit", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"First-level Manager", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Job Level", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Job Level Code", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Job Title", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Pay Scale ID", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Function Unit", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Job ID", None))
        self.pushButtonFetchJobDescription.setText(QCoreApplication.translate("MainWindow", u"Fetch Job Description", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Job Description", None))
        self.currentJobEvaluation.setTitle(QCoreApplication.translate("MainWindow", u"Current Jobs List", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Job title", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Job ID", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Evaluation ID", None));
        self.jobToEvaluate.setTitle(QCoreApplication.translate("MainWindow", u"Job Group to Evaluate", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Job ID : ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Job Evaluation ID", None))
        self.newJobEvaluation.setTitle(QCoreApplication.translate("MainWindow", u"New Job Evaluation", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Knowledge and Education", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Factor Description ID", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Factor level", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Factor level ID", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Skills and Qualifications", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"Experience", None))
        self.jobFactor.setTabText(self.jobFactor.indexOf(self.factor1), QCoreApplication.translate("MainWindow", u"Skills and Qualifications", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Financial Accountability", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"HR Responsabilities", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Communication", None))
        self.jobFactor.setTabText(self.jobFactor.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Responsabilities", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Physical Efforts", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Current Factor Level : ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"New Factor Level : ", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Intellectual Efforts", None))
        self.jobFactor.setTabText(self.jobFactor.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Efforts", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Physical Environnement", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.f4s2TextDescription.setDocumentTitle("")
        self.f4s2TextDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Factor Description", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Factor Level", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"Level Description", None))
        self.textEdit_2.setDocumentTitle(QCoreApplication.translate("MainWindow", u"texte", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Psychological and Social Environnement", None))
        self.jobFactor.setTabText(self.jobFactor.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Work Environnement", None))
        self.evaluationResult.setTitle(QCoreApplication.translate("MainWindow", u"Job Evaluation Result", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Job Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Points : ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Job Level : ", None))
        self.pushButtonFetchJE.setText(QCoreApplication.translate("MainWindow", u"Fetch Job\n"
"Evaluation", None))
        self.pushButtonEvaluate.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Job Evaluation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Factors, Points and Weighting", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Benchmarking and Compensation Analysis", None))
    # retranslateUi


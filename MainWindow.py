# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from custommenu import CustomMenu
import Icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(979, 604)
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"*{\n"
"	background:rgb(255,255,255);\n"
"}\n"
"QGroupBox\n"
"{\n"
"	font-family:Century Gothic, sans-serif;\n"
"}\n"
"QLabel\n"
"{\n"
"	font-family:Century Gothic, sans-serif;\n"
"	font-size:12px;\n"
"}\n"
"QComboBox\n"
"{\n"
"	background:rgb(252,252,252);\n"
"	border-radius:4px;\n"
"	border: 1px solid #717072;\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"	background-color:rgb(204,232,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"QListWidget\n"
"{\n"
"	font-size:12px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	border: 1px solid #717072;\n"
"	border-radius: 4px;\n"
"}\n"
"QListWidget::item\n"
"{\n"
"	border-bottom: 1px solid black;\n"
"	padding-top: 5%;\n"
"    padding-bottom: 5%;\n"
"}\n"
"QListWidget::item:selected\n"
"{\n"
"	background-color:rgb(0,133,252);\n"
"	color:rgb(255,255,255);\n"
"}\n"
"QMenu::item:selected\n"
"{\n"
"	background-color:rgb(204,232,255);\n"
"	color:rgb(0,0,0);\n"
"}\n"
"#startPushButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Cen"
                        "tury Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#startPushButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#startPushButton:disabled\n"
"{\n"
"	background:rgb(143,188,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Generator = QWidget()
        self.Generator.setObjectName(u"Generator")
        self.gridLayout_5 = QGridLayout(self.Generator)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox = QGroupBox(self.Generator)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(200, 16777215))
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.backendsComboBox = QComboBox(self.groupBox)
        self.backendsComboBox.addItem("")
        self.backendsComboBox.addItem("")
        self.backendsComboBox.setObjectName(u"backendsComboBox")

        self.verticalLayout.addWidget(self.backendsComboBox)

        self.backendsListWidget = QListWidget(self.groupBox)
        self.backendsListWidget.setObjectName(u"backendsListWidget")

        self.verticalLayout.addWidget(self.backendsListWidget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_8.addWidget(self.groupBox)

        self.resultListView = QListView(self.Generator)
        self.resultListView.setObjectName(u"resultListView")

        self.horizontalLayout_8.addWidget(self.resultListView)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.Generator)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.shotsLabel = QLabel(self.groupBox_2)
        self.shotsLabel.setObjectName(u"shotsLabel")
        self.shotsLabel.setMinimumSize(QSize(121, 0))

        self.horizontalLayout_5.addWidget(self.shotsLabel)

        self.shotsSpinBox = QSpinBox(self.groupBox_2)
        self.shotsSpinBox.setObjectName(u"shotsSpinBox")
        self.shotsSpinBox.setMinimum(1)
        self.shotsSpinBox.setMaximum(99999)
        self.shotsSpinBox.setValue(20000)

        self.horizontalLayout_5.addWidget(self.shotsSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.qbitsLabel = QLabel(self.groupBox_2)
        self.qbitsLabel.setObjectName(u"qbitsLabel")
        self.qbitsLabel.setMinimumSize(QSize(121, 0))

        self.horizontalLayout_6.addWidget(self.qbitsLabel)

        self.qbitsSpinBox = QSpinBox(self.groupBox_2)
        self.qbitsSpinBox.setObjectName(u"qbitsSpinBox")
        self.qbitsSpinBox.setMinimum(1)
        self.qbitsSpinBox.setMaximum(9999)

        self.horizontalLayout_6.addWidget(self.qbitsSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.threadsLabel = QLabel(self.groupBox_2)
        self.threadsLabel.setObjectName(u"threadsLabel")
        self.threadsLabel.setMinimumSize(QSize(121, 0))
        self.threadsLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_7.addWidget(self.threadsLabel)

        self.threadsSpinBox = QSpinBox(self.groupBox_2)
        self.threadsSpinBox.setObjectName(u"threadsSpinBox")
        self.threadsSpinBox.setMinimum(1)
        self.threadsSpinBox.setMaximum(999)

        self.horizontalLayout_7.addWidget(self.threadsSpinBox)


        self.verticalLayout_3.addLayout(self.horizontalLayout_7)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.Generator)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_2 = QGridLayout(self.groupBox_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.systemLabel = QLabel(self.groupBox_3)
        self.systemLabel.setObjectName(u"systemLabel")
        self.systemLabel.setMinimumSize(QSize(92, 0))
        self.systemLabel.setMaximumSize(QSize(92, 16777215))

        self.horizontalLayout.addWidget(self.systemLabel)

        self.systemLabelValue = QLabel(self.groupBox_3)
        self.systemLabelValue.setObjectName(u"systemLabelValue")

        self.horizontalLayout.addWidget(self.systemLabelValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.queueLabel = QLabel(self.groupBox_3)
        self.queueLabel.setObjectName(u"queueLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.queueLabel.sizePolicy().hasHeightForWidth())
        self.queueLabel.setSizePolicy(sizePolicy)
        self.queueLabel.setMinimumSize(QSize(92, 0))
        self.queueLabel.setMaximumSize(QSize(92, 16777215))

        self.horizontalLayout_2.addWidget(self.queueLabel)

        self.queueLabelValue = QLabel(self.groupBox_3)
        self.queueLabelValue.setObjectName(u"queueLabelValue")

        self.horizontalLayout_2.addWidget(self.queueLabelValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.shotsLabelStatus = QLabel(self.groupBox_3)
        self.shotsLabelStatus.setObjectName(u"shotsLabelStatus")
        sizePolicy.setHeightForWidth(self.shotsLabelStatus.sizePolicy().hasHeightForWidth())
        self.shotsLabelStatus.setSizePolicy(sizePolicy)
        self.shotsLabelStatus.setMinimumSize(QSize(92, 0))
        self.shotsLabelStatus.setMaximumSize(QSize(92, 16777215))

        self.horizontalLayout_3.addWidget(self.shotsLabelStatus)

        self.shotsLabelStatusValue = QLabel(self.groupBox_3)
        self.shotsLabelStatusValue.setObjectName(u"shotsLabelStatusValue")

        self.horizontalLayout_3.addWidget(self.shotsLabelStatusValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.qbitsLabelStatus = QLabel(self.groupBox_3)
        self.qbitsLabelStatus.setObjectName(u"qbitsLabelStatus")
        self.qbitsLabelStatus.setMinimumSize(QSize(92, 0))
        self.qbitsLabelStatus.setMaximumSize(QSize(92, 16777215))

        self.horizontalLayout_4.addWidget(self.qbitsLabelStatus)

        self.qbitsLabelStatusValue = QLabel(self.groupBox_3)
        self.qbitsLabelStatusValue.setObjectName(u"qbitsLabelStatusValue")

        self.horizontalLayout_4.addWidget(self.qbitsLabelStatusValue)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.groupBox_3)

        self.startPushButton = QPushButton(self.Generator)
        self.startPushButton.setObjectName(u"startPushButton")
        self.startPushButton.setMinimumSize(QSize(0, 30))

        self.verticalLayout_4.addWidget(self.startPushButton)


        self.horizontalLayout_8.addLayout(self.verticalLayout_4)


        self.gridLayout_5.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Generator, "")
        self.Statistics = QWidget()
        self.Statistics.setObjectName(u"Statistics")
        self.tabWidget.addTab(self.Statistics, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 979, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = CustomMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"IBMqRNG", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Backends", None))
        self.backendsComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Cloud backends", None))
        self.backendsComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Local backends", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.shotsLabel.setText(QCoreApplication.translate("MainWindow", u"Number of shots:", None))
        self.qbitsLabel.setText(QCoreApplication.translate("MainWindow", u"Number of qbits:", None))
        self.threadsLabel.setText(QCoreApplication.translate("MainWindow", u"Number of threads:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Status", None))
        self.systemLabel.setText(QCoreApplication.translate("MainWindow", u"System status:", None))
        self.systemLabelValue.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.queueLabel.setText(QCoreApplication.translate("MainWindow", u"Queue position:", None))
        self.queueLabelValue.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.shotsLabelStatus.setText(QCoreApplication.translate("MainWindow", u"Number of shots:", None))
        self.shotsLabelStatusValue.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.qbitsLabelStatus.setText(QCoreApplication.translate("MainWindow", u"Number of qbits:", None))
        self.qbitsLabelStatusValue.setText(QCoreApplication.translate("MainWindow", u"Waiting...", None))
        self.startPushButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Generator), QCoreApplication.translate("MainWindow", u"Generator", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Statistics), QCoreApplication.translate("MainWindow", u"Statistics", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi


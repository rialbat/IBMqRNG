# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)
import Icon_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(253, 105)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(253, 105))
        Dialog.setMaximumSize(QSize(253, 105))
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"*{\n"
"	background:rgb(255,255,255);\n"
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
"#canclePushButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#canclePushButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#canclePushButton:disabled\n"
"{\n"
"	background:rgb(143,188,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#generatePushButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#generatePus"
                        "hButton:pressed\n"
"{\n"
"	background:rgb(0,122,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"#generatePushButton:disabled\n"
"{\n"
"	background:rgb(143,188,228);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bitLabel = QLabel(Dialog)
        self.bitLabel.setObjectName(u"bitLabel")
        self.bitLabel.setMinimumSize(QSize(121, 0))

        self.horizontalLayout_5.addWidget(self.bitLabel)

        self.bitSpinBox = QSpinBox(Dialog)
        self.bitSpinBox.setObjectName(u"bitSpinBox")
        self.bitSpinBox.setMinimum(1)
        self.bitSpinBox.setMaximum(1024)
        self.bitSpinBox.setValue(32)

        self.horizontalLayout_5.addWidget(self.bitSpinBox)


        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.generatePushButton = QPushButton(Dialog)
        self.generatePushButton.setObjectName(u"generatePushButton")
        self.generatePushButton.setEnabled(True)
        self.generatePushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.generatePushButton)

        self.canclePushButton = QPushButton(Dialog)
        self.canclePushButton.setObjectName(u"canclePushButton")
        self.canclePushButton.setEnabled(True)
        self.canclePushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.canclePushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.canclePushButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Generate numbers", None))
        self.bitLabel.setText(QCoreApplication.translate("Dialog", u"Bit depth:", None))
        self.generatePushButton.setText(QCoreApplication.translate("Dialog", u"Generate", None))
        self.canclePushButton.setText(QCoreApplication.translate("Dialog", u"Cancle", None))
    # retranslateUi


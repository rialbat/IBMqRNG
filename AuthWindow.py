# -*- coding: utf-8 -*-


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)
import Icon_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(305, 120)
        Dialog.setMinimumSize(QSize(305, 120))
        Dialog.setMaximumSize(QSize(305, 120))
        icon = QIcon()
        icon.addFile(u":/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"QPushButton\n"
"{\n"
"	background:rgb(0,133,252);\n"
"	border-radius:4px;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	color:rgb(255,255,255);\n"
"}\n"
"*{\n"
"	background:rgb(255,255,255);\n"
"}\n"
"#welcomeLabel\n"
"{\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"	text-align: center;\n"
"	vertical-align: middle;\n"
"}\n"
"QLineEdit\n"
"{\n"
"	background:rgb(245,245,245);\n"
"	border-radius:4px;\n"
"	border: 1px solid #717072;\n"
"}\n"
"QToolButton\n"
"{\n"
"	border-radius: 4px;\n"
"	border: 1px solid #717072;\n"
"	font-size:15px;\n"
"	font-family:Century Gothic, sans-serif;\n"
"}")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.welcomeLabel = QLabel(Dialog)
        self.welcomeLabel.setObjectName(u"welcomeLabel")
        self.welcomeLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.welcomeLabel)

        self.keyLineEdit = QLineEdit(Dialog)
        self.keyLineEdit.setObjectName(u"keyLineEdit")
        self.keyLineEdit.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.keyLineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loginPushButton = QPushButton(Dialog)
        self.loginPushButton.setObjectName(u"loginPushButton")
        self.loginPushButton.setMinimumSize(QSize(0, 31))
        self.loginPushButton.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout.addWidget(self.loginPushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelPushButton = QPushButton(Dialog)
        self.cancelPushButton.setObjectName(u"cancelPushButton")
        self.cancelPushButton.setMinimumSize(QSize(0, 31))
        self.cancelPushButton.setMaximumSize(QSize(16777215, 31))

        self.horizontalLayout.addWidget(self.cancelPushButton)

        self.questionToolButton = QToolButton(Dialog)
        self.questionToolButton.setObjectName(u"questionToolButton")
        self.questionToolButton.setMinimumSize(QSize(31, 31))
        self.questionToolButton.setMaximumSize(QSize(31, 31))

        self.horizontalLayout.addWidget(self.questionToolButton)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)


        self.retranslateUi(Dialog)
        self.cancelPushButton.clicked.connect(Dialog.close)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Authorization", None))
        self.welcomeLabel.setText(QCoreApplication.translate("Dialog", u"Enter your IBMQ API key", None))
        self.keyLineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u" API key", None))
        self.loginPushButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.cancelPushButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.questionToolButton.setText(QCoreApplication.translate("Dialog", u"?", None))
    # retranslateUi


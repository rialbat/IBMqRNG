# IBM
import ibmapi

# System
import sys
import os.path

# RegEx
import re

# GUI
from PySide6 import QtWidgets, QtCore, QtGui
import MainWindow
import AuthWindow

programVersion = '0.1'


class AuthUI(QtWidgets.QDialog, AuthWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.login)

        self._credsFile = open(os.path.join(os.path.expanduser("~"),
                                            '.qiskit', 'qiskitrc'), "r")
        self._token = ""
        self._successLogin = False

        self.keyLineEdit.setText(self.loadCreds(self._credsFile.read()))

    def login(self):
        IBManswer = ibmapi.IBMQLogin(self.keyLineEdit.text())
        self._token = self.keyLineEdit.text()
        if IBManswer == 1:
            self._successLogin = True
            self.close()
        elif IBManswer == -1:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "Key can't be empty!")
        elif IBManswer == -2:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "This service isn't available in your country!")
        elif IBManswer == -3:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "No internet connection!")
        elif IBManswer == -4:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "Login failed!")
        elif IBManswer == -5:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "Unknown error!")

    def loadCreds(self, token):
        regExPattern = 'token = (.*?)\n'
        finalMatch = ''
        matches = re.finditer(regExPattern, token, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                if match.group(groupNum) is not None:
                    finalMatch = finalMatch + match.group(groupNum)
        return finalMatch

    @property
    def successLogin(self):
        return self._successLogin


class ProgrammUI(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuAbout.customTriggeredSignal.connect(self.aboutMessage)
        self.backendsComboBox.currentIndexChanged.connect(self.updateServers)
        # self.startButton.clicked.connect(self.startAsyncSerch)
        # self._model = QtGui.QStandardItemModel()
        # self.tableInit()

        self._shots = 20000
        self._qbits = 1
        self._threads = 1

        self.updateServers()

    def aboutMessage(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    str("The program was created by rialbat\nVersion: %s\nMIT License" % programVersion))

    def updateServers(self):
        if(self.backendsComboBox.)

def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthUI()
    if auth_window.exec() and not auth_window.successLogin:
        pass
    if auth_window.successLogin:
        window = ProgrammUI()
        window.show()
        app.exec()


if __name__ == '__main__':
    main()

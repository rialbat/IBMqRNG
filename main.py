# IBM
import ibmapi

# System
import sys

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

        self._token = ""



    def login(self):
        IBManswer = ibmapi.IBMQLogin(self.keyLineEdit.text())

        if IBManswer == 1:
            pass
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



    def successLogin(self):
        self.close()
    # Request to the IBM server then check answer (try, catch)


class ProgrammUI(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuAbout.customTriggeredSignal.connect(self.aboutMessage)
        # self.startButton.clicked.connect(self.startAsyncSerch)
        # self._model = QtGui.QStandardItemModel()
        # self.tableInit()

        self._shots = 20000
        self._qbits = 1
        self._threads = 1

        # self._serverResponseList = []

    def aboutMessage(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    str("The program was created by rialbat\nVersion: %s\nMIT License" % programVersion))


def main():
    app = QtWidgets.QApplication(sys.argv)
    auth_window = AuthUI()
    if(auth_window.exec()):
        pass
    else:
        window = ProgrammUI()
        window.show()
        app.exec()


if __name__ == '__main__':
    main()

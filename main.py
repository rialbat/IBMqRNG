# IBM
import ibmapi

# GUI
from PySide6 import QtWidgets, QtCore, QtGui
import MainWindow

programVersion = '0.1'


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ProgrammUI()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

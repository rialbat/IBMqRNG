# IBM
import ibmapi
from qiskit import result

# System
import sys
import os.path
import math

# RegEx
import re

# GUI
from PySide6 import QtWidgets, QtCore, QtGui
import MainWindow
import AuthWindow

# Plot
from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlibwidget import MatplotlibWidget

# BitMap
from bitmapwidget import BitMapWidget

# For Multithreading
from worker import Worker

programVersion = '1.1'


class AuthUI(QtWidgets.QDialog, AuthWindow.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loginPushButton.clicked.connect(self.login)
        self.questionToolButton.clicked.connect(self.helpDialog)

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

    def helpDialog(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    str("The program was created by Rialbat\nVersion: %s\nMIT License" % programVersion))

    @property
    def successLogin(self):
        return self._successLogin


class ProgrammUI(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menuAbout.customTriggeredSignal.connect(self.aboutMessage)
        self.backendsComboBox.currentIndexChanged.connect(self.updateServers)
        self.shotsSpinBox.valueChanged.connect(self.updateShotsStatus)
        self.threadsSpinBox.valueChanged.connect(self.updateThreadsStatus)
        self.qbitsSpinBox.valueChanged.connect(self.updateQbitsStatus)
        self.clearPushButton.clicked.connect(self.clearResult)
        self.startPushButton.clicked.connect(self.startAsync)
        self.distribPushButton.clicked.connect(self.showHist)
        self.externalDistribPushButton.clicked.connect(self.showHistExternal)
        self.bitmapPushButton.clicked.connect(self.showBitMap)
        self.frequencyPushButton.clicked.connect(self.checkFreq)
        self.resultsCheckBox.stateChanged.connect(self.checkBoxStatus)
        self.actionSave_result.triggered.connect(self.saveToFile)
        self.backendsListWidget.itemSelectionChanged.connect(self.selectBackend)
        self._model = QtGui.QStandardItemModel()
        self._modelFreq = QtGui.QStandardItemModel()
        self.tableInit()

        self._threadPool = QtCore.QThreadPool()

        self._shots = 20000
        self._qbits = 1
        self._maxQbits = 1
        self._threads = 1
        self._backend = ""
        self._showResults = False
        self._currentJob = 0
        self._cloudServers = ibmapi.getCloudServers()
        self._localServers = ibmapi.getLocalServers()
        self.shotsLabelStatusValue.setText(str(self.shotsSpinBox.value()))
        self.threadsLabelStatusValue.setText(str(self.threadsSpinBox.value()))
        self.qbitsLabelStatusValue.setText("1/1")
        self.jobsLabelStatusValue.setText("0/1")

        self.plotExist = False
        self.canvasExist = False
        self.layoutVerticalPlot = QtWidgets.QVBoxLayout(self.plotWidget)
        self.layoutVerticalCanvas = QtWidgets.QVBoxLayout(self.canvasWidget)

        self.updateServers()

        self._resultsList = []

    @QtCore.Slot(result.result.Result)
    def receiveResponse(self, serverResponse):
        self._resultsList.append(serverResponse)
        self.updateJobsStatus()
        if self._showResults:
            self.fillTable()
        self.enGUIEl()

    def updateJobsStatus(self):
        self._currentJob = self._currentJob + 1
        self.jobsLabelStatusValue.setText(str(self._currentJob) + "/" + str(self._threads))
        if self._currentJob == self._threads:
            QtWidgets.QMessageBox.information(self, "Jobs' update",
                                              "All jobs completed!")
            self.jobsLabelStatusValue.setText("0/" + str(self._threads))

    def initPlotWidget(self):
        if not self.plotExist:
            self.matplotWidget = MatplotlibWidget()
            self.layoutVerticalPlot.addWidget(self.matplotWidget)
            self.plotExist = True

    def initBitMapWidget(self):
        if not self.canvasExist:
            self.bitMapWidget = BitMapWidget(self._resultsList[-1].get_memory())
            self.layoutVerticalCanvas.addWidget(self.bitMapWidget)
            self.canvasExist = True

    def checkFreq(self):
        if self._qbits > 10:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "10 qbits max!")
        else:
            self.freqTable()

    def tableInit(self):
        headersLabels = ["Q0"]

        self._model.setHorizontalHeaderLabels(headersLabels)
        self.resultTableView.setModel(self._model)

    def checkBoxStatus(self):
        self._showResults = True if self.resultsCheckBox.checkState() == QtCore.Qt.CheckState.Checked else False

    def fillTable(self):
        self._model.removeRows(0, self._model.rowCount())
        posY = -1
        for i in self._resultsList:
            for j in i.get_memory():
                posX = 0
                posY = posY + 1
                for s in j:
                    itemQ = QtGui.QStandardItem(str(s))
                    itemQ.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
                    self._model.setItem(posY, posX, itemQ)
                    posX = posX + 1

    def clearResult(self):
        self._resultsList.clear()
        self._model.setRowCount(0)
        self._modelFreq.setRowCount(0)

        self.clearPushButton.setEnabled(False)
        self.distribPushButton.setEnabled(False)
        self.externalDistribPushButton.setEnabled(False)
        self.bitmapPushButton.setEnabled(False)
        self.frequencyPushButton.setEnabled(False)


    def saveToFile(self):
        savePath = QtWidgets.QFileDialog.getSaveFileName(
            self, 'Save File', '', 'TXT(*.txt)')
        saveFile = QtCore.QFile(savePath[0])

        if savePath[0]:
            if saveFile.open(QtCore.QFile.WriteOnly | QtCore.QFile.Truncate):
                result = QtCore.QTextStream(saveFile)
                for i in self._resultsList:
                    for j in i.get_memory():
                        for z in j:
                            result << str(z)

            QtWidgets.QMessageBox.information(self, "Save result",
                                              "Success!")

    def aboutMessage(self):
        QtWidgets.QMessageBox.about(self, "About",
                                    str("The program was created by Rialbat\nVersion: %s\nMIT License" % programVersion))

    def updateServers(self):
        self.backendsListWidget.clear()
        if(self.backendsComboBox.currentIndex() == 0):
            ibmapi.updateProvider(0)
            for i in self._cloudServers:
                self.backendsListWidget.addItem(str(i))
        else:
            ibmapi.updateProvider(1)
            for i in self._localServers:
                self.backendsListWidget.addItem(str(i))

    def updateShotsStatus(self):
        self.shotsLabelStatusValue.setText(str(self.shotsSpinBox.value()))
        self._shots = self.shotsSpinBox.value()

    def updateThreadsStatus(self):
        self.threadsLabelStatusValue.setText(str(self.threadsSpinBox.value()))
        self._threads = self.threadsSpinBox.value()
        self.jobsLabelStatusValue.setText("0/" + str(self._threads))

    def updateQbitsStatus(self):
        self.qbitsLabelStatusValue.setText(str(self.qbitsSpinBox.value()) + "/" + str(self._maxQbits))
        self._qbits = self.qbitsSpinBox.value()

        self._model.setRowCount(0)
        self._model.clear()
        headersLabels = [f"Q{x}" for x in range(self._qbits)]
        self._model.setHorizontalHeaderLabels(headersLabels)

    def disGUIEl(self):
        self.shotsSpinBox.setEnabled(False)
        self.threadsSpinBox.setEnabled(False)
        self.qbitsSpinBox.setEnabled(False)
        self.startPushButton.setEnabled(False)
        self.clearPushButton.setEnabled(False)
        self.distribPushButton.setEnabled(False)
        self.externalDistribPushButton.setEnabled(False)
        self.bitmapPushButton.setEnabled(False)
        self.frequencyPushButton.setEnabled(False)

    def enGUIEl(self):
        self.shotsSpinBox.setEnabled(True)
        self.threadsSpinBox.setEnabled(True)
        self.qbitsSpinBox.setEnabled(True)
        self.startPushButton.setEnabled(True)
        self.clearPushButton.setEnabled(True)
        self.distribPushButton.setEnabled(True)
        self.externalDistribPushButton.setEnabled(True)
        self.bitmapPushButton.setEnabled(True)
        self.frequencyPushButton.setEnabled(True)

    def startAsync(self):
        self._currentJob = 0
        self.disGUIEl()
        self._threadPool.setMaxThreadCount(self._threads)

        for thread in range(self._threads):
            lWorker = Worker(self._qbits, self._backend, self._shots)
            lWorker.signals.result.connect(self.receiveResponse)
            self._threadPool.start(lWorker)

    def selectBackend(self):
        self._backend = self.backendsListWidget.currentItem().text()
        self._maxQbits = ibmapi.getServerQbits(self._backend)
        self.qbitsSpinBox.setMaximum(self._maxQbits)
        self.updateQbitsStatus()
        self.startPushButton.setEnabled(True)

        if self.backendsComboBox.currentIndex() == 1:
            self.queueLabelValue.setText("0")
            self.systemLabelValue.setText("active")
        else:
            self.updateStatus(self._backend)

    def updateStatus(self, backsys):
        self.systemLabelValue.setText(ibmapi.getServerStatus(backsys))
        self.queueLabelValue.setText(str(ibmapi.getPendingJobs(backsys)))

    def freqTable(self):
        self._modelFreq.setRowCount(0)

        headerSeq = [i for i in range(int(math.pow(2, self._qbits)))]
        headersLabels = [bin(headerSeq[i])[2:].zfill(self._qbits) for i in range(len(headerSeq))]
        countDic = self._resultsList[-1].get_counts()

        self._modelFreq.setVerticalHeaderLabels(headersLabels)
        self._modelFreq.setHorizontalHeaderLabels(["Counts"])
        self.statTableView.setModel(self._modelFreq)
        for i in range(len(headerSeq)):
            itemQ = QtGui.QStandardItem(str(countDic[headersLabels[i]]))
            itemQ.setTextAlignment(QtCore.Qt.AlignCenter)  # type: ignore
            self._modelFreq.setItem(i, 0, itemQ)

    def showHist(self):
        if self._qbits > 10:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "10 qbits max!")
        else:
            self.initPlotWidget()
            self.tabWidget_2.setCurrentIndex(0)

            dictionary = self._resultsList[-1].get_counts()
            dictionarySum = sum(dictionary.values())
            dictionaryPercent = dictionary

            for i in dictionary:
                dictionaryPercent[i] = dictionary[i] / dictionarySum * 100
            labels = list(dictionaryPercent.keys())
            formatter = FuncFormatter(lambda y, pos: "%1.1f%%" % (y))
            self.matplotWidget.ax.yaxis.set_major_formatter(formatter)
            self.matplotWidget.ax.bar(labels, dictionary.values(), color='g')
            self.matplotWidget.ax.set_title("Frequency distribution")
            for tick in self.matplotWidget.ax.get_xticklabels():
                tick.set_rotation(45)
            self.matplotWidget.canvas.draw()

    def showHistExternal(self):
        if self._qbits > 10:
            QtWidgets.QMessageBox.warning(self, "Error",
                                          "10 qbits max!")
        else:
            dictionary = self._resultsList[-1].get_counts()
            dictionarySum = sum(dictionary.values())
            dictionaryPercent = dictionary

            for i in dictionary:
                dictionaryPercent[i] = dictionary[i]/dictionarySum * 100
            labels = list(dictionaryPercent.keys())
            formatter = FuncFormatter(lambda y, pos: "%1.1f%%" % (y))
            fig, ax = plt.subplots(num='Distribution')
            ax.yaxis.set_major_formatter(formatter)
            plt.bar(labels, dictionary.values(), color='g')
            plt.title("Frequency distribution")
            plt.xticks(rotation=45)
            plt.show()

    def showBitMap(self):
        self.initBitMapWidget()
        self.tabWidget_2.setCurrentIndex(1)


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

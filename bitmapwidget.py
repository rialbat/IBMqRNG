import math

from PySide6 import QtGui, QtCore, QtWidgets

class BitMapWidget(QtWidgets.QWidget):
    def __init__(self, bitSeq):
        self.localSeq = bitSeq
        self.resultSeq = []
        self.sizeSeq = 0
        self.getBitSeq()
        super().__init__()


    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setPen(QtCore.Qt.black)

        for y in range(self.sizeSeq):
            for x in range(self.sizeSeq):
                rnd = self.resultSeq[y * self.sizeSeq + x]
                if rnd == "1":
                    qp.drawPoint(x + 20, y + 20)

        qp.end()

    def getBitSeq(self):
        for i in self.localSeq:
            for j in i:
                self.resultSeq.append(j)
        self.sizeSeq = int(math.sqrt(len(self.resultSeq)))
from PySide6 import QtCore
from qiskit import result
import ibmapi

class WorkerSignals(QtCore.QObject):
    result = QtCore.Signal(result.result.Result)

class Worker(QtCore.QRunnable):
    def __init__(self, qbits = 1, backend = "", shots=20000):
        super(Worker, self).__init__()
        self._qbits = qbits
        self._backend = backend
        self._shots = shots

        self.signals = WorkerSignals()

    @QtCore.Slot()
    def run(self):
        lResult = ibmapi.createRequest(self._qbits, self._backend, self._shots)
        self.signals.result.emit(lResult)
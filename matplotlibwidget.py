from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout

__all__ = ['MatplotlibWidget']


class MatplotlibWidget(QWidget):
    def __init__(self, parent=None):
        super(MatplotlibWidget, self).__init__(parent)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.ax = self.figure.add_subplot(111)

        self.layoutVertical = QVBoxLayout(self)
        self.layoutVertical.addWidget(self.canvas)
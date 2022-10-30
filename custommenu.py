from PySide6.QtWidgets import QMenu
from PySide6.QtCore import Signal

class CustomMenu(QMenu):

    def __init__(self, parent=None):
        super(CustomMenu, self).__init__(parent)

    customTriggeredSignal = Signal()


    def mouseReleaseEvent(self, event):
        act = super().menuAction()

        if act:
            super().mouseReleaseEvent(event)
            self.customTriggeredSignal.emit()
        else:
            super().mouseReleaseEvent(event)

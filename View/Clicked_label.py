from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ClickLabel(QLabel):
    clicked = pyqtSignal()
    # double_clicked = pyqtSignal()

    x = 0
    y = 0

    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QLabel.mousePressEvent(self, QMouseEvent)

    # def mouseDoubleClickEvent(self, *args, **kwargs):
    #     self.double_clicked.emit()
    #     QLabel.mouseDoubleClickEvent(self, QMouseEvent)




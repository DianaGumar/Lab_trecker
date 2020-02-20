from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ClickLabel(QLabel):
    clicked = pyqtSignal()

    x = 0
    y = 0

    color = []
    color_font = "white"

    def __init__(self, *args):
        QLabel.__init__(self, *args)


    def mousePressEvent(self, QMouseEvent):
        self.clicked.emit()
        QLabel.mousePressEvent(self, QMouseEvent)





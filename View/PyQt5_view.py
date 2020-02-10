import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import date
from Table import Table
from Objects import Subject
from View.Clicked_label import ClickLabel


class PyQt5_view(QWidget):
    def __init__(self, parent=None):
        super(PyQt5_view, self).__init__(parent)
        # self.setStyleSheet("background-color: "+ self.colors[3])
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(780, 400, 550, 250)
        self.setWindowTitle("Lab trecker")
        self.setWindowOpacity(0.8)
        # self.setWindowIcon(QIcon('img/logo.png'))
        self.init_ui()


    def init_ui(self):
        self.table = Table()
        self.subject_names, self.max_lab_count, self.lab_maiking = self.table.Make_table()

        self.labels = [self.subject_names.__len__() + self.max_lab_count]

        self.ctrl_press = False
        self.prosent_add_maiking = 10
        self.square_id = 0
        self.x = 30
        self.y = 100
        self.margin = 120
        self.colors = ['#e0f2ff', "#1c2c1e", "#4b674a", "#060b0d"]

        self.qle = QPushButton("X", self)
        self.qle.move(475, 5)
        self.qle.clicked.connect(self.close)
        self.qle.setFont(QFont('Ralleway', 18))
        self.qle.setStyleSheet(
            "color: #a0302d; "
            "max-height: 25px; "
            "max-width: 25px; ")

        self.smap = QSignalMapper(self)
        self.GetSquares()
        self.smap.mapped.connect(self.on_click)


        self.show()

    def GetSquares(self):

        for i in range(0, self.subject_names.__len__()):

            c1 = i * self.x * 1.2 + self.x
            self.Get_label(str(self.subject_names[i].SubID) + " " + str(self.subject_names[i].Name),
                           None, 20, c1, self.y + self.margin/2, self.x, False)

            for j in range(0, self.lab_maiking[i].__len__()):

                c2 = j * self.x * 1.2 + self.x
                label = self.Get_label(str(int(self.lab_maiking[i][j])),
                               self.colors[2], self.margin + 20 + c2, c1, self.x, self.x, True)

                label.clicked.connect(self.smap.map)  # соединить
                self.smap.setMapping(label, self.square_id)

                label.x = i
                label.y = j

                self.labels.append(label)
                self.square_id += 1


    def Get_label(self, text, color, x, y, width, height, aline) -> ClickLabel:
        label_sq = ClickLabel(self)
        label_sq.setText(str(text))
        label_sq.setFont(QFont("Ralleway", 12))
        if(aline):
            label_sq.setAlignment(Qt.AlignCenter)
        label_sq.setStyleSheet("background-color: " + str(color))
        label_sq.setGeometry(x, y, width, height)

        return label_sq

    @pyqtSlot(int)
    def on_click(self, id):
        # print(str(id) + "  " + str(self.labels[id + 1].x) + "," + str(self.labels[id + 1].y))
        self.labels[id + 1].setStyleSheet("background-color: blue")

        if(self.ctrl_press):
            prosent_add_maiking = -self.prosent_add_maiking
        else:
            prosent_add_maiking = self.prosent_add_maiking

        if(self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y] < 100):
            self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y] += prosent_add_maiking
        self.labels[id + 1].setText(str(self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y]))

        self.update()

        #обновление бд
        self.table.Update_square(self.labels[id + 1].y,
                                 self.subject_names[self.labels[id + 1].x].Name,
                                 prosent_add_maiking)

        # self.subject_names, self.max_lab_count, self.lab_maiking = self.table.Make_table()



    # вызывается при нажатии кнопки мыши
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.pos()

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Control:
            self.ctrl_press = True

    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Control:
            self.ctrl_press = False

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQt5_view()
    sys.exit(app.exec_())
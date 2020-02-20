import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import date
from Table import Table
from Objects import Subject
from View.Clicked_label import ClickLabel

from View.Color_theme import Color_theme_wb


class PyQt5_view(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # установить тему приложения: 0 - dark; 1 - white
        self.theme_init(0)

        self.init_ui()
        self.edit_opt(0)
        self.init_options_window()

        self.setWindowTitle("Lab trecker")

        # self.setWindowIcon(QIcon('img/logo.png'))

        self.show()

    def edit_opt(self, edit):
        if (edit):
            # self.setGeometry(770, 400, 510, 240)
            self.setFixedSize(510, 240)
            # self.init_options_window()
        else:
            self.setFixedSize(510, 200)
            # self.setGeometry(770, 400, 510, 200)

    def init_ui(self):
        self.table = Table()
        self.subject_names, self.max_lab_count, self.lab_maiking = self.table.Make_table()

        self.labels = [self.subject_names.__len__() * self.max_lab_count]
        self.labels_names = [self.subject_names.__len__()]

        self.ctrl_press = False
        self.prosent_add_maiking = 10
        self.square_id = 0
        self.x = 30
        self.y = 100
        self.margin = 120


        self.qle = QPushButton("X", self)
        self.qle.move(465, 199)
        self.qle.clicked.connect(self.close)
        self.qle.setFont(QFont('Ralleway', 14))
        self.qle.setStyleSheet(
            "color: #a0302d; "
            "max-height: 24px; "
            "max-width: 24px; ")

        self.smap = QSignalMapper(self)
        self.GetSquares()
        self.smap.mapped.connect(self.on_click)

    def theme_init(self, int):
        self.colored_theme = Color_theme_wb()

        if(int == 1):
            self.theme_color = self.colored_theme.theme_color_white
            self.sqare_colors = self.colored_theme.sqare_colors_white
            self.setStyleSheet("background-color: " + self.colored_theme.background_white)
            self.setWindowOpacity(self.colored_theme.opacity_white)
        else:
            self.theme_color = self.colored_theme.theme_color_black
            self.sqare_colors = self.colored_theme.sqare_colors_black
            self.setStyleSheet("background-color: " + self.colored_theme.background_black)
            self.setWindowOpacity(self.colored_theme.opacity_black)

    def init_options_window(self):
        untheme = 1
        strs_font = " color: rgb(" + str(self.theme_color[untheme][0]) + \
               ", " + str(self.theme_color[untheme][1]) + \
               ", " + str(self.theme_color[untheme][2]) + "); "

        self.combo =  QComboBox(self)
        for i in self.subject_names:
            self.combo.addItem(i.Name)
        self.combo.move(20, 200)
        self.combo.setFont(QFont('Ralleway', 12))
        self.combo.setStyleSheet( strs_font )


        self.line_edit = QLineEdit(self)
        self.line_edit.move(160, 200)
        self.line_edit.setFont(QFont('Ralleway', 12))
        self.line_edit.setStyleSheet(
            "max-width: 135px; " +  strs_font)


        self.spinBox =  QSpinBox(self)
        self.spinBox.move(302, 200)
        self.spinBox.setFont(QFont('Ralleway', 12))
        self.spinBox.setStyleSheet(strs_font)


        self.add_button = QPushButton("Add", self)
        self.add_button.move(355, 199)
        self.add_button.clicked.connect(self.ok_button)
        self.add_button.setFont(QFont('Ralleway', 12))
        self.add_button.setStyleSheet(
            "max-height: 25px; " 
            "max-width: 40px; " + strs_font )

        self.add_button = QPushButton("Del", self)
        self.add_button.move(396, 199)
        self.add_button.clicked.connect(self.dell_button)
        self.add_button.setFont(QFont('Ralleway', 12))
        self.add_button.setStyleSheet(
            "max-height: 25px; "
            "max-width: 40px; " +  strs_font)

        self.show()

    def GetSquares(self):
        for i in range(0, self.subject_names.__len__()):

            c1 = i * self.x * 1.2 + self.x/3
            label_n = self.Get_label(str(self.subject_names[i].SubID) + " " + str(self.subject_names[i].Name),
                           None, 20, c1, self.y + self.margin/2, self.x, False)
            self.labels_names.append(label_n)

            for j in range(0, self.lab_maiking[i].__len__()):

                c2 = j * self.x * 1.2 + self.x
                label = self.Get_label(str(int(self.lab_maiking[i][j])),
                              None, self.margin + 20 + c2, c1, self.x, self.x, True)


                label.clicked.connect(self.smap.map)  # соединить
                self.smap.setMapping(label, self.square_id)

                label.x = i
                label.y = j
                label.color, label.color_font = self.get_color(self.lab_maiking[i][j])

                self.set_label_color(label)

                self.labels.append(label)
                self.square_id += 1

    def Get_label(self, text, color, x, y, width, height, aline) -> ClickLabel:
        label_sq = ClickLabel(self)
        label_sq.setText(str(text))
        label_sq.setFont(QFont("Ralleway", 12))
        if(aline):
            label_sq.setAlignment(Qt.AlignCenter)

        untheme = 1

        strs = "color: rgb(" + str(self.theme_color[untheme][0]) + \
               ", " + str(self.theme_color[untheme][1]) + \
               ", " + str(self.theme_color[untheme][2]) + ")"
        label_sq.setStyleSheet("background-color: " + str(color) + ";" + strs)
        label_sq.setGeometry(x, y, width, height)

        return label_sq

    @pyqtSlot(int)
    def on_click(self, id):
        # print(str(id) + "  " + str(self.labels[id + 1].x) + "," + str(self.labels[id + 1].y))
        if(self.ctrl_press):
            prosent_add_maiking = -self.prosent_add_maiking
        else:
            prosent_add_maiking = self.prosent_add_maiking


        self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y] += prosent_add_maiking
        z = self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y]

        if(100 >= z >= 0):
            self.labels[id + 1].setText(str(self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y]))
            self.labels[id + 1].color, self.labels[id + 1].color_font = \
                self.get_color(self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y])
            self.set_label_color(self.labels[id + 1])
            self.update()

            self.table.Update_square(self.labels[id + 1].y,
                                     self.subject_names[self.labels[id + 1].x].Name,
                                     prosent_add_maiking)

        else:
            self.lab_maiking[self.labels[id + 1].x][self.labels[id + 1].y] -= prosent_add_maiking

        # self.subject_names, self.max_lab_count, self.lab_maiking = self.table.Make_table()

    def set_label_color(self, label):
        strs = "background-color: rgb(" + str(label.color[0]) + \
               ", " + str(label.color[1]) + \
               ", " + str(label.color[2]) + "); "

        # untheme = 1
        # strs_font = "color: rgb(" + str(self.theme_color[untheme][0]) + \
        #        ", " + str(self.theme_color[untheme][1]) + \
        #        ", " + str(self.theme_color[untheme][2]) + ")"


        label.setStyleSheet(strs  + label.color_font)


    def get_color(self, count):
        l = []

        m = int(count/20)
        if(m >= self.sqare_colors.__len__()):
            m = self.sqare_colors.__len__() - 1
        l = self.sqare_colors[m]

        untheme = 0
        if(count < 20):
            untheme = 1

        strs_font = "color: rgb(" + str(self.theme_color[untheme][0]) + \
               ", " + str(self.theme_color[untheme][1]) + \
               ", " + str(self.theme_color[untheme][2]) + ")"

        return l , strs_font

    def ok_button(self):
        if(self.line_edit.text().__len__() == 0):
            self.table.Change_lab_count(self.combo.currentText(), self.spinBox.text())
        else:
            self.table.Add_new_Subject(self.line_edit.text(), self.spinBox.text())

    def dell_button(self):
        self.table.Delete_subject(str(self.combo.currentText()))


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
        if e.key() == Qt.Key_Shift:
            if(self.height() > 210):
                self.edit_opt(0)
            else:
                self.edit_opt(1)


    def keyReleaseEvent(self, e):
        if e.key() == Qt.Key_Control:
            self.ctrl_press = False


# def resource_path(relative_path):
#     try:
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PyQt5_view()
    sys.exit(app.exec_())
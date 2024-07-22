import sys
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox
from PyQt5.QtWidgets import QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import os
import tempfile

# Путь к файлу с историей вычислений
storage_path = os.path.join(tempfile.gettempdir(), 'history4.txt')


class MyWindow(QMainWindow):
    ANSWER = ""

    def __init__(self):
        super().__init__()
        uic.loadUi('pashкалькулятор.ui', self)  # Загружаем дизайн

        self.figure_combo.activated[str].connect(self.onFigureSelect)

        self.clear_btn.clicked.connect(self.clear)

        self.exitButton.triggered.connect(self.exitEvent)

        self.about_program = AboutProgram()
        self.programButton.triggered.connect(self.about)

        '''self.about_author = AboutAuthor()
        self.authorButton.triggered.connect(self.about2)'''
        self.about_author = AboutAuthor2()
        self.authorButton.triggered.connect(self.about2)

        self.btn.clicked.connect(self.find_perimetr)

        self.openButton.triggered.connect(lambda: self.read_file_history())
        self.save_btn.clicked.connect(self.save_file_history)
        self.clear_hist_btn.clicked.connect(self.clear_file_history)

    def read_file_history(self):
        if not os.path.exists(storage_path):
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Critical)
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText("Нет истории вычислений")
            msg_err.exec_()
        else:
            if SettingsWindow.font_type.currentText() == "Arial":
                my_font = "Arial"
            else:
                my_font = "Calibri"
            if SettingsWindow.font_type1.currentText() == "Жирный":
                self.textEdit.setFont(QtGui.QFont(my_font, 12, QtGui.QFont.Bold))
            else:
                self.textEdit.setFont(QtGui.QFont(my_font, 12))
            f = open(storage_path, 'r')
            self.textEdit.setText(f.read())
            f.close()

    def save_file_history(self):
        if not os.path.exists(storage_path):
            f = open(storage_path, "w")
            f.close()
        with open(storage_path, 'a') as f:
            letter = self.ANSWER
            f.writelines(letter)

    def clear_file_history(self):
        if not os.path.exists(storage_path):
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Critical)
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText("Нет истории вычислений")
            msg_err.exec_()
        else:
            result = QMessageBox.question(self, "Подтверждение",
                                          "Очистить историю?",
                                          QMessageBox.Yes | QMessageBox.No,
                                          QMessageBox.No)
            if result == QMessageBox.Yes:
                self.textEdit.clear()
                os.remove(storage_path)
            else:
                pass

    def about(self):
        self.about_program.show()

    def about2(self):
        self.about_author.show()

    def onFigureSelect(self, figure):
        if figure == 'Прямоугольник':
            self.lbl_info_c.setVisible(False)
            self.ed_c.setVisible(False)
        else:  # Треугольник
            self.lbl_info_c.setVisible(True)
            self.ed_c.setVisible(True)

    def clear(self):
        self.ed_a.clear()
        self.ed_b.clear()
        self.ed_c.clear()

    def exitEvent(self):
        confirm = QMessageBox.question(self, 'Подтверждение выхода',
                                       'Вы уверены, что хотите выйти?',
                                       QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            sys.exit()

    def closeEvent(self, e):
        result = QMessageBox.question(self, "Закрытие окна",
                                      "Вы действительно хотите выйти?",
                                      QMessageBox.Yes | QMessageBox.No)
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:
            e.ignore()

    def find_perimetr(self):
        msg_err = QMessageBox()
        msg_err.setIcon(QMessageBox.Critical)
        try:
            figure = self.figure_combo.currentText()
            if figure == 'Треугольник':
                a = int(self.ed_a.text())
                b = int(self.ed_b.text())
                c = int(self.ed_c.text())
                if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or c + b <= a:
                    raise ValueError
                else:
                    perimetr = a + b + c
                    answer = f"Периметр Треугольника: {a} + {b} + {c} = {perimetr}"
            else:
                a = int(self.ed_a.text())
                b = int(self.ed_b.text())
                if a <= 0 or b <= 0:
                    raise ValueError
                else:
                    perimetr = 2 * (a + b)
                    answer = f"Периметр Прямоугольника: 2*({a} + {b}) = {perimetr}"

        except ValueError:
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText("Проверьте значения")
            msg_err.exec_()
        else:
            self.ANSWER = answer + "\n"
            self.show_answer(answer)
            self.clear_btn.setEnabled(True)

    def show_answer(self, answer):
        self.second_form = SecondForm(answer)
        self.second_form.show()


class AboutProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Программа нахождения периметра для прямоугольника и треугольника.')
        self.layout().addWidget(self.info)


class AboutAuthor2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Об авторе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText('Автор: Наумов Павел Валерьевич.\n'
                          'Номер телефона: 89308830536')
        self.layout().addWidget(self.info)


'''class AboutAuthor(QWidget):
    def __init__(self):
        super().__init()
        self.setWindowTitle('Об авторе')
        self.setLayout(QVBoxLayout(self))
        self.image = QLabel(self)
        pixmap = QPixmap('a.jpg')
        self.image.setPixmap(pixmap)
        self.layout().addWidget(self.image)'''


class SecondForm(QMainWindow):
    def __init__(self, answer):
        super().__init__()

        self.setWindowTitle('Периметр')
        self.resize(200, 215)

        self.lbl = QLabel(answer, self)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)


class SettingsWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('Settings.ui', self)
        self.setWindowTitle("Настройки")

        self.clear_history_button.clicked.connect(self.clear_file_history)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # создаем приложение
    window = MyWindow()  # создаем окно
    window.show()  # показываем окно
    sys.exit(app.exec())  # запускаем приложение

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QComboBox, QGridLayout, QVBoxLayout, QGroupBox, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
import os
import tempfile

storage_path = os.path.join(tempfile.gettempdir(), 'history.txt')


class CalculatorForm(QWidget):
    answer=str('')
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()

        self.setWindowTitle('Калькулятор')
        self.setWindowIcon(QtGui.QIcon(""))

        self.lbl_info_a = QLabel("Коэффициент a:")
        self.ed_a = QLineEdit()
        self.lbl_info_b = QLabel("Коэффициент b:")
        self.ed_b = QLineEdit()
        self.ed_a.textChanged.connect(self.data_change)
        self.ed_b.textChanged.connect(self.data_change)

        self.info_box = QGroupBox()
        self.info_vbox = QVBoxLayout()
        self.info_vbox.addWidget(self.lbl_info_a)
        self.info_vbox.addWidget(self.ed_a)
        self.info_vbox.addWidget(self.lbl_info_b)
        self.info_vbox.addWidget(self.ed_b)
        self.info_box.setLayout(self.info_vbox)

        self.figure_label = QLabel('Выберите операцию:')
        self.figure_combo = QComboBox(self)
        self.figure_box = QGroupBox()
        self.figure_vbox = QVBoxLayout()
        self.figure_vbox.setSpacing(20)
        self.figure_combo.addItems(['Сложение', 'Вычитание', 'Умножение', 'Деление'])
        self.figure_vbox.addWidget(self.figure_label)
        self.figure_vbox.addWidget(self.figure_combo)
        self.figure_vbox.addStretch()
        self.figure_box.setLayout(self.figure_vbox)

        self.btn = QPushButton('Рассчитать')
        self.btn.clicked.connect(self.calculate_result)
        self.clear_btn = QPushButton("Очистить")
        self.clear_btn.setEnabled(False)
        self.clear_btn.clicked.connect(self.clear)
        self.btn_box = QGroupBox()
        self.btn_vbox = QVBoxLayout()
        self.btn_vbox.addWidget(self.btn)
        self.btn_vbox.addWidget(self.clear_btn)
        self.btn_box.setLayout(self.btn_vbox)

        self.grid.addWidget(self.info_box, 0, 0)
        self.grid.addWidget(self.figure_box, 0, 1)
        self.grid.addWidget(self.btn_box, 1, 0, 1, 2)

        self.setLayout(self.grid)

    def data_change(self):
        self.clear_btn.setEnabled(False)

    def clear(self):
        self.ed_a.clear()
        self.ed_b.clear()

    def closeEvent(self, e):
        result = QMessageBox.question(self, "Закрыть окно",
                                      "Вы уверены, что хотите выйти?",
                                      QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.No)
        if result == QMessageBox.Yes:
            e.accept()
            QWidget.closeEvent(self, e)
        else:
            e.ignore()

    def calculate_result(self):
        msg_err = QMessageBox()
        msg_err.setIcon(QMessageBox.Critical)
        a = int(self.ed_a.text())
        b = int(self.ed_b.text())
        try:
            figure = self.figure_combo.currentText()
            if figure == 'Сложение':
                if len(str(a)) >= 7 or len(str(b)) >= 7:
                    raise ArithmeticError("Слишком большие числа для вычислений")
                answer = f"Решение: {a} + {b} = {a + b}"
            elif figure == 'Вычитание':
                if len(str(a)) >= 7 or len(str(b)) >= 7:
                    raise ArithmeticError("Слишком большие числа для вычислений")
                answer = f"Решение: {a} - {b} = {a - b}"
            elif figure == 'Умножение':
                if len(str(a)) >= 7 or len(str(b)) >= 7:
                    raise ArithmeticError("Слишком большие числа для вычислений")
                answer = f"Решение: {a} * {b} = {a * b}"
            elif figure == 'Деление':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль невозможно")
                elif len(str(a)) >= 7 or len(str(b)) >= 7:
                    raise ArithmeticError("Слишком большие числа для вычислений")
                answer = f"Решение: {a} / {b} = {a / b}"
            else:
                raise ValueError("Неверная операция выбрана")

        except ValueError as e:
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText(f"Ошибка: {e}")
            msg_err.exec_()
        except ArithmeticError as e:
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText(f"Ошибка: {e}")
            msg_err.exec_()
        except ZeroDivisionError as e:
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText(f"Ошибка: {e}")
            msg_err.exec_()
        else:
            self.show_answer(answer)
            self.clear_btn.setEnabled(True)

    def show_answer(self, answer):
        self.second_form = ResultForm(answer)
        self.second_form.show()


class ResultForm(QMainWindow):
    def __init__(self, answer):
        super().__init__()

        self.setWindowTitle('Решение')
        self.resize(200, 215)

        self.lbl = QLabel(answer, self)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = CalculatorForm()
    calculator.show()
    sys.exit(app.exec())

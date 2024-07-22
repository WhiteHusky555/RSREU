import sys
from PyQt5 import QtGui, QtWidgets, QtCore, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QLabel, QVBoxLayout
import os
import tempfile
from PyQt5.QtCore import Qt


storage_path = os.path.join(tempfile.gettempdir(), 'history.txt')


class Calculator(QtWidgets.QMainWindow):
    answer=''
    def __init__(self):
        super().__init__()
        uic.loadUi('mainwindow.ui', self)
        self.setupUi()
        self.ochist.clicked.connect(self.clear)

        self.Exit.triggered.connect(self.exitEvent)

        self.about_program1 = AboutProgram()
        self.about_program.triggered.connect(self.about)

        self.about_author1 = AboutAuthor()
        self.about_author.triggered.connect(self.about2)

        self.vichisl.clicked.connect(self.calculate)

        self.Open.triggered.connect(lambda: self.read_file_history())
        self.Styles.triggered.connect(lambda: self.open_settings())
        self.sohran.clicked.connect(self.save_file_history)
        #self.clear_hist_btn.clicked.connect(self.clear_file_history)

    def setupUi(self):
        self.setWindowTitle("КалькуляторQtDesigner")
        self.resize(230, 300)
        self.setMinimumSize(QtCore.QSize(400, 300))
        self.setMaximumSize(QtCore.QSize(800, 600))
        self.setBaseSize(QtCore.QSize(500, 600))
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 231, 282))
        self.tabWidget.setObjectName("tabWidget")

        self.setupInputTab()
        self.setupHistoryTab()

        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.setMenuBar(self.menubar)

        self.setupMenus()

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        self.get_a.textChanged['QString'].connect(self.pokaz.update)
        self.ochist.clicked.connect(self.clear)
        #self.ochist.pressed.connect(self.get_b.clear)

    def setupInputTab(self):
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 101, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.input_a = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_a.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input_a.setText("")
        self.input_a.setMaxLength(8)
        self.input_a.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_a.setObjectName("input_a")
        self.verticalLayout_2.addWidget(self.input_a)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.input_b = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.input_b.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.input_b.setText("")
        self.input_b.setMaxLength(8)
        self.input_b.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_b.setObjectName("input_b")
        self.verticalLayout_2.addWidget(self.input_b)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(160, 10, 160, 84))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.radioButton_sloj = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_sloj.setObjectName("radioButton_sloj")
        self.verticalLayout_3.addWidget(self.radioButton_sloj)
        self.radioButton_vich = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_vich.setObjectName("radioButton_vich")
        self.verticalLayout_3.addWidget(self.radioButton_vich)
        self.radioButton_ymnoj = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_ymnoj.setObjectName("radioButton_ymnoj")
        self.verticalLayout_3.addWidget(self.radioButton_ymnoj)
        self.radioButton_del = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radioButton_del.setObjectName("radioButton_del")
        self.verticalLayout_3.addWidget(self.radioButton_del)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(160, 100, 61, 80))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.vichisl = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.vichisl.setObjectName("vichisl")
        self.verticalLayout_4.addWidget(self.vichisl)
        self.ochist = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.ochist.setObjectName("ochist")
        self.verticalLayout_4.addWidget(self.ochist)
        self.sohran = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.sohran.setObjectName("sohran")
        self.verticalLayout_4.addWidget(self.sohran)
        self.pokaz = QtWidgets.QLabel(self.tab)
        self.pokaz.setGeometry(QtCore.QRect(30, 160, 35, 10))
        self.pokaz.setText("")
        self.pokaz.setObjectName("pokaz")
        self.tabWidget.addTab(self.tab, "")

    def setupHistoryTab(self):
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.show_history_vich = QtWidgets.QTextEdit(self.tab_2)
        self.show_history_vich.setGeometry(QtCore.QRect(0, 0, 241, 231))
        self.show_history_vich.setReadOnly(True)
        self.show_history_vich.setObjectName("show_history_vich")
        self.tabWidget.addTab(self.tab_2, "")

    def setupMenus(self):
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.Open = QtWidgets.QAction(self)
        self.Open.setObjectName("Open")
        self.Exit = QtWidgets.QAction(self)
        self.Exit.setObjectName("Exit")
        self.about_program = QtWidgets.QAction(self)
        self.about_program.setObjectName("about_program")
        self.about_author = QtWidgets.QAction(self)
        self.about_author.setObjectName("about_author")
        self.actionsfdg = QtWidgets.QAction(self)
        self.actionsfdg.setObjectName("actionsfdg")
        self.Styles = QtWidgets.QAction(self)
        self.Styles.setObjectName("Styles")

        self.menu.addAction(self.Open)
        self.menu.addSeparator()
        self.menu.addAction(self.Exit)
        self.menu_2.addAction(self.about_program)
        self.menu_2.addAction(self.about_author)
        self.menu_3.addAction(self.Styles)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindow", "Коэффициент а"))
        self.input_a.setPlaceholderText(_translate("MainWindow", "Коэффициент а"))
        self.label_2.setText(_translate("MainWindow", "Коэффициент b"))
        self.input_b.setPlaceholderText(_translate("MainWindow", "Коэффициент b"))
        self.label_3.setText(_translate("MainWindow", "Вид выражения"))
        self.radioButton_sloj.setText(_translate("MainWindow", "Сложение"))
        #self.radioButton_sloj.connect(self.onClicked)
        self.radioButton_vich.setText(_translate("MainWindow", "Вычитание"))
        self.radioButton_ymnoj.setText(_translate("MainWindow", "Умножение"))
        self.radioButton_del.setText(_translate("MainWindow", "Деление"))
        self.vichisl.setText(_translate("MainWindow", "Вычислить"))
        self.ochist.setText(_translate("MainWindow", "Очистить"))
        self.sohran.setText(_translate("MainWindow", "Сохранить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Решение"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "История"))
        self.menu.setTitle(_translate("MainWindow", "Файл"))
        self.menu_2.setTitle(_translate("MainWindow", "Справка"))
        self.menu_3.setTitle(_translate("MainWindow", "Стиль вывода"))
        self.Open.setText(_translate("MainWindow", "Открыть"))
        self.Exit.setText(_translate("MainWindow", "Выход"))
        self.about_program.setText(_translate("MainWindow", "О программе"))
        self.about_author.setText(_translate("MainWindow", "Об авторе"))
        self.actionsfdg.setText(_translate("MainWindow", "sfdg"))
        self.Styles.setText(_translate("MainWindow", "Открыть"))

    def clear(self):
        self.input_a.clear()
        self.input_b.clear()

    def calculate(self):
        msg_err = QMessageBox()
        msg_err.setIcon(QMessageBox.Critical)
        try:
            if self.radioButton_sloj.isChecked(): #Сложение
                a = float(self.input_a.text())
                b = float(self.input_b.text())
                answer = f"Решение: {a} + {b} = {a+b}"
            elif self.radioButton_vich.isChecked(): #Вычитание
                a = float(self.input_a.text())
                b = float(self.input_b.text())
                answer = f"Решение: {a} - {b} = {a-b}"
            elif self.radioButton_ymnoj.isChecked(): #Умножение
                a = float(self.input_a.text())
                b = float(self.input_b.text())
                answer = f"Решение: {a} * {b} = {a*b}"
            elif self.radioButton_del.isChecked(): #Деление
                a = float(self.input_a.text())
                b = float(self.input_b.text())
                if b==0:
                    raise ValueError
                answer = f"Решение: {a} \ {b} = {a / b}"
        except ValueError:
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText("Проверьте значения")
            msg_err.exec_()
        else:
            self.ANSWER = answer + "\n"
            self.show_answer(answer)
            self.ochist.setEnabled(True)

    def read_file_history(self):
        if not os.path.exists(storage_path):
            msg_err = QMessageBox()
            msg_err.setIcon(QMessageBox.Critical)
            msg_err.setWindowTitle("Ошибка!")
            msg_err.setText("Нет истории вычислений")
            msg_err.exec_()
        else:
            print(SettingsWindow.FONT_TYPE, SettingsWindow.FONT_TYPE1)
            if SettingsWindow.FONT_TYPE == "Arial":
                my_font = "Arial"
            else:
                my_font = "Calibri"
            if SettingsWindow.FONT_TYPE1 == "Жирный":
                self.show_history_vich.setFont(QtGui.QFont(my_font, 10, QtGui.QFont.Bold))
            else:
                self.show_history_vich.setFont(QtGui.QFont(my_font, 10))
            f = open(storage_path, 'r')
            self.show_history_vich.setText(f.read())
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
                self.show_history_vich.clear()
                os.remove(storage_path)
            else:
                pass
    def about(self):
        self.about_program1.show()

    def about2(self):
        self.about_author1.show()

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
    def show_answer(self, answer):
        self.second_form = SecondForm(answer)
        self.second_form.show()

    def open_settings(self):
        self.settings = SettingsWindow()
        self.settings.show()
class AboutProgram(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('О программе')
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText(f'Программа рассчёта числовых значений \n Подготовлена в рамках выполнения \n учебно-технологической практики.')
        self.layout().addWidget(self.info)


class AboutAuthor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Об авторе')
        uic.loadUi('AboutAuthor.ui', self)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(current_dir, 'cat.png')

        self.label.setPixmap(QtGui.QPixmap(image_path))


class SecondForm(QMainWindow):
    def __init__(self, answer):
        super().__init__()

        self.setWindowTitle('Решение')
        self.resize(200, 215)

        self.lbl = QLabel(answer, self)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.lbl)


class SettingsWindow(QMainWindow):
    FONT_TYPE = "Arial"
    FONT_TYPE1 = "Нормальный"

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('Settings.ui', self)
        self.setWindowTitle("Настройки")

        self.font_type.setCurrentText(SettingsWindow.FONT_TYPE)
        self.font_type1.setCurrentText(SettingsWindow.FONT_TYPE1)

        self.font_type.currentTextChanged.connect(self.change_font)
        self.font_type1.currentTextChanged.connect(self.change_font)

    def change_font(self):
        SettingsWindow.FONT_TYPE = self.font_type.currentText()
        SettingsWindow.FONT_TYPE1 = self.font_type1.currentText()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Calculator()
    #window.__init__()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()

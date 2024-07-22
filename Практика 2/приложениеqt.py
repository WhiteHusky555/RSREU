import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QTabWidget, QWidget, QVBoxLayout, QFrame, QLabel, QLineEdit, QRadioButton, QPushButton, QTextEdit, QScrollArea
import PyQt5 as Qt
import os
import tempfile
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.ttk as ttk
from itertools import count
from tkinter import messagebox as mb

class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image="")
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)

def change_data(event):
    """ Отлавливает изменение вводимых данных """
    label_text['text'] = ''
    label_root['text'] = ''
def foo2(e):
    entry_a.delete ('5', '6')
    label_text['text'] = ''
    label_root['text'] = ''
def foo(e):
    entry_b.delete('5', '6')
    label_text['text'] = ''
    label_root['text'] = ''
def close_window():
    """ Выход из приложения """
    if mb.askyesno("Выход", "Вы действительно хотите выйти из калькулятора?"):
        root.destroy()
def program_description():
    """ Отображение окна О программе """
    mb.showinfo(
        "О программе", "Программа расчёта числовых значений\
            Подготовлена в рамках выполнения учебно-технологической практики.")
def about_show():
    """ Окно с информацией об авторе"""
    about = tk.Toplevel()
    about.title("Информация об авторе")
    filepath_about_author = 'shigure-ui-dance.gif'
    with Image.open(filepath_about_author) as img:
        width, height = img.size
    about.geometry(f'{width}x{height}')
    about.resizable(False, False)
    lbl = ImageLabel(about)
    lbl.pack()
    lbl.load('shigure-ui-dance.gif')
    # Делаем дочернее окно модальным
    about.grab_set() # перехват событий, происходящих в приложении
    about.focus_set() # захват и удержание фокуса
    about.wait_window()
def is_file_empty(file_path):
    with open(file_path, 'r') as file:
        if file.read().strip()=='':
            return True
        else:
            return False

def read_file_history():
    """Отображение истории вычислений """
    if not os.path.exists(storage_path) or is_file_empty(storage_path):
        mb.showinfo(title="Информация", message="Нет истории вычислений.")
    else:
        text.delete(1.0, tk.END)
        with open(storage_path, 'r') as f:
            text.insert(1.0, f.read())
            text.focus_set()

def save_file_history():
    """ Запись результата в файл с историей вычислений"""
    if not os.path.exists(storage_path):
        f = open(storage_path, "w")
        f.close()
    with open(storage_path, 'a') as f:
        letter = label_text['text'] + '\n ' + label_root['text'] + '\n'
        f.writelines(letter)
def radiobutton_change():
    """" Выбор переключателя делает видимым или скрывает
    метку и поле ввода для ввода коэффициента c """
    label_text['text'] = ''
    label_root['text'] = ''
    data_clear()

def popup(event):
    """ Определение выбора пункта контекстного меню """
    popupmenu.post(event.x_root, event.y_root)

def history_clear():
    """ Очистка многострочного текстового поля """
    answer = mb.askyesno(title="Подтверждение действия", message="Очистить историю?")
    if answer == True:
        text.delete(1.0, tk.END)
        f = open(storage_path, "w")
        f.write('')
        f.close()

def data_clear():
    """ Очистка полей для ввода коэффициентов уравнения и Lable'v с ответами """
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    label_root['text'] = ''
    label_text['text'] = ''
    button_save['state'] = 'disable'
    button_clear['state'] = 'disable'


def run_solution():
    """ Считывание коэффициентов уравнения """
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
    except ValueError:
        mb.showerror('Ошибка!', 'Проверьте значения коэффициентов!')
    except Exception:
        mb.showerror('Ошибка!', 'Непонятная ошибка.')
    else:
        if rb_var.get() == 1:
            label_text['text'] = "Решение cуммы:\n " \
                                 "{0} + {1}".format(a, b, equation_solution(a, b))
        elif rb_var.get() == 2:
            label_text['text'] = "Решение разности:\n " \
                                 "{0} - {1}".format(a, b, equation_solution(a, b))
        elif rb_var.get() == 3:
            label_text['text'] = "Решение произведения:\n " \
                                 "{0} * {1}".format(a, b, equation_solution(a, b))
        elif rb_var.get() == 4:
            label_text['text'] = "Решение частного:\n " \
                                 "{0} / {1}".format(a, b, equation_solution(a, b))

    button_save['state'] = 'active'
    button_clear['state'] = 'active'


def equation_solution(a, b):
    if rb_var.get() == 1:
        label_root['text'] = f'Значение равно\n {a + b}'
    elif rb_var.get() == 2:
        label_root['text'] = f'Значение равно\n {a - b}'
    elif rb_var.get() == 3:
        x = a * b
        label_root['text'] = 'Значение равно\n {0:.4f}'.format(x)
    elif rb_var.get() == 4 and b == float(0):
        label_root['text'] = f'Значение не определено'
    elif rb_var.get() == 4:
        x = a / b
        label_root['text'] = 'Значение равно\n {0:.4f}'.format(x)


storage_path = os.path.join(tempfile.gettempdir(), 'historyComputing21.txt')
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Дебильный калькулятор")
window.setGeometry(100, 100, 300, 300)
window.setFixedSize(300, 300)

# Main Menu Setup
main_menu = window.menuBar()
file_menu = main_menu.addMenu("Файл")
help_menu = main_menu.addMenu("Справка")

# File Menu Items
open_action = QAction("Открыть...", window)
open_action.triggered.connect(read_file_history)
exit_action = QAction("Выход", window)
exit_action.triggered.connect(close_window)
file_menu.addAction(open_action)
file_menu.addSeparator()
file_menu.addAction(exit_action)

# Help Menu Items
about_action = QAction("О программе", window)
about_action.triggered.connect(program_description)
author_action = QAction("Об авторе", window)
author_action.triggered.connect(about_show)
help_menu.addAction(about_action)
help_menu.addAction(author_action)

# Tab Creation
tab_widget = QTabWidget()
solution_tab = QWidget()
history_tab = QWidget()
tab_widget.addTab(solution_tab, "Решение")
tab_widget.addTab(history_tab, "Просмотр истории")

# Widgets Placement in "Solution" Tab
layout_solution = QVBoxLayout(solution_tab)
frame_coefficients = QFrame()
frame_type = QFrame()
frame_result = QFrame()
frame_button = QFrame()
layout_solution.addWidget(frame_coefficients)
layout_solution.addWidget(frame_type)
layout_solution.addWidget(frame_result)
layout_solution.addWidget(frame_button)

label_a = QLabel("a = ")
label_b = QLabel("b = ")
entry_a = QLineEdit()
entry_b = QLineEdit()
entry_a.textChanged.connect(foo2)
entry_b.textChanged.connect(foo)

frame_coefficients.setLayout(QVBoxLayout())
frame_coefficients.layout().addWidget(label_a)
frame_coefficients.layout().addWidget(entry_a)
frame_coefficients.layout().addWidget(label_b)
frame_coefficients.layout().addWidget(entry_b)

rb_var = 1
rb_lin = QRadioButton("Сложение")
rb_kv = QRadioButton("Вычитание")
rb_mul = QRadioButton("Умножение")
rb_div = QRadioButton("Деление")
rb_lin.toggled.connect(radiobutton_change)
rb_kv.toggled.connect(radiobutton_change)
rb_mul.toggled.connect(radiobutton_change)
rb_div.toggled.connect(radiobutton_change)

frame_type.setLayout(QVBoxLayout())
frame_type.layout().addWidget(rb_lin)
frame_type.layout().addWidget(rb_kv)
frame_type.layout().addWidget(rb_mul)
frame_type.layout().addWidget(rb_div)

label_text = QLabel()
label_root = QLabel()
frame_result.setLayout(QVBoxLayout())
frame_result.layout().addWidget(label_text)
frame_result.layout().addWidget(label_root)

button_res = QPushButton("Решить")
button_clear = QPushButton("Очистить")
button_save = QPushButton("Сохранить")
button_res.clicked.connect(run_solution)
button_clear.clicked.connect(data_clear)
button_save.clicked.connect(save_file_history)

frame_button.setLayout(QVBoxLayout())
frame_button.layout().addWidget(button_res)
frame_button.layout().addWidget(button_clear)
frame_button.layout().addWidget(button_save)

# Widgets Placement in "History" Tab
layout_history = QVBoxLayout(history_tab)
text_edit = QTextEdit()
scroll_area = QScrollArea()
scroll_area.setWidgetResizable(True)
scroll_area.setWidget(text_edit)
layout_history.addWidget(scroll_area)

# Context Menu
context_menu = QMenu()
context_menu.addAction("Очистить", history_clear)
context_menu.addAction("Показать историю", read_file_history)

text_edit.setContextMenuPolicy(ContextMenuPolicy.Qt.CustomContextMenu)
text_edit.customContextMenuRequested.connect(context_menu.popup)

window.setCentralWidget(tab_widget)
window.show()
sys.exit(app.exec())

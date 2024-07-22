import tkinter as tk
import tkinter.ttk as ttk
from itertools import count
from tkinter import messagebox as mb
import os
import tempfile
from PIL import Image, ImageTk # сторонний модуль для отображения картинок
# устанавливается командой pip install Pillow
# Путь к файлу с историей вычислений
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

storage_path = os.path.join(tempfile.gettempdir(), 'historyComputing2.txt')
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


# Настройка окна
root = tk.Tk()
root.title("Калькулятор")
root.geometry('300x300')
root.resizable(False, False)


# Настройка главного меню
mainmenu = tk.Menu(root)
root.config(menu=mainmenu)


# Создание выпадающих списков команд
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Открыть...", command=read_file_history)
filemenu.add_separator()
filemenu.add_command(label="Выход", command=close_window)
helpmenu = tk.Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе", command=program_description)
helpmenu.add_command(label="Об авторе", command=about_show)


# Подвязыванием экземпляры меню к главному меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)


# Создание вкладок
nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
nb.add(frame1, text='Решение')
nb.add(frame2, text='Просмотр истории')


# Размещение виждетов на вкладке "Решение уравнения"

#окошко a b c
frame_koef = tk.LabelFrame(frame1, text="Укажите коэффициенты:")
frame_koef.grid(row=0, column=0, columnspan=2, padx=15, pady=5)
#окошко вида выражения
frame_type = tk.LabelFrame(frame1, text="Вид выражения")
frame_type.grid(row=0, column=2, padx=5, pady=5)
frame_result = tk.Frame(frame1)
frame_result.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
frame_button = tk.Frame(frame1)
frame_button.grid(row=1, column=2, padx=5, pady=5)
#настройка a b c
tk.Label(frame_koef, text="a = ", font=("Comic Sans MS", 11, "bold"),
fg='#c21d4a').grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_koef, text="b = ", font=("Comic Sans MS", 11, "bold"),
fg='#c21d4a').grid(row=1, column=0, padx=5, pady=5)
#label_c = tk.Label(frame_koef, text="c = ", font=("Comic Sans MS", 11, "bold"), fg='#c21d4a')
#label_c.grid(row=2, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_koef, width=10)
#entry_a.bind("<KeyPress>", change_data)
entry_a.grid(row=0, column=1, padx=5, pady=10)
entry_b = tk.Entry(frame_koef, width=10)
#entry_b.bind("<KeyPress>", change_data)
entry_b.grid(row=1, column=1, padx=5, pady=5)
entry_a.bind('<KeyPress>',foo2)
entry_b.bind('<KeyPress>',foo)
#current_text_a=entry_a.get()
#current_text_b=entry_b.get()
#entry_a.bind("<KeyPress>", check_changes)
#entry_b.bind("<KeyPress>", check_changes)
#entry_c = tk.Entry(frame_koef, width=10)
#entry_c.grid(row=2, column=1, padx=5, pady=10)
#настройка вида выражения
rb_var = tk.IntVar()
rb_var.set(1)

rb_lin = tk.Radiobutton(frame_type, variable=rb_var, text='Сложение', value=1,
command=radiobutton_change)
rb_lin.grid(row=0, column=0, pady=5, sticky='w')

rb_kv = tk.Radiobutton(frame_type, variable=rb_var, text='Вычитание', value=2,
command=radiobutton_change)
rb_kv.grid(row=1, column=0, pady=5, sticky='w')

rb_mul = tk.Radiobutton(frame_type, variable=rb_var, text='Умножение', value=3,
command=radiobutton_change)
rb_mul.grid(row=2, column=0, pady=5, sticky='w')

rb_div = tk.Radiobutton(frame_type, variable=rb_var, text='Деление', value=4,
command=radiobutton_change)
rb_div.grid(row=3, column=0, pady=5, sticky='w')

label_text = tk.Label(frame_result)
label_text.grid(row=0, column=0)
label_root = tk.Label(frame_result)
label_root.grid(row=1, column=0)
button_res = tk.Button(frame_button, width=12, text="Решить", command=run_solution)
button_res.grid(row=0, column=0, padx=5, pady=2, )
button_clear = tk.Button(frame_button, state='disable', width=12, text="Очистить", command=data_clear)
button_clear.grid(row=1, column=0, padx=5, pady=2)
button_save = tk.Button(frame_button, state='disabled', width=12, text="Сохранить",
command=save_file_history)
button_save.grid(row=2, column=0, padx=5, pady=2)


# Размещение виждетов на вкладке "Просмотр истории"
# Многострочное текстовое поле с полосой прокрутки
text = tk.Text(frame2, wrap=tk.WORD)
scroll = tk.Scrollbar(frame2, command=text.yview)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scroll.set)
text.pack(side=tk.LEFT)


# Контекстное меню
popupmenu = tk.Menu(tearoff=0)
popupmenu.add_command(label="Очистить", command=history_clear)
popupmenu.add_command(label="Показать историю", command=read_file_history)
text.bind('<Button-3>', popup)
root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()


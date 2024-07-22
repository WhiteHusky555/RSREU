import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox as mb
import os
import tempfile
from PIL import Image, ImageTk # сторонний модуль для отображения картинок
# устанавливается командой pip install Pillow
# Путь к файлу с историей вычислений
storage_path = os.path.join(tempfile.gettempdir(), 'historyComputing.txt')
def close_window():
    """ Выход из приложения """
    if mb.askyesno("Выход", "Вы действительно хотите выйти из приложения?"):
        root.destroy()
def program_description():
    """ Отображение окна О программе """
    mb.showinfo(
        "О программе", "Программа нахождения корней уравнений первой и второй степени.\
        Подготовлена в рамках выполнения лабораторной работы по дисциплине\
        'Современные технологии и языки программирования'.")
def about_show():
    """ Окно с информацией об авторе"""
    about = tk.Toplevel()
    about.title("Информация об авторе")
    about.geometry('260x260')
    about.resizable(False, False)
    myimage = ImageTk.PhotoImage(Image.open('anime.jpg'))
    label_image = tk.Label(about, image=myimage)
    label_image.pack()
    # Делаем дочернее окно модальным
    about.grab_set() # перехват событий, происходящих в приложении
    about.focus_set() # захват и удержание фокуса
    about.wait_window()
def read_file_history():
    """ Отображение истории вычислений """
    if not os.path.exists(storage_path):
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
    if rb_var.get() == 1:
        """ Скрытие элементов """
        entry_c.grid_remove()
        label_c.grid_remove()
    elif rb_var.get() == 0:
        """ Отображение элементов """
        entry_c.grid()
        label_c.grid()
    data_clear()

def popup(event):
    """ Определение выбора пункта контекстного меню """
    popupmenu.post(event.x_root, event.y_root)

def history_clear():
    """ Очистка многострочного текстового поля """
    answer = mb.askyesno(title="Подтверждение действия", message="Очистить историю?")
    if answer == True:
        text.delete(1.0, tk.END)

def data_clear():
    """ Очистка полей для ввода коэффициентов уравнения и Lable'v с ответами """
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    label_root['text'] = ''
    label_text['text'] = ''
    button_save['state'] = 'disable'
    button_clear['state'] = 'disable'

def run_solution():
    """ Считывание коэффициентов уравнения """
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if rb_var.get() == 0:
            c = float(entry_c.get())
    except ValueError:
        mb.showerror('Ошибка!', 'Проверьте значения коэффициентов уравнения!')
    except Exception:
        mb.showerror('Ошибка!', 'Непонятная ошибка.')
    else:
        if rb_var.get() == 1:
            equation_solution(0, a, b)
            label_text['text'] = "Уравнение: {0}x + {1} = 0".format(entry_a.get(), entry_b.get())
        else:
            label_text['text'] = "Уравнение: {0}x^2 + {1}x + {2} =0".format(entry_a.get(), entry_b.get(), entry_c.get())
            equation_solution(a, b, c)
    button_save['state'] = 'active'
    button_clear['state'] = 'active'

def equation_solution(a, b, c):
    """ Поиск корней линейного и квадратного уравнения """
    if a == 0:
        if b == 0:
            if c == 0:
                label_root['text'] = 'Корень - любое число.'
            else:
                label_root['text'] = 'Не имеет решений.'
        else:
            x = -c / b
            label_root['text'] = 'Корень: {0:6.2f}.'.format(x)
    else:
        d = b*b - 4*a*c
        if d > 0:
            x1 = (-b + d ** 0.5) / 2 / a
            x2 = (-b - d ** 0.5) / 2 / a
            label_root['text'] = 'Корни: {0:6.2f} и {1:6.2f}.'.format(x1, x2)
        else:
            if d == 0:
                x = -b / 2 / a
                label_root['text'] = 'Корень: {0:6.2f}.'.format(x)
            else:
                label_root['text'] = 'Не имеет решений.'

# Настройка окна
root = tk.Tk()
root.title("Решение уравнений")
root.geometry('300x270')
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
nb.add(frame1, text='Решение уравнения')
nb.add(frame2, text='Просмотр истории')
# Размещение виждетов на вкладке "Решение уравнения"
frame_koef = tk.LabelFrame(frame1, text="Укажите коэффициенты:")
frame_koef.grid(row=0, column=0, columnspan=2, padx=15, pady=5)
frame_type = tk.LabelFrame(frame1, text="Вид уравнения")
frame_type.grid(row=0, column=2, padx=5, pady=5)
frame_result = tk.Frame(frame1)
frame_result.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
frame_button = tk.Frame(frame1)
frame_button.grid(row=1, column=2, padx=5, pady=5)
tk.Label(frame_koef, text="a = ", font=("Comic Sans MS", 11, "bold"),
fg='#c21d4a').grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame_koef, text="b = ", font=("Comic Sans MS", 11, "bold"),
fg='#c21d4a').grid(row=1, column=0, padx=5, pady=5)
label_c = tk.Label(frame_koef, text="c = ", font=("Comic Sans MS", 11, "bold"), fg='#c21d4a')
label_c.grid(row=2, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_koef, width=10)
entry_a.grid(row=0, column=1, padx=5, pady=10)
entry_b = tk.Entry(frame_koef, width=10)
entry_b.grid(row=1, column=1, padx=5, pady=5)
entry_c = tk.Entry(frame_koef, width=10)
entry_c.grid(row=2, column=1, padx=5, pady=10)
rb_var = tk.BooleanVar()
rb_var.set(0)
rb_lin = tk.Radiobutton(frame_type, variable=rb_var, text='Линейное', value=1,
command=radiobutton_change)
rb_lin.grid(row=0, column=0, padx=5, pady=5)
rb_kv = tk.Radiobutton(frame_type, variable=rb_var, text='Квадратное', value=0,
command=radiobutton_change)
rb_kv.grid(row=1, column=0, padx=5, pady=5)
label_text = tk.Label(frame_result)
label_text.grid(row=0, column=0)
label_root = tk.Label(frame_result)
label_root.grid(row=1, column=0)
button_res = tk.Button(frame_button, width=12, text="Найти корни", command=run_solution)
button_res.grid(row=0, column=0, padx=5, pady=2, )
button_clear = tk.Button(frame_button, state='disabled', width=12, text="Очистить",
command=data_clear)
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
root.mainloop()
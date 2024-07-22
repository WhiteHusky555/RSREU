from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import nametofont
from idlelib.tooltip import Hovertip
from RAScal_5_INPUT import input_value
from RAScal_5_CONVERT import convert_value


def enable_choice():
    if convert_type.get() == 2 or convert_type.get() == 3:
        code_type.set(0)
        strcode.configure(state='normal')
        revcode.configure(state='normal')
        addcode.configure(state='normal')
        # codetask.grid(row=2, column=0 ,pady=[0, 20])
        # strcode.grid(row=2, column=1, pady=[0, 20], padx=20, sticky=EW)
        # revcode.grid(row=2, column=2, pady=[0, 20],padx=20, sticky=EW)
        # addcode.grid(row=2, column=3, pady=[0, 20],padx=20, sticky=EW)
    else:
        code_type.set(0)
        strcode.configure(state='disabled')
        revcode.configure(state='disabled')
        addcode.configure(state='disabled')
        # codetask.grid_forget()
        # strcode.grid_forget()
        # revcode.grid_forget()
        # addcode.grid_forget()


# ВЫВОД ОШИБКИ ИЛИ РЕЗУЛЬТАТОВ
def show_error(error_type):
    if error_type == '01':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели тип перевода.')
    elif error_type == '02':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели тип кода.')
    elif error_type == '03':
        messagebox.showerror(parent=window, title='Ошибка', message='Вы не ввели значение.')
    elif error_type == '10':
        messagebox.showerror(parent=window, title='Ошибка', message='Число должно содержать только '
                                                                    'десятичные цифры и '
                                                                    'одиночный знак + или - перед числом.')
    elif error_type == '11':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число не должно начинаться с нуля.')
    elif error_type == '12':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число должно быть целым.')
    elif error_type == '13':
        messagebox.showerror(parent=window, title='Ошибка', message='Ошибка. Число должно быть в диапазоне от '
                                                                    '-(2^63 - 1) до 2^63 - 1.')
    elif error_type == '20':
        messagebox.showerror(parent=window, title='Ошибка', message='Введены недопустимые символы.')
    elif error_type == '21':
        messagebox.showerror(parent=window, title='Ошибка', message='Превышена максимальная длина.')
        correct_input = False
    elif error_type == '22':
        messagebox.showerror(parent=window, title='Ошибка', message='Код не должен '
                                                                    'состоять меньше чем из двух символов ')
    elif error_type == '23':
        messagebox.showerror(parent=window, title='Ошибка', message='Обратный код не должен '
                                                                    'состоять только из единиц.')
    elif error_type == '24':
        messagebox.showerror(parent=window, title='Ошибка', message='Дополнительный код не должен '
                                                                    'состоять только из нулей.')
    elif error_type == '30':
        messagebox.showerror(parent=window, title='Ошибка', message='Введены недопустимые символы.')
    elif error_type == '31':
        messagebox.showerror(parent=window, title='Ошибка', message='Превышена максимальная длина.')
    elif error_type == '32':
        messagebox.showerror(parent=window, title='Ошибка', message='Обратный код не должен '
                                                                    'состоять только из единиц.')
    elif error_type == '33':
        messagebox.showerror(parent=window, title='Ошибка', message='Дополнительный код не должен '
                                                                    'состоять только из нулей.')


def show_result(result):
    table.delete(*table.get_children())
    if len(result) == 3:
        crutch = Label(window, text=result[0][1])
        crutch.grid(row=5, column=1, ipadx=10)
        window.update_idletasks()
        cell_size = crutch.winfo_width()
        pass
        crutch.destroy()
        results.grid(row=5, column=0)
        columns = ('1', '2', '3')
        table.config(columns=columns, show='headings', height=3)
        table.heading('1', text='', anchor='center')
        table.column('1', anchor='center', minwidth=103)
        table.heading('2', text='Двоичный', anchor='center')
        table.column('2', anchor='center', minwidth=cell_size, width=cell_size)
        table.heading('3', text='Шестнадцатеричный', anchor='center')
        table.column('3', anchor='center', minwidth=121)
    elif len(result) == 1:
        results.grid(row=5, column=0)
        columns = ('0', '1')
        table.config(columns=columns, show='headings', height=1)
        table.heading('0', text='Код', anchor='center')
        table.column('0', anchor='center')
        table.heading('1', text='Число', anchor='center')
        table.column('1', anchor='center')
    for data in result:
        table.insert('', END, values=data)
    table.pack(fill='x', expand=YES)
    res_frame.grid(row=5, column=1, columnspan=3, pady=[0,20], sticky=NSEW)


def input_convert_show():
    result_of_input = input_value(convert_type.get(), code_type.get(), valinput.get())
    if result_of_input[0]:
        results = convert_value(convert_type.get(), code_type.get(), valinput.get())
        show_result(results)
    else:
        show_error(result_of_input[1])


def refer():
    reference = Toplevel()
    x = window.winfo_x()
    y = window.winfo_y()
    reference.wm_geometry('+{}+{}'.format(x+window.winfo_width()//4, y))
    refer_label = Label(reference, text="А ВОТ И СПРАВКА")
    refer_label.pack(padx=100, pady=100)
    reference.grab_set()


window = Tk()
window.resizable(True, False)

window.title('RAScal 5')
icon = PhotoImage(file="RAScal-logo.png")
window.iconphoto(True, icon)
nametofont("TkHeadingFont").configure(size=10)
nametofont("TkDefaultFont").configure(size=10)

img = PhotoImage(file='ReferImage.png')
referimg = img.subsample(26, 26)
refer = Button(window, image=referimg, border=0, command=refer)
refer.grid(row=0, column=3, sticky=NE)
Hovertip(refer, text='Справка', hover_delay=500)

tips = ['Вид перевода:', 'Тип кода:', 'Значение:', 'Результаты:']
Label(window, text=tips[0]).grid(row=1, column=0)
codetask = Label(window, text=tips[1])
Label(window, text=tips[2], font='TkDefaultFont 10').grid(row=3, column=0)
results = Label(window, text=tips[3])

convert_type = IntVar()
code_type = IntVar()
code_type.set(0)
code_type.set(0)

todec = Radiobutton(window, text='Из десятичного числа\nв коды',
                    variable=convert_type, value=1, command=enable_choice, indicatoron=0)
bincdec = Radiobutton(window, text='Из двоичного кода\nв число',
                      variable=convert_type, value=2, command=enable_choice, indicatoron=0)
hexdec = Radiobutton(window, text='Из шестнадцатеричного кода\nв число',
                     variable=convert_type, value=3, command=enable_choice, indicatoron=0)

todec.grid(row=1, column=1, pady=20)
bincdec.grid(row=1, column=2)
hexdec.grid(row=1, column=3)

strcode = Radiobutton(window, text='Прямой код', indicatoron=0,
                      variable=code_type, value=1, state='disabled')
revcode = Radiobutton(window, text='Обратный код', indicatoron=0,
                      variable=code_type, value=2, state='disabled')
addcode = Radiobutton(window, text='Дополнительный код', indicatoron=0,
                      variable=code_type, value=3, state='disabled')

codetask.grid(row=2, column=0, pady=[0, 20])
strcode.grid(row=2, column=1, pady=[0, 20], sticky=EW)
revcode.grid(row=2, column=2, pady=[0, 20], sticky=EW)
addcode.grid(row=2, column=3, pady=[0, 20], sticky=EW)

valinput = Entry(window, borderwidth=1, relief='solid')
valinput.grid(row=3, column=1, sticky=NSEW, columnspan=3)

res_frame=Frame(window)
table=ttk.Treeview(res_frame)
# table = ttk.Treeview(height=3, columns=('1', '2', '3'), show='headings')
# results.grid(row=5, column=0)
# table.grid(row=5, column=1, columnspan=3, pady=[0,20], padx=[0,20])

submit = Button(window, text='Перевести', font="TkDefaultFont 11", command=input_convert_show)
submit.grid(row=4, column=2, sticky=NSEW, pady=20)

window.eval('tk::PlaceWindow . center')

window.mainloop()

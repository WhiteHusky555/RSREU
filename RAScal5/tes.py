from tkinter import *
from tkinter import ttk
import os


def show_result(result):
    table.delete(*table.get_children())
    if len(result) == 3:
        crutch = Label(window, text=result[0][1])
        crutch.grid(row=5, column=1, ipadx=10)
        window.update_idletasks()
        cell_size = crutch.winfo_width()
        pass
        crutch.destroy()
        columns = ('1', '2', '3')
        table.config(columns=columns, show='headings', height=3)
        table.heading('1', text='', anchor='center')
        table.column('1', anchor='center')
        table.heading('2', text='Двоичный', anchor='center')
        table.column('2', anchor='center', width=cell_size)
        table.heading('3', text='Шестнадцатеричный', anchor='center')
        table.column('3', anchor='center')
    elif len(result) == 1:
        columns = ('0', '1')
        table.config(columns=columns, show='headings', height=1)
        table.heading('0', text='Код', anchor='center')
        table.column('0', anchor='center')
        table.heading('1', text='Число', anchor='center')
        table.column('1', anchor='center')
    for data in result:
        table.insert('', END, values=data)


window = Tk()
table = ttk.Treeview(window)
for i in range(4):
    result = [[1,10*i,3], [1,2,3], [1,2,3]]
    show_result(result)
# label = Label(window, text='Шестнадцатеричный')
# label.grid(row=0, column=0, sticky=NSEW)
# window.update_idletasks()
# print(label.winfo_width())
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
frame = Frame(window)
frame.grid(row=0, column=0,sticky=NSEW)
button = Button(frame, text='ДДАДА')
button.pack(expand=True, fill='both')
window.mainloop()
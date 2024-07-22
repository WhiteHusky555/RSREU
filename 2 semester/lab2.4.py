from re import sub
from time import perf_counter_ns
def f1(x):
    for i in range(ord('A'), ord('Z')-1):
        a=chr(i)+chr(i+1)+chr(i+2)
        x=sub(a, '', x)
    return x

def f2(x):
    t=[]
    for i in range(len(x)-2):
        if (ord(x[i])) == (ord(x[i+1])-1) == (ord(x[i+2])-2) and str(x[i] + x[i+1] + x[i+2]).isupper():
            t.append(x[i:(i+3)])
    for i in t:
        x=x.replace(i, '')
    return x

st=str(input('Введите первую строку: '))
while st=='':
    st=str(input('Введите первую строку: '))
i = 2
while True:
    k = int(input('Введите 1 - для ввода следующей строки\n 2 - для окончания ввода: '))
    while k != 1 and k != 2:
        k = int(input(('Ошибка, повторите ввод: ')))
    if k==2:
        break
    else:
        st+='\n'
        sti=str(input(f'Введите {i}-ю строку: '))
        while sti=='':
            sti=str(input(f'Ошибка, введите {i}-ю строку: '))
        st+=sti
        i+=1
print(f'Эхо-вывод ввода\n{st}')

start_time = perf_counter_ns()
st1=f1(st)
end_time= perf_counter_ns()
print('Работа программы с использованием регулярных выражений языка')
print(f'Вывод обработанной строки: \n{st1}\nВремя выполнения {end_time-start_time} наносекунд')
start_time = perf_counter_ns()
st2=f2(st)
end_time= perf_counter_ns()
print('Работа программы без использования регулярных выражений языка')
print(f'Вывод обработанной строки: \n{st2}\nВремя выполнения {end_time-start_time} наносекунд')
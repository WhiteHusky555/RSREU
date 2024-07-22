from random import uniform
from time import perf_counter_ns
k=int(input('Введите 1 - для ввода одномерного массива с клавиатуры, 2 - для заполнения одномерного массива с помощью датчика псевдослучайных чисел: '))
while k!=1 and k!=2:
    k=int(input(('Ошибка, повторите ввод: ')))
while True:
    I=int(input('Введите количество строк матрицы: '))
    J=int(input('Введите количество столбцов матрицы: '))
    if I>1 and J>1:
        break
A=[[0]*J for i in range(I)]
if k==1:
    for i in range(I):
        for j in range(J):
            A[i][j]=(float(input(f'Ввод элемента №{i}-{j}: ')))
else:
    while True:
        a=float(input('Введите нижний предел случайного значения: '))
        b=float(input('Введите верхний предел случайного значения: '))
        if a>=b:
            print('Ошибка ввода')
        else:
            break
    for i in range(I):
        for j in range(J):
            A[i][j]=float(uniform(a, b))
print(f'Эхо-вывод массива')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in A[i]]}')
print(f'Размер матрицы - {I}x{J}')
start_time = perf_counter_ns()
for q in range(I):
    for i in range(J):
        for j in range(J-1-i):
            if A[q][j]>A[q][j+1]:
                A[q][j], A[q][j+1]=A[q][j+1], A[q][j]
c=0
for i in range(J):
    c+=A[1][i]
c/=J
end_time= perf_counter_ns()
print(f'Вывод работы подпрограммы без использования методов списка: ')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in A[i]]}')
print(f'Cреднее значение элементов 2-й строки = {"%.3f" % c}\n Bремя работы программы: {(end_time-start_time)} наносекунд')
start_time = perf_counter_ns()
for i in range(3):
    A[i].sort()
c=sum(A[1])/len(A[1])
end_time = perf_counter_ns()
print(f'Вывод работы подпрограммы с использованием методов списка: ')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in A[i]]}')
print(f'Cреднее значение элементов 2-й строки = {"%.3f" % c}\n Bремя работы программы: {(end_time-start_time)} наносекунд')

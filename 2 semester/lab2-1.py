from random import uniform
from copy import deepcopy
from time import perf_counter_ns
def f1(A):
    min1=A[0]
    for x in A:
        if min1>x:
            min1=x
    min2=A[0]
    if min2==min1:
        min2=A[1]
    for x in A:
        if min2>x and x!=min1:
            min2=x
    flag=True
    B=[float(0)]*r
    q=0
    for x in A:
        if x == min1 or x == min2:
            B[q] = x
            q += 1
            flag = not (flag)
        elif flag == True:
            B[q] = x
            q += 1

    return B[:q]

def f2(A):
    B = deepcopy(A)
    B.sort()
    min1 = B[0]
    min2 = B[1]
    imin1 = A.index(min1)
    imin2 = A.index(min2)
    if imin1 < imin2:
        C= (A[:(imin1 + 1)] + A[imin2:])
    else:
        C= (A[:(imin2 + 1)] + A[imin1:])
    return C

    
k=int(input('Введите 1 - для ввода одномерного массива с клавиатуры, 2 - для заполнения одномерного массива с помощью датчика псевдослучайных чисел: '))
while k!=1 and k!=2:
    k=int(input(('Ошибка, повторите ввод: ')))
r=int(input('Введите количество элементов в массиве: '))
while r<=2:
    r=int(input(('Ошибка, повторите ввод количества элементов в массиве:')))
while True:
    An= [0] * r
    if k==1:
        for i in range(0, r, 1):
            An[i]=(float(input(f'Ввод элемента №{i}: ')))
    else:
        while True:
            a=float(input('Введите нижний предел случайного значения: '))
            b=float(input('Введите верхний предел случайного значения: '))
            if a>=b:
                print('Ошибка ввода')
            else:
                break
        for i in range(0, r, 1):
            An[i]=round(float(uniform(a, b)), 3)
    A = []
    for x in An:
        if x not in A:
            A.append(x)
        else:
            r-=1
    if r<=2:
        r = int(input(('Ошибка, повторите ввод количества элементов в массиве:')))
    else:
        break
print(f'Эхо-вывод массива\n{A}\nРазмер одномерного массива - {r}')
start_time = perf_counter_ns()
C1=f1(A)
end_time= perf_counter_ns()
print(f'Вывод работы подпрограммы без использования методов списка: \n {C1} \n Bремя работы программы: {(end_time-start_time)/10e6} миллисекунд')
start_time = perf_counter_ns()
C2 = f2(A)
end_time = perf_counter_ns()
print(f'Вывод работы подпрограммы с использованием методов списка: \n {C2} \n Bремя работы программы: {(end_time - start_time) / 10e6} миллисекунд')


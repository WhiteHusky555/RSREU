from random import randint
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
            A[i][j]=(randint(a, b))
print(f'Эхо-вывод массива')
for i in range(0, I):
   print(f'{[a for a in A[i]]}')
print(f'Размер матрицы - {I}x{J}')
B=[[0]*J for i in range(I)]
minA=A[0][0]
for i in range(I):
    for j in range(J):
        if minA>A[i][j]:
            minA=A[i][j]
for i in range(I):
    match i%3:
        case 0:
            w=0
            for j in range(J):
                if abs(A[i][j])%2==1:
                    B[i][w]=A[i][j]
                    w+=1
            for j in range(w, J):
                B[i][j]=minA
        case 1:
            w=0
            for j in range(J):
                if abs(A[i][j])%2==0:
                    B[i][w]=A[i][j]
                    w+=1
            for j in range(w, J):
                B[i][j]=minA
        case _:
            w=0
            for j in range(J):
                if A[i][j]>0:
                    B[i][w]=A[i][j]
                    w+=1
                for j in range(w, J):
                    B[i][j] = minA
for i in range(I):
    print(B[i])
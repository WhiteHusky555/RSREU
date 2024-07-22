from random import uniform
def fB(A):
    B=[[0]*len(A[i]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            B[i][j]=int(A[i][j])
    return B

def fC(A):
    C = [[0] * len(A[i]) for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[i])):
            C[i][j] = abs((A[i][j]))%1
    for i in range(len(A)):
        C[i]=sorted(C[i], reverse=bool(((i))%2==1))
    return C

def fZ(B):
    Z=[[0] * len(B[i]) for i in range(len(B))]
    for i in range(len(B)):
        for j in range(len(B[i])):
            if (((i)%2==0 and B[i][j]%2==0) or ((i)%2==1 and B[i][j]%2==1)):
                Z[i][j]=B[i][j]
    return Z

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
            A[i][j]=(float(input(f'Ввод элемента A №{i}-{j}: ')))
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
print(f'Эхо-вывод массива A')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in A[i]]}')
B=fB(A)
print(f'Эхо-вывод массива B')
for i in range(0, I):
   print(f'{[a for a in B[i]]}')
C=fC(A)
print(f'Эхо-вывод массива C')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in C[i]]}')
Z=fZ(B)
print(f'Эхо-вывод массива Z')
for i in range(0, I):
   print(f'{[a for a in Z[i]]}')


from random import uniform
from numpy import zeros, transpose, array
from numpy.linalg import matrix_power


def Minor(A,i,j):
    return [list(x[:j]) + list(x[j+1:]) for x in ((A[:i])+(A[i+1:]))]
def Det(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    det = 0
    for c in range(len(m)):
        det += ((-1)**c)*m[0][c]*Det(Minor(m,0,c))
    return det

def invert(m):
    det = Det(m)
    if len(m) == 2:
        return [[m[1][1]/det, -1*m[0][1]/det],
                [-1*m[1][0]/det, m[0][0]/det]]
    lin_dop = []
    for r in range(len(m)):
        lin_dop_str = []
        for c in range(len(m)):
            minor = Minor(m,r,c)
            lin_dop_str.append(((-1)**(r+c)) * Det(minor))
        lin_dop.append(lin_dop_str)
    lin_dop = trans(lin_dop)
    for r in range(len(lin_dop)):
        for c in range(len(lin_dop)):
            lin_dop[r][c] = lin_dop[r][c]/det
    return lin_dop

def trans(A):
    C=zeros((I, I), 'float')
    for i in range(I):
        for j in range(I):
            C[i][j] = A[j][i]
    return C
def mathmultip(A, B):
    C=zeros((I, I), 'float')
    for i in range(I):
        for j in range(I):
            for k in range(I):
                C[i][j]+=A[i][k]*B[k][j]
    return C

k=int(input('Введите 1 - для ввода одномерного массива с клавиатуры, 2 - для заполнения одномерного массива с помощью датчика псевдослучайных чисел: '))
while k!=1 and k!=2:
    k=int(input(('Ошибка, повторите ввод: ')))
while True:
    I=int(input('Введите размер матрицы: '))
    if I>1:
        break
A=zeros((I, I), 'float')
B=zeros((I, I), 'float')
if k==1:
    for i in range(I):
        for j in range(I):
            A[i][j]=(float(input(f'Ввод элемента A №{i}-{j}: ')))
            B[i][j]=(float(input(f'Ввод элемента B №{i}-{j}: ')))
else:
    while True:
        a=float(input('Введите нижний предел случайного значения: '))
        b=float(input('Введите верхний предел случайного значения: '))
        if a>=b:
            print('Ошибка ввода')
        else:
            break
    for i in range(I):
        for j in range(I):
            A[i][j]=float(uniform(a, b))
            B[i][j] = float(uniform(a, b))
print(f'Эхо-вывод массива A')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in A[i]]}')
print(f'Размер матрицы - {I}x{I}')
print(f'Эхо-вывод массива B')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in B[i]]}')
print(f'Размер матрицы - {I}x{I}')

A, B = list(A), list(B)
С=mathmultip(A, A) + invert(B) * trans(A) - B
print(f'Вывод работы подпрограммы без использования методов списка: ')
print('Вывод массива C')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in С[i]]}')

C=matrix_power(A, 2) - matrix_power(B, -1) * transpose(A) - B
print(f'Вывод работы подпрограммы c использованием методов списка: ')
print('Вывод массива C')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in C[i]]}')

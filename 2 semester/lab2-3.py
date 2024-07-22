from random import uniform
from time import perf_counter_ns
from numpy import zeros, matmul, transpose, diagonal, fliplr, argmax, argmin
from numpy.linalg import matrix_power

def max_min_diag(A):
    max_diag=max(diagonal(A))
    min_diag=min(fliplr(A).diagonal())
    return max_diag, min_diag
def min_max_diag_no_numpy(A):
    max_diag=A[0][0]
    for i in range(1, I):
        if max_diag<A[i][i]:
            max_diag=A[i][i]
    min_diag=A[I-1][0]
    for i in range(I-1, 0, -1):
        if min_diag>A[i][I-i]:
            min_diag=A[i][I-i]
    return max_diag, min_diag
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
X=zeros((I, I), 'float')
Y=zeros((I, I), 'float')
if k==1:
    for i in range(I):
        for j in range(I):
            X[i][j]=(float(input(f'Ввод элемента X №{i}-{j}: ')))
            Y[i][j]=(float(input(f'Ввод элемента Y №{i}-{j}: ')))
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
            X[i][j]=float(uniform(a, b))
            Y[i][j] = float(uniform(a, b))
print(f'Эхо-вывод массива X')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in X[i]]}')
print(f'Размер матрицы - {I}x{I}')
print(f'Эхо-вывод массива Y')
for i in range(0, I):
   print(f'{[ "%.3f" % a for a in Y[i]]}')
print(f'Размер матрицы - {I}x{I}')

start_time = perf_counter_ns()
Z=mathmultip(X, X) + mathmultip(trans(X), Y) + mathmultip(trans(X), trans(Y))
U=mathmultip(X, X) - mathmultip(mathmultip(Z, Z), Z)
C=zeros((8, 1), 'float')
C[0], C[1]=min_max_diag_no_numpy(X)
C[2], C[3]=min_max_diag_no_numpy(Y)
C[4], C[5]=min_max_diag_no_numpy(Z)
C[6], C[7]=min_max_diag_no_numpy(U)
max_in_C=C[0][0]
min_in_C=C[0][0]
for i in range(8):
    if max_in_C<C[i]:
        max_in_C=C[i]
for i in range(8):
    if max_in_C==C[i]:
        index_max_in_C=i
for i in range(8):
    if min_in_C>C[i]:
        min_in_C=C[i]
for i in range(8):
    if min_in_C==C[i]:
        index_min_in_C=i
C[index_max_in_C], C[index_min_in_C] = C[index_min_in_C], C[index_max_in_C]
end_time= perf_counter_ns()
print(f'Вывод работы подпрограммы без использования методов списка: ')
print('Вывод массива Z')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in Z[i]]}')
print('Вывод массива U')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in U[i]]}')
print(f'Вывод массива С, состоящего из максимальных элементов главных диагоналей и минимальных - вспомогательных диагоналей \n {[ "%.3f" % a for a in C]}\n Bремя работы программы: {(end_time-start_time)} наносекунд')

start_time = perf_counter_ns()
Z= matrix_power(X, 2) + matmul(transpose(X), Y) + matmul(transpose(X), transpose(Y))
U= matrix_power(X, 2) - matrix_power(Z, 3)
C=zeros((8, 1), 'float')
C[0], C[1]=max_min_diag(X)
C[2], C[3]=max_min_diag(Y)
C[4], C[5]=max_min_diag(Z)
C[6], C[7]=max_min_diag(U)
C[argmax(C)], C[argmin(C)] = C[argmin(C)], C[argmax(C)]
end_time = perf_counter_ns()
print(f'Вывод работы подпрограммы с использованием методов списка: ')
print('Вывод массива Z')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in Z[i]]}')
print('Вывод массива U')
for i in range(0, I):
    print(f'{[ "%.3f" % a for a in U[i]]}')
print(f'Вывод массива С, состоящего из максимальных элементов главных диагоналей и минимальных - вспомогательных диагоналей \n {[ "%.3f" % a for a in C]}\n Bремя работы программы: {(end_time-start_time)} наносекунд')
from random import randint
def is_a_number(numb_str):
    for symbol in numb_str:
        if symbol not in '1234567890-':
            return False
    return True
def is_prime(a):
    k=0
    a=int(a)
    for i in range(2, abs(a) // 2 + 1):
        if (abs(a) % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    else:
        return False

def check_palindrome(n):
    n=str(n)
    ln=len(n)
    return (n[:ln // 2] == n[ln:(ln + 1) // 2 - 1:-1])


def palindrome_list(A):
    B=[[] for i in range(I)]
    for i in range(I):
        for j in range(J):
            if check_palindrome(A[i][j]):
                B[i]+=[A[i][j]]
        B[i]=set(B[i])
    return B

def prime_list(A):
    B=[[] for i in range(I)]
    for i in range(I):
        for j in range(J):
            if is_prime(A[i][j]):
                B[i]+=[A[i][j]]
    for i in range(I):
        B[i]=set(B[i])
    return B

def list_intersection(B, C):
    Z = [[] for i in range(I)]
    for i in range(I):
        Z[i]=set(B[i]).intersection(set(C[i]))
    return Z


k=int(input('Введите 1 - для ввода одномерного массива с клавиатуры, 2 - для заполнения одномерного массива с помощью датчика псевдослучайных чисел: '))
while k!=1 and k!=2:
    k=int(input(('Ошибка, повторите ввод: ')))
while True:
    I=str(input('Введите количество строк матрицы: '))
    J=str(input('Введите количество столбцов матрицы: '))
    if (is_a_number(I) and is_a_number(J)) and int(I)>1 and int(J)>1:
        I, J=int(I), int(J)
        break
A=[[0]*J for i in range(I)]
if k==1:
    for i in range(I):
        for j in range(J):
            while True:
                A[i][j]=(str(input(f'Ввод элемента A №{i+1}-{j+1}: ')))
                if is_a_number(A[i][j]) == bool(True):
                    break
else:
    while True:
        a = str(input('Введите нижний предел случайного значения: '))
        b = str(input('Введите верхний предел случайного значения: '))
        if a>=b or (is_a_number(a) and is_a_number(b)) == False:
            print('Ошибка ввода')
        else:
            break
    for i in range(I):
        for j in range(J):
            A[i][j]=int(randint(int(a), int(b)))
print(f'Эхо-вывод массива A')
for i in range(0, I):
   print(f'{[a for a in A[i]]}')
print('Палиндромы')
B=palindrome_list(A)
for i in range(0, I):
   print(f'{[a for a in B[i]]}')
print('Простые')
C=prime_list(A)
for i in range(0, I):
   print(f'{[a for a in C[i]]}')
print('Пересечение')
Z=list_intersection(B, C)
for i in range(0, I):
   print(f'{[a for a in Z[i]]}')
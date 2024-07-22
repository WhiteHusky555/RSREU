from math import sin, cos, exp
def f1(x):
    return (sin(x)+cos(x))/(2+sin(x)*sin(x))
def f2(x):
    return (exp(x)+exp(-x))/(3+cos(x))
def OIf1(a, b, n):
    flag=1
    if a==b:
        return 0
    else:
        if a>b:
            flag=-1
        sm=0
        h=abs(b-a)/n
        x=a+h
        for i in range(1, n):
            sm+=f1(x)
            x+=h
        return flag*(abs(b-a)/(2*n)) * (f1(a)+f1(b)+2*sm)
def OIf2(a, b, n):
    flag=1
    if a==b:
        return 0
    else:
        if a>b:
            flag=-1
        sm=0
        h=abs(b-a)/n
        x=a+h
        for i in range(1, n):
            sm+=f2(x)
            x+=h
        return flag*(abs(b-a)/(2*n)) * (f2(a)+f2(b)+2*sm)

k=int(input('Введите 1 для нахождения ОИ функции (sin(x)+cos(x))/(2+sin(x)*sin(x))\n Введите 2 для нахождения ОИ функции (exp(x)+exp(-x))/(3+cos(x))\nВвод: '))
while k!=1 and k!=2:
    k=int(input('Повторите ввод: '))
while True:
    a = float(input('Введите нижний предел интегрирования: '))
    b = float(input('Введите верхний предел интегрирования: '))
    if a > b:
        print('Ошибка ввода')
    else:
        break
while True:
    n=int(input('Выберите точность вычисления: 1 - для 1.000 отрезков разбиения, 2 - для 10.000 отрезков разбиения, 3 - для 100.000 отрезков разбиения\n'))
    match n:
        case 1:
            n=1000
            break
        case 2:
            n=10000
            break
        case 3:
            n=100000
            break
        case _:
            pass
if k==1:
    print(OIf1(a, b, n))
else:
    print(OIf2(a, b, n))
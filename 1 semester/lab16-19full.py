def iterations(a,b): # метод итераций
    from math import log, exp
    def f(x):
        return x**3/2-log(abs(x))-1
    def fi(x):
        if x>1:
            return (2+2*log(abs(x)))**(1/3)
        elif x>0:
            return exp(((x**3)/2)-1)
        return -exp(((x**3)/2)-1)
    eps=1e-3
    x=(a+b)/2
    count = 0
    while True:
        print(x, f(x))
        count+=1
        xp=x
        x=fi(x)
        if abs(xp-x)>eps:
            continue
        else:
            break
    return xp, count

def pol(a, b): # метод половинного деления
    def f(x):
        return (pow(x, 3) / 2) - log(abs(x)) - 1
    from math import log
    eps = 1e-3
    count = 0
    while abs(b - a) >= eps:
        count += 1
        x = (a + b) / 2
        print(x, f(x))
        z = (a + b) / 2
        if f(z) * f(a) < 0:
            b = z
        else:
            a = z
    x = (a + b) / 2
    return x,count

def newton(a,b): # метод Ньютона
    from math import log
    eps=1e-3
    error=False
    if (a**3/2-log(abs(a))-1)*(3*a+1/a**2)>0:
        x=a
    elif (b**3/2-log(abs(b))-1)*(3*b+1/b**2)>0:
        x=b
    else:
        error=True
        print("ошибка")
    if not error:
        count = 0
        while True:
            print(x, x**3/2-log(abs(x))-1)
            h=(x**3/2-log(abs(x))-1)/(3/2*x-1/x)
            x=x-h
            count+=1
            if abs(h)<eps:
                break
        return x, count

def chords(a,b): # метод хорд
    from math import log
    def f(x):
        return (x*x*x)/2-log(abs(x))-1
    eps=1e-3
    ya=f(a)
    yb=f(b)
    x=a
    count=0
    while True:
        count+=1
        print(x, f(x))
        x=a-((b-a)/(yb-ya)) *ya
        y=f(x)
        if y*ya<0:
            b=x
            yb=y
        else:
            a=x
            ya=y
        if abs(f(x))<eps:
            break
    return x, count

def straigt(a): # прямой метод
    from math import log
    def f(x):
        return x**3/2-log(abs(x))-1
    eps=1e-3
    b=a+eps
    count=0
    while f(a)*f(b)>0:
        count+=1
        a=a+eps
        b=b+eps
    x=(a+b)/2
    return x, count
# Цель: определить интервал в котором лежит только один корень
# и уточнить его значение с помощью выбранного метода с точностью 1e-3
# Дата написания: 25.11.2023
# Программисты: Мыльников Р. В., Набатчиков А. В.
# Наумов П. В., Непрокин И. С., Прасолов М. Г.
# a, bn - границы поиска интервала, содержащего только 1 корень
# h - шаг поиска
# a, b - границы интервала, содержащего только 1 корень
# method_number - номер выбранного пользователем метода
# x - искомое значение корня
# count - количество итераций совершённых при выполнении метода

from math import log
import method

def f(x):
    return (pow(x, 3) / 2) - log(abs(x)) - 1


# ПЕРВЫЙ ЭТАП (определение интервала):
a = float(input('Введите левую границу области поиска: '))
bn = float(input('Введите правую границу области поиска: '))
h = float(input('Введите шаг поиска: '))
b = a + h
while ((f(a) * f(b)) > 0) and (b < (bn + h / 2)):
    a = a + h
    b = b + h
if b > (bn + h / 2):
    print('На заданном интервале нет корней')
    exit()

# ВТОРОЙ ЭТАП (уточнение значения с точностью 1e-3)
print(f'Корень лежит в интервале от {a} до {b}')
method_number = input("Введите номер желаемого метода уточнения:\n"
                      "1) Метод итераций\n"
                      "2) Метод половинного деления\n"
                      "3) Метод Ньютона\n"
                      "4) Метод хорд\n"
                      "5) Метод прямого вычисления\n"
                      "Номер: ")
match method_number:
    case '1':  # Метод итераций
        x, count = method.iterations(a, b)
    case '2':  # Метод половинного деления
        x, count = method.pol(a, b)
    case '3':  # Метод Ньютона
        x, count = method.newton(a, b)
    case '4':  # Метод хорд
        x, count = method.chords(a, b)
    case '5':  # Метод прямого вычисления
        x, count = method.straigt(a)
    case _:
        print('Ошибка. Введено некорректное значение.')
        exit()
print(f'Корень {x}; Количество итераций: {count}')

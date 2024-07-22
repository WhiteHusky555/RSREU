#Цель: табулирование данной функции y=f(x), где х = a*b^2 - sin(b^2) +m*b с помощью оператора цикла с постусловием
#Переменные:
#a0 (float) – вводимое начальное значение х0
#an (float) – вводимое конечное значение xn
#ax (float) – вводимое значение шага функции
#m (float) – вводимое значение m
#b (float) – вводимое значения b
#a (float) – промежуточные a между значениями a0 и an (a=a0(ax)an)#Константы: pi, e (из exp)
#Метод: ввод функции пользователя для вычисления значения f(x), использование кодировки Unicode для вызова символов псевдографики
#Программист: Непрокин И.С.
#Дата написания: 17.10.2023
from math import sin, exp, pi
def f(x):
    if x>pi:
        r=1 - (exp(-a * x)) * sin(a * x + b)
        #print('1-(exp(-'+'('+str(a)+')'+'*'+'('+str(x)+')))'+'*'+'sin('+'('+str(a)+')'+'*'+'('+str(x)+')'+'+'+'('+str(b)+'))'+'='+str(r))
        return round(1 - (exp(-a * x)) * sin(a * x + b), 5)
    elif -pi<=x<=pi:
        r=1-(exp(-a*x))*(a*x+b)
        #print('1-(exp(-'+'('+str(a)+')'+'*'+'('+str(x)+')))'+'*'+'('+'('+str(a)+')'+'*'+'('+str(x)+')'+'+'+'('+str(b)+'))'+'='+str(r))
        return round(1-(exp(-a*x))*(a*x+b), 5)
    else:
        r=1-((exp(-a*x))+exp(-b*x))
        #print('1-(exp('+'-'+'('+str(a)+')'+'*'+'('+str(b)+'))'+'+exp('+'-'+'('+str(b)+')'+'*'+'('+str(x)+')))'+str(r))
        return round(1-((exp(-a*x))+exp(-b*x)), 5)

a0=float(input('Введите начальное значение a0: '))
an=float(input('Введите конечное значение an: '))
ax=float(input("Введите шаг функции ax: "))
m=float(input('Введите m: '))
b=float(input('Введите b: '))
if ((an>a0 and ax>0) or (an<a0 and ax<0)):
    a = round(a0, 5)
    print(chr(9484)+chr(9472)*int(20)+chr(9516)+chr(9472)*int(20 )+chr(9516)+chr(9472)*int(20)+chr(9488))
    print(chr(9474)+'F(x)'+' '*int(20-len('F(x)'))+chr(9474)+'x'+' '*int(20-len('x'))+chr(9474)+'a'+' '*int(20-len('a'))+chr(9474))
    while True:
        x=a*b*b-sin(b*b)+m*b
        print(chr(9500) + chr(9472) * 20 + chr(9532) + chr(9472) * 20 + chr(9532) + chr(9472) * 20 + chr(9508))
        print(chr(9474) + str(f(x)) + ' ' * (20 - len(str(f(x)))) + chr(9474)+str(round(x, 5)) + ' ' * (20 - len(str(round(x, 5))))
              +chr(9474) + str(round(a, 5)) + ' ' * (20 - len(str(round(a, 5)))) + chr(9474))
        #print('('+str(a)+')'+'*'+'('+str(b)+')'+'*'+'('+str(b)+')'+'+'+'sin('+'('+str(b)+')'+'*'+'('+str(b)+')'+')'+'+'+'('+str(m)+')'+'*'+'('+str(b)+')'+'='+str(x))
        t=f(x)
        a=round(a+ax, 5)
        if ((a>an) and ax>0) or ((a<an) and ax<0):
            print(chr(9492) + chr(9472) * 20 + chr(9524) + chr(9472) * 20 + chr(9524) + chr(9472) * 20 + chr(9496))
            break
else:
    print('Ошибка ввода')


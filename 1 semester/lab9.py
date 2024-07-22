#Цель: табулирование данной функции y=f(x), где х = a*b^2 - sin(b^2) +m*b с помощью оператора цикла с параметром
#Переменные:
#a0 (float) – вводимое начальное значение х0
#an (float) – вводимое конечное значение xn
#ax (float) – вводимое значение шага функции
#m (float) – вводимое значение m
#b (float) – вводимое значения b
#a (float) – промежуточные a между значениями a0 и an (a=a0(ax)an)#Константы: pi, e (из exp)
#Na (integer) - количество повторений цикла
#i (integer) - параметр цикла
#Метод: Ввод пользовательской функции для расчёта значения f(x), расчёт количества повторений цикла
# Na= абсолютная целая часть от |(an-a0)/ax| + 1, использование кодировки Unicode для вызова символов псевдографики.
#Программист: Непрокин И.С.
#Дата написания: 17.10.2023
from math import sin, exp, pi
def f(x):
    if x>pi:
        return round(1-(exp(-a*x))*sin(a*x+b), 7)
    elif -pi<=x<=pi:
        return round(1-(exp(-a*x))*(a*x+b), 7)
    else:
        return round(1-((exp(-a*x))+exp(-b*x)), 7)

a0=float(input('Введите начальное значение a0: '))
an=float(input('Введите конечное значение an: '))
ax=float(input("Введите шаг функции ax: "))
m=float(input('Введите m: '))
b=float(input('Введите b: '))
if ((an>a0 and ax>0) or (an<a0 and ax<0)):
    a = round(a0, 5)
    Na=(int(abs((an-a0)//ax)+1))
    print(chr(9484)+chr(9472)*int(20)+chr(9516)+chr(9472)*int(20 )+chr(9516)+chr(9472)*int(20)+chr(9488))
    print(chr(9474)+'F(x)'+' '*int(20-len('F(x)'))+chr(9474)+'x'+' '*int(20-len('x'))+chr(9474)+'a'+' '*int(20-len('a'))+chr(9474))
    for i in range(1, Na+1):
        x = a * b * b - sin(b * b) + m * b
        print(chr(9500) + chr(9472) * 20 + chr(9532) + chr(9472) * 20 + chr(9532) + chr(9472) * 20 + chr(9508))
        print(chr(9474) + str(f(x)) + ' ' * (20 - len(str(f(x)))) + chr(9474)+str(round(x, 5))
              + ' ' * (20 - len(str(round(x, 5))))+chr(9474) + str(round(a, 5)) + ' ' * (20 - len(str(round(a, 5)))) + chr(9474))
        a=round(a+ax, 5)
    print(chr(9492) + chr(9472) * 20 + chr(9524) + chr(9472) * 20 + chr(9524) + chr(9472) * 20 + chr(9496))
else:
    print('Ошибка ввода')


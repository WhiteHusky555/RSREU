#Программа нахождения значений y и z
from math import log, e #Импортируем log и e из библиотеки math
a = float(input('Введите значение а: ')) #Вводим значение а с клавиатуры
b = float(input('Введите значение b: ')) #Вводим значение b с клавиатуры
x = float(input('Введите значение x: ')) #Вводим значение x с клавиатуры, где x>0 и x!=-3.4*10**(-3)
z = log(x**2) - e**(a*x+b) + (x+2.3*10**(-3))/(x+3.4*10**(-3)) #Вычисляем значение z по формуле для выбранных a, b, x, где z!=-1
y= (a*(x**2)+b)/(a*(x**5)+b**2)+log(abs(1+z**3)) #Вычисляем значение y по формуле для выбранных a, b, x и найденного z
print(f'При a='+ str(a) + ', b='+ str(b)+', x='+ str(x)) #Выводим значения с округлением до 3 знака после запятой
print(f'y='+str(round(y, 3))+', z='+str(round(z, 3)))
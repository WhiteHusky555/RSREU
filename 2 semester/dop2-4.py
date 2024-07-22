import re
def count_digits(x):
    len_digits=0
    abc='1234567890'
    for i in str(x):
        if i in abc:
            len_digits+=1
    return len_digits
def count_liters(x):
    len_chars=0
    abc='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    for i in str(x):
        if i in abc:
            len_chars+=1
    return len_chars

s=str(input('Введите строку: '))
S1=list(re.split(r'(?<=\w[.!?]) ', s)) #текст на предложения
S2='' #числовые х2 = слова
S3='' #другие последовательности> числа+слова
for x in S1: #беру одно предложение
    len_digits=0
    len_chars=0
    len_else=0
    for i in x.split(' '): #делю предложение на слова (последовательности)
        if len(i)==count_digits(i):
            len_digits+=1
        elif len(i)==count_liters(i) or ((len(i)-1)==count_liters(i) and (i[-1] in '.!?')):
            len_chars+=1
        else:
            len_else+=1
    if len_digits==len_chars*2:
        S2+=x+' '
    if len_else>(len_digits+len_chars):
        S3+=x+' '+x+' '
print(f'S2 - список предложений, где последовательностей чисел в 2 раза больше последовательностей букв: \n{S2}')
print(f'S3 - список предложений, где суммарное количество последовательностей чисел и букв меньше количества последовательностей других символов: \n{S3}')
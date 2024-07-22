import string
def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))
def z(x, y):
    if sorted(str(x).lower())==sorted(str(y).lower()):
        return True
    else:
        return False

stroka=str(input())
stroka=remove_punctuation(stroka)
print(stroka)
list_sl=stroka.split(' ')
list_sl0=stroka.split(' ')
print(list_sl)
I=len(list_sl)
Y=len(list_sl)
for i in list_sl:
    for y in list_sl:
        if i==y:
            list_sl.remove(y)
        if i==(y[0].upper() + y[1:]):
            list_sl.remove(i)
print(list_sl)

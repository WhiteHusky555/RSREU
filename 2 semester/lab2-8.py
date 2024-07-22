while True:
    i = int(input("Введите количество элементов в словаре: "))
    if i>=2:
        break
dictionary_1 = {chr(ord('a')+a): 400-100*(a-1) for a in range(0, i)}
print(f'Эхо-вывод словаря:\n{dictionary_1}')
# Разбиваем словарь на два словаря
dictionary_2 = dict(list(dictionary_1.items())[:len(dictionary_1)//2])
dictionary_3 = dict(list(dictionary_1.items())[len(dictionary_1)//2:])
# Удаляем по одному элементу из каждого словаря
dictionary_2.popitem()
dictionary_3.popitem()
print("Словарь 2:", dictionary_2)
print("Словарь 3:", dictionary_3)
from random import randint
set_of_all=['Хлеб', 'Булки', 'Баранки', 'Сахар', 'Чай', 'Кофе', 'Какао', 'Сода', 'Масло', 'Соль', 'Макароны', 'Крупа', 'Бобы', 'Кисель', 'Карамель', 'Конфеты', 'Шоколад', 'Печенье', 'Пряники', 'Вафли', 'Консервы', 'Сок', 'Компот', 'Повидло', 'Джемы', 'Конфитюр', 'Варенье', 'Соусы', 'Сыр', 'Маргарин', 'Сало', 'Рыба', 'Мясо']
while True:
    k_m=int(input('Введите количество магазинов: '))
    if k_m>=1:
        break
shops=[[0]*randint(1, 10) for i in range(k_m)]
for i in range(len(shops)):
    for j in range(len(shops[i])):
        shops[i][j]=set_of_all[randint(0, 32)]
for i in range(len(shops)):
    shops[i]=set(shops[i])

print('Эхо-вывод номенклатуры товаров в магазинах')
for i in range(len(shops)):
    print(f'{i+1}-й магазин:\n{shops[i]}')
while True:
    k_t=int(input('Введите количество товаров: '))
    if k_t>=1:
        break
set_of_user=[0]*k_t
for i in range(k_t):
    set_of_user[i]=str(input(f'Введите {i+1}-й товар, представленный в номенклатуре товаров в магазинах:\n'))
while True:
    k_b=int(input('Введите количество магазинов, к которым имеет доступ покупатель:\n'))
    if k_b>=1 and k_b<= k_m:
        break
set_of_user=set(set_of_user)
shops_b=set()
for i in range(k_b):
    shops_b= shops_b | shops[i]
if set_of_user.intersection(shops_b) == set_of_user:
    print('Покупатель сможет приобрести все товары, используя маршруты городского транспорта')
else:
    print('Покупатель не сможет приобрести все товары, используя маршруты городского транспорта')
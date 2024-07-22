from datetime import date
from prettytable import PrettyTable
tabl = PrettyTable(['id', 'Адрес', 'Метраж в м^2', 'Цена за м^2', 'Стоимость', 'Дата выставления на продажу', 'Время нахождения в продаже'])
tabl = PrettyTable(title='Агенство', min_table_width=0)
def menu():
    print()
    print('  МЕНЮ:  '.center(38, "*"))
    print('1. Просмотр всех записей в базе данных')
    print('2. Добавление объекта')
    print('3. Удаление объекта по id')
    print('4. Вычисление покупки квартир')
    print('5. Завершение работы с базой данных\n')
    n = int(input("Выберите пункт меню для продолжения:"))
    return n

def pokypka(kolvo, minm2, maxm2, money):
    list_price=[]
    for name, info in dict.items():
        if minm2<=info['метраж (м^2)']<=maxm2 and info['стоимость']!= '-':
            list_price=list_price+[[name, info['стоимость'], info['метраж (м^2)']]]
            list_price.sort(key = lambda x: x[1])
    if kolvo>len(list_price):
        print('Желаемое количество квартир превышает доступное количество')
    money_from_list=0
    for i in range(kolvo):
            money_from_list+=float(list_price[i][1])
    if money<money_from_list:
        print('Покупка по заданным параметрам невозможна')
    else:
        tabl = PrettyTable(title='Агенство', min_table_width=0)
        tabl.clear()
        tabl.field_names = ['id', 'Адрес', 'Метраж в м^2', 'Стоимость', 'Продавец', 'Дата выставления на продажу',
                            'Время нахождения в продаже']
        for name, info in dict.items():
            for i in range(kolvo):
                if name==list_price[i][0]:
                        tabl.add_row([name, info['адрес'], info['метраж (м^2)'], info['стоимость'], info['продавец'],
                                      info['дата выставления на продажу'], info['время нахождения в продаже']])
        print(tabl)


def input_datesell():
    while True:
        year=int(input('Введите год выставления на продажу: '))
        months=int(input('Введите месяц выставления на продажу (число): '))
        day=int(input('Введите день выставления на продажу (число): '))
        if 1<=months<=12 and 1<=day<=31 and year>0:
            break
    return date(year, months, day)

def generator_id(n):
    id='0'*(8-len(str(n)))+str(n)
    return id

def generate_id():
    n=0
    while True:
        if generator_id(n) in dict:
            n+=1
        else:
            break
    return generator_id(n)


def add_adress(adress, m2, price,  datesale, prod):
    id = generate_id()
    if id not in dict:
        dict[id] = {'адрес': adress,
                      'метраж (м^2)': m2,
                      'стоимость': price,
                    'продавец': prod,
                      'дата выставления на продажу': (datesale),
                      'время нахождения в продаже': date.today() - (datesale)
                      }
    else:
        print('Данный объект уже внесён в базу данных')

def del_records(name):
    if name in dict:
        del dict[name]
        print(f'Запись об объекте {name} удалена.')
    else:
        print(f'Запись об объекте {name} не найдена!')

dict={}
add_adress('Адрес1', 40, '-', date(2020, 11, 28), '-')
add_adress('Адрес2', 44, 150_000, date(2022, 4, 15), 'Иван')
add_adress('Адрес3', 50, 130_000, date(2024, 6, 2), 'Татьяна')

def viewing_records(dict):
    tabl = PrettyTable(title='Агенство', min_table_width=0)
    tabl.clear()
    tabl.field_names = ['id', 'Адрес', 'Метраж в м^2', 'Стоимость', 'Продавец', 'Дата выставления на продажу', 'Время нахождения в продаже']
    for name, info in dict.items():
        tabl.add_row([name, info['адрес'], info['метраж (м^2)'],  info['стоимость'], info['продавец'], info['дата выставления на продажу'], info['время нахождения в продаже']])
    print(tabl)

n = 0
while n != 6:
    n = menu()
    while n not in range(1, 6):
        n = int(input("Повторите выбор пункта меню для продолжения:"))
    if n == 1:
        print('***Просмотр всех объектов:***\n')
        viewing_records(dict)
    elif n == 2:
        adress=str(input('Введите адресс: '))
        datesell=input_datesell()
        price='-'
        prod='-'
        prod=str(input('Введите имя продавца, иначе оставьте в строке "-": '))
        while True:
            k=int(input('Нажмите 1, если будете вводить цену квартиры; 0 - если нет: '))
            if k==1 or k==0:
                break
        if k==1:
            while True:
                price = float(input('Введите цену: '))
            if price>0:
                break
        while True:
            m2 = float(input('Введите метраж в м^2: '))
            if m2>0:
                break
        add_adress(adress, m2, price, datesell, prod)
    elif n == 3:
        id = input('Введите id объекта для удаления:')
        del_records(id)
    elif n==4:
        while True:
            kolvo=int(input('Введите количество квартир для покупки: '))
            minm2=float(input('Введите минимальный метраж каждой квартиры: '))
            maxm2=float(input('Введите максимальный метраж каждой квартиры: '))
            money=float(input('Введите имеющееся количество денег'))
            if kolvo>0 and money>0 and minm2>0 and maxm2>0 and minm2<=maxm2:
                break
        pokypka(kolvo, minm2, maxm2, money)
    else:
        print('Работа с программой завершена.')
        exit()

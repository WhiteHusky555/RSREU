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
    print('4. Завершение работы с базой данных\n')
    n = int(input("Выберите пункт меню для продолжения:"))
    return n

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


def add_adress(adress, m2, perm2, datesale):
    id = generate_id()
    if id not in dict:
        price=int(m2)*float(perm2)
        dict[id] = {'адрес': adress,
                      'метраж (м^2)': m2,
                      'цена за м^2': perm2,
                      'стоимость': price,
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
add_adress('Адрес1', 40, 120_000, date(2020, 11, 28))
add_adress('Адрес2', 44, 119_000, date(2022, 4, 15))
add_adress('Адрес3', 50, 130_000, date(2024, 6, 2))

def viewing_records(dict):
    tabl = PrettyTable(title='Агенство', min_table_width=0)
    tabl.clear()
    tabl.field_names = ['id', 'Адрес', 'Метраж в м^2', 'Цена за м^2', 'Стоимость', 'Дата выставления на продажу', 'Время нахождения в продаже']
    for name, info in dict.items():
        tabl.add_row([name, info['адрес'], info['метраж (м^2)'], info['цена за м^2'], info['стоимость'], info['дата выставления на продажу'], info['время нахождения в продаже']])
    print(tabl)

n = 0
while n != 5:
    n = menu()
    while n not in range(1, 6):
        n = int(input("Повторите выбор пункта меню для продолжения:"))
    if n == 1:
        print('***Просмотр всех объектов:***\n')
        viewing_records(dict)
    elif n == 2:
        adress=str(input('Введите адресс: '))
        datesell=input_datesell()
        while True:
            m2 = float(input('Введите метраж в м^2: '))
            perm2 = float(input('Введите цену на м^2: '))
            if m2>0 and perm2>0:
                break
        add_adress(adress, m2, perm2, datesell)
    elif n == 3:
        id = input('Введите id объекта для удаления:')
        del_records(id)
    else:
        print('Работа с программой завершена.')
        exit()

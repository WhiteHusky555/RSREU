from datetime import date
from prettytable import PrettyTable


class Apartment:
    id_counter = 0

    def __init__(self, address, area, price, seller, sale_date):
        self.id = f"0" * (8 - len(str(Apartment.id_counter))) + str(Apartment.id_counter)
        Apartment.id_counter += 1
        self.address = address
        self.area = area
        self.price = price
        self.seller = seller
        self.sale_date = sale_date
        self.time_on_sale = date.today() - sale_date

    def __str__(self):
        return f"Квартира {self.id}: {self.address}, площадь {self.area} кв.м, цена {self.price} руб"


class Database:
    def __init__(self):
        self.apartments = {}

    def add_apartment(self, address, area, price, seller, sale_date):
        apartment=Apartment(address, area, price, seller, sale_date)
        self.apartments[apartment.id] = apartment

    def delete_apartment(self, id):
        if id in self.apartments:
            del self.apartments[id]
            print(f'Объект {id} удалён.')
        else:
            print(f"Квартира {id} не найдена")

    def get_apartments(self):
        return list(self.apartments.values())

    def print_table(self):
        table = PrettyTable(title='Агентство', min_table_width=0)
        table.field_names = ['id', 'Адрес', 'Площадь (кв.м)', 'Цена (руб)', 'Продавец', 'Дата выставления на продажу',
                             'Время нахождения в продаже']
        for apartment in self.get_apartments():
            table.add_row([apartment.id, apartment.address, apartment.area, apartment.price, apartment.seller,
                           apartment.sale_date, apartment.time_on_sale])
        print(table)

    def purchase_apartments(self, kolvo, minm2, maxm2, money):
        list_price = []
        for apartment in self.get_apartments():
            if minm2 <= apartment.area <= maxm2 and apartment.price != '-':
                list_price += [[apartment.id, apartment.price, apartment.area]]
        if list_price == []:
            print('Покупка по заданным параметрам невозможна')
            return
        list_price.sort(key=lambda x: x[1])
        if kolvo > len(list_price):
            print('Покупка по заданным параметрам невозможна')
            return
        money_from_list = 0
        for i in range(kolvo):
            money_from_list += float(list_price[i][1])
        if money < money_from_list:
            print('Покупка по заданным параметрам невозможна')
            return
        else:
            table = PrettyTable(title='Агентство', min_table_width=0)
            table.field_names = ['id', 'Адрес', 'Площадь (кв.м)', 'Цена (руб)', 'Продавец',
                                 'Дата выставления на продажу', 'Время нахождения в продаже']
            for i in range(kolvo):
                apartment = self.get_apartment(list_price[i][0])
                table.add_row([apartment.id, apartment.address, apartment.area, apartment.price, apartment.seller,
                               apartment.sale_date, apartment.time_on_sale])
            print(table)

    def get_apartment(self, id):
        return self.apartments.get(id)


def input_datesell():
    while True:
        year = int(input('Введите год выставления на продажу: '))
        month = int(input('Введите месяц выставления на продажу (число): '))
        day = int(input('Введите день выставления на продажу (число): '))
        if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
            break
    return date(year, month, day)


def add_apartment(database):
    address = input('Введите адрес: ')
    datesell = input_datesell()
    price = '-'
    prod = input('Введите имя продавца, или оставьте в поле "-": ')
    while True:
        k = int(input('Введите 1 для ввода цены квартиры, 0 для пропуска: '))
        if k == 1 or k == 0:
            break
    if k == 1:
        while True:
            price = float(input('Введите цену: '))
            if price > 0:
                break
    while True:
        m2 = float(input('Введите площадь в кв.м: '))
        if m2 > 0:
            break
    database.add_apartment(address, m2, price, prod, datesell)


def menu():
    print()
    print('  МЕНЮ:  '.center(38, "*"))
    print('1. Просмотр всех записей в базе данных')
    print('2. Добавление объекта')
    print('3. Удаление объекта по id')
    print('4. Вычисление покупки квартир')
    print('5. Завершение работы с базой данных')
    n = int(input("Выберите пункт меню для продолжения: "))
    return n


database = Database()
database.add_apartment('Адрес1', 44, '-', '-', date(2020, 12, 12))
database.add_apartment('Адрес2', 50, 1550000, 'Иван', date(2022, 12, 21))
database.add_apartment('Адрес3', 38, 1150000, 'Татьяна', date(2024, 5, 9))

while True:
    n = menu()
    if n == 1:
        database.print_table()
    elif n == 2:
        add_apartment(database)
    elif n == 3:
        id = input('Введите id объекта для удаления: ')
        database.delete_apartment(id)
    elif n == 4:
        while True:
            kolvo = int(input('Введите количество квартир для покупки: '))
            minm2 = float(input('Введите минимальную площадь: '))
            maxm2 = float(input('Введите максимальную площадь: '))
            money = float(input('Введите имеющееся количество денег: '))
            if kolvo > 0 and money > 0 and minm2 > 0 and maxm2 > 0 and minm2 <= maxm2:
                break
        database.purchase_apartments(kolvo, minm2, maxm2, money)
    elif n == 5:
        print('Работа с программой завершена.')
        break
    else:
        print('Некорректный ввод. Пожалуйста, повторите выбор.')

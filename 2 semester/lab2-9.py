def menu():
    print()
    print('  МЕНЮ:  '.center(38, "*"))
    print('1. Просмотр всех записей в базе данных')
    print('2. Добавление сотрудника')
    print('3. Удаление сотрудника по имени')
    print('4. Рассчёт накоплений сотрудника на определённую покупку')
    print('5. Завершение работы с базой данных\n')
    n = int(input("Выберите пункт меню для продолжения:"))
    return n

def add_employee(name, dolj, kv, okl, vz):
    if name not in dict:
        podrab = int(vz)*0.5*okl
        dict[name] = {'должность': dolj,
                      'квалификация': kv,
                      'оклад за месяц': okl,
                      'возможность подработки': vz,
                      'оплата за подработку': podrab}
    else:
        print('Данный работник уже внесён в базу данных')

def del_records(name):
    if name in dict:
        del dict[name]
        print(f'Запись о сотруднике {name} удалена.')
    else:
        print(f'Запись о сотруднике {name} не найдена!')

dict={}
add_employee('Антипов', 'Доцент', 'Кандидат технических наук', 80, bool(False))
add_employee('Бубнов', 'Доцент', 'Кандидат физико-математических наук', 70, bool(True))
add_employee('Овечкин', 'Заведующий кафедрой', 'Доктор технических наук', 100, bool(True))
add_employee('Пылькин', 'Профессор', 'Доктор технических наук', 80, bool(True))
add_employee('Власов', 'Доцент', 'Доктор технических наук', 70, bool(False))

def viewing_records(dict):
    for name, info in dict.items():
        print(f'Имя: {name}\n'
              f'Должность: {info["должность"]}\n'
              f'Квалификация: {info["квалификация"]}\n'
              f'Оклад за месяц: {info["оклад за месяц"]}\n'
              f'Возможность подработки: {info["возможность подработки"]}\n'
              f'Оплата за подработку: {info["оплата за подработку"]}')
        print('')

def checking_the_purchase(Name, money, proc1, proc2):
    for name, info in dict.items():
        if name==Name:
            k=money/(info['оклад за месяц']*proc1 + info['оплата за подработку']*proc2)
            if k%1>0:
                k=int(k+1)
    return k

n = 0
while n != 5:
    n = menu()
    while n not in range(1, 6):
        n = int(input("Повторите выбор пункта меню для продолжения:"))
    if n == 1:
        print('***Просмотр всех записей сотрудников:***\n')
        viewing_records(dict)
    elif n == 2:
        name=str(input('Введите имя: '))
        dolj=str(input('Введите должность: '))
        kv=str(input('Введите квалификацию: '))
        while True:
            okl=int(input('Введите оклад за месяц: '))
            if okl>0:
                break
        vz=bool(int(input('Введите 0 - если сотрудник не может иметь подработку\nВ обратном случае введите 1:\n')))
        add_employee(name, dolj, kv, okl, vz)
    elif n == 3:
        name = input('Введите имя сотрудника для удаления:')
        del_records(name)
    elif n == 4:
        while True:
            name=str(input('Введите имя сотрудника: '))
            if name not in dict:
                print('Сотрудник не найден')
            else:
                break
        while True:
            money = float(input("Введите сумму денег:"))
            if money>0:
                break
        while True:
            proc1=float(input('Введите процент, который сотрудник может откладывать с оклада: '))*0.01
            proc2=float(input('Введите процент, который сотрудник может откладывать с подработки: '))*0.01
            if proc1>0 and proc2>0:
                break
        months=checking_the_purchase(name, money, proc1, proc2)
        print(f'Время на накопление суммы {money} coставит {months} месяцев')
    else:
        print('Работа с программой завершена.')

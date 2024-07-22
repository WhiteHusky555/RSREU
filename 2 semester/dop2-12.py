class Employee:
    def __init__(self, name, position, qualification, salary, overtime):
        self.name = name
        self.position = position
        self.qualification = qualification
        self.salary = salary
        self.overtime = overtime
        self.overtime_payment = self.calculate_overtime_payment()

    def calculate_overtime_payment(self):
        return self.overtime * 0.5 * self.salary

class Database:
    def __init__(self):
        self.employees = {}

    def add_employee(self, name, position, qualification, salary, overtime):
        employee = Employee(name, position, qualification, salary, overtime)
        if employee.name not in self.employees:
            self.employees[employee.name] = employee
        else:
            print('Данный работник уже внесён в базу данных.')

    def delete_employee(self, name):
        if name in self.employees:
            del self.employees[name]
            print(f'Запись о сотруднике {name} удалена.')
        else:
            print(f'Запись о сотруднике {name} не найдена!')

    def view_all_employees(self):
        for name, employee in self.employees.items():
            print(f'Имя: {name}\n'
                  f'Должность: {employee.position}\n'
                  f'Квалификация: {employee.qualification}\n'
                  f'Оклад за месяц: {employee.salary}\n'
                  f'Возможность подработки: {employee.overtime}\n'
                  f'Оплата за подработку: {employee.overtime_payment}\n')

    def calculate_savings_time(self, name, money, salary_percentage, overtime_percentage):
        if name in self.employees:
            employee = self.employees[name]
            total_income = employee.salary + employee.overtime_payment
            savings_time = money / (total_income * salary_percentage + employee.overtime_payment * overtime_percentage)
            if savings_time % 1 > 0:
                savings_time = int(savings_time + 1)
            return savings_time
        else:
            return None

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

database = Database()
database.add_employee('Антипов', 'Доцент', 'Кандидат технических наук', 80, bool(False))
database.add_employee('Бубнов', 'Доцент', 'Кандидат физико-математических наук', 70, bool(True))
database.add_employee('Овечкин', 'Заведующий кафедрой', 'Доктор технических наук', 100, bool(True))
database.add_employee('Пылькин', 'Профессор', 'Доктор технических наук', 80, bool(True))
database.add_employee('Власов', 'Доцент', 'Доктор технических наук', 70, bool(False))

n = 0
while n != 5:
    n = menu()
    while n not in range(1, 6):
        n = int(input("Повторите выбор пункта меню для продолжения: "))
    if n == 1:
        print('***Просмотр всех записей сотрудников:***\n')
        database.view_all_employees()
    elif n == 2:
        name = input('Введите имя:  ')
        position = input('Введите должность: ')
        qualification = input('Введите квалификацию: ')
        while True:
            salary = int(input('Введите оклад за месяц: '))
            if salary > 0:
                break
        overtime = bool(int(input('Введите 0 - если сотрудник не может иметь подработку\nВ обратном случае введите 1:\n')))
        database.add_employee(name, position, qualification, salary, overtime)
    elif n == 3:
        name = input('Введите имя сотрудника для удаления: ')
        database.delete_employee(name)
    elif n == 4:
        while True:
            name = input('Введите имя сотрудника: ')
            if name not in database.employees:
                print('Сотрудник не найден.')
            else:
                break
        while True:
            money = float(input("Введите сумму денег: "))
            if money > 0:
                break
        while True:
            salary_percentage = float(input('Введите процент, который сотрудник может откладывать с оклада: ')) * 0.01
            overtime_percentage = float(input('Введите процент, который сотрудник может откладывать с подработки: ')) * 0.01
            if salary_percentage > 0 and overtime_percentage > 0:
                break
        savings_time = database.calculate_savings_time(name, money, salary_percentage, overtime_percentage)
        if savings_time is not None:
            print(f'За {savings_time} месяцев будет накоплено {money}.')
        else:
            print('Сотрудник не найден.')
    else:
        print('Работа с программой завершена.')

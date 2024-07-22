class BaseObject:
    def __init__(self):
        self.operations = []

    def get_operations(self):
        return self.operations

    def add_operations(self, operations):
        self.operations += operations

    def to_console(self):
        print(self.get_operations())


class Vector(BaseObject):
    def __init__(self, x, y, z):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.x = x
        else:
            print('Ошибка в координате х')

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.y = y
        else:
            print('Ошибка в координате y')

    def set_z(self, z):
        if isinstance(z, (int, float)):
            self.z = z
        else:
            print('Ошибка в координате z')
    def add(self, v2):
        v3 = Vector(self.get_x() + v2.get_x(), self.get_y() + v2.get_y(), self.get_z() + v2.get_z())
        self.add_operations(['Сложение'])
        return v3

    def sub(self, v2):
        v3 = Vector(self.get_x() - v2.get_x(), self.get_y() - v2.get_y(), self.get_z() - v2.get_z())
        self.add_operations(['Вычитание'])
        return v3

    def mul(self, v2):
        v3 = self.get_x() * v2.get_x() + self.get_y() * v2.get_y() + self.get_z() * v2.get_z()
        self.add_operations(['Скалярное произведение'])
        return v3

    def scale(self, s):
        v3 = Vector(self.get_x() * s, self.get_y() * s, self.get_z() * s)
        self.add_operations(['Умножение вектора на число'])
        return v3

    def to_console(self):
        print(self.get_x(), self.get_y(), self.get_z())
        super().to_console()

'''
v1 = Vector(1, 2, 3)
v2 = Vector(3, 2, 1)
v3 = v1.add(v2)
v3.to_console()
print(v3.get_operations())
v4 = v1.sub(v2)
print(v4.get_x(), v4.get_y(), v4.get_z())
v5 = v1.mul(v2)
print(v5)
v6 = v1.scale(5)
v1.to_console()
'''
v1=Vector(1, 2, 3)
v2=Vector(5, 6 ,7)
v3=v1.add(v2)
v4=v1.add(v3)
v5=v1.sub(v4)
v1.to_console()
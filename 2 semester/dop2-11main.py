
class Vector():
    def __init__(self, x, y, z):
        self.__x=x
        self.set_x(x)
        self.__y = y
        self.set_y(y)
        self.__z = z
        self.set_z(z)
        self.operation_list=[]


    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_operation_list(self):
        return self.operation_list
    def set_operation_list(self, operation):
        self.operation_list+=[operation]
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
        v3=Vector((self).get_x()+(v2).get_x(), (self).get_y()+(v2).get_y(), (self).get_z()+(v2).get_z())
        operations=self.get_operation_list()+v2.get_operation_list()+['Сложение']
        v3.set_operation_list(operations)
        return v3
    def sub(self, v2):
        v3 = Vector((self).get_x() - (v2).get_x(), (self).get_y() - (v2).get_y(), (self).get_z() - (v2).get_z())
        operations = self.get_operation_list() + v2.get_operation_list() + ['Вычитание']
        v3.set_operation_list(operations)
        return v3
    def mul(self, v2):
        v3=(self.get_x()*v2.get_x() + self.get_y()*v2.get_y() + self.get_z()*v2.get_z())
        operations = self.get_operation_list() + v2.get_operation_list() + ['Скалярное произведение']
        v3=VectorAfterMul(v3)
        v3.set_operation_list_VAM(operations)
        return v3
    def scale(self, s):
        v3=Vector(self.get_x()*s, self.get_y()*s, self.get_z()*s)
        operations = self.get_operation_list() + v2.get_operation_list() + ['Умножение вектора на число']
        v3.set_operation_list(operations)
        return v3
class VectorAfterMul(Vector):
    def __init__(self, x):
        self.__x = x
        self.set_x(x)
        self.operation_list = []

    def get_x(self):
        return self.x
    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.x = x
    def get_operation_list(self):
        return self.operation_list
    def set_operation_list_VAM(self, operation):
        self.operation_list+=[operation]

v1=Vector(1, 2, 3)
v2=Vector(3, 2, 1)
v3=v1.add(v2)
print(v1.get_x(), v1.get_y(), v1.get_z())
print(v3.get_x(), v3.get_y(), v3.get_z())
print(v3.get_operation_list())
v4=v1.sub(v2)
print(v4.get_x(), v4.get_y(), v4.get_z())
v5=v1.mul(v2)
print(v5.get_x())
print(v5.get_operation_list())
v6=v1.scale(5)
print(v6.get_x(), v6.get_y(), v6.get_z())
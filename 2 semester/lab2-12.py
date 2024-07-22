class Confectionery:
    def __init__(self, name, count_products, avg_price):
        self.__name = name
        self.set_name(name)
        self.__count_products = count_products
        self.set_count_products(count_products)
        self.__avg_price = avg_price
        self.set_avg_price(avg_price)

    def get_name(self):
        return self.name

    def get_count_products(self):
        return self.count_products

    def get_avg_price(self):
        return self.avg_price

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name
        else:
            print("Ошибка в названии продукта.")

    def set_count_products(self, count_product):
        if isinstance(count_product, int) and count_product > 0:
            self.count_products = count_product
        else:
            print("Ошибка в количестве продуктов.")

    def set_avg_price(self, avg_price):
        if isinstance(avg_price, (int, float)) and avg_price > 0:
            self.avg_price = avg_price
        else:
            print('Ошибка в средней стоимости')


p1 = Confectionery('Продукт1', 10, 62)
p2 = Confectionery('Продукт2', 100, 44)
p3 = Confectionery('Продукт3', 53, 29)
p4 = Confectionery('Продукт4', 753, 13)
p5 = Confectionery('Продукт5', 25, 21)
sweetshop = [p1, p2, p3, p4, p5]
for s in sweetshop:
    print(f'Название продукта: {s.get_name()}')
    print(f'Количество продукта: {s.get_count_products()}')
    print(f'Название продукта: {s.get_avg_price()}')
p=Confectionery()

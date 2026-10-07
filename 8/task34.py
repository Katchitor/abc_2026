# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.

class Product:
    def __init__(self, name:str, price:int):
        self.name = name
        self.price = price
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value:str):
        self._name = value

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value:int):
        if value >= 0:
            self._price = int(value)
        else:
            self._price = 0

class Order:
    def __init__(self):
        self._products = []
    
    @property
    def total_price(self):
        self._total_price = 0
        for product in self._products:
            self._total_price += product.price
        return self._total_price

    def add_product(self, product:Product):
        self._products.append(product)

    def remove_product(self, product:Product):
        self._products.remove(product)



# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12
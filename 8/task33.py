# Инкапсуляция и property
# todo: Класс "Товар" (Защита от отрицательной цены)
# Создайте класс Product. У него есть свойства name (простая строка) и price.
# При установке цены проверяйте, что она не отрицательная.
# Если пытаются установить отрицательную цену, устанавливайте 0.


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
    

# Пример использования
product = Product("Book", 10)
print(product.price)  # 10
product.price = -5
print(product.price)  # 0


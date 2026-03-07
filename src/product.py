class Product:
    """Модуль представляющий товары"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, data_dict):
        return cls(data_dict["name"], data_dict["description"], data_dict["price"], data_dict["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной!")
        else:
            self.__price = new_price

    def __str__(self):  # Задание 1 часть 1
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):  # Задание 2 переопределить магический метод __add__ в классе Product
        return self.price * self.quantity + other.price * other.quantity

from abc import ABC, abstractmethod
from typing import Any


# Базовый абстрактный класс для всех продуктов
class BaseProduct(ABC):
    """Абстрактный класс для всех продуктов"""

    @abstractmethod
    def example_method(self) -> None:
        """Пример абстрактного метода"""
        pass


# Класс-миксин для логирования создания объектов
class CreationLoggerMixin:
    """Миcкин для логирования создания объектов"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        # Получаем имя класса, от которого был создан объект
        class_name = self.__class__.__name__

        # Формируем строку с параметрами
        args_repr = ', '.join(repr(arg) for arg in args)
        kwargs_repr = ', '.join(f"{key}={value!r}" for key, value in kwargs.items())
        params = f"{args_repr}{', ' if args_repr and kwargs_repr else ''}{kwargs_repr}"

        # Печатаем информацию о создании объекта
        print(f"{class_name}({params})")


class Product(CreationLoggerMixin, BaseProduct):
    """Модуль представляющий товары"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        # Задание 1 Проверка на нулевое количество
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        # Вызываем конструктор миксина, который в свою очередь вызовет конструктор BaseProduct
        super().__init__(name=name, description=description, price=price, quantity=quantity)

        # Инициализируем атрибуты
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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        # Добавляем проверку типов
        if not isinstance(other, type(self)):
            raise TypeError("Нельзя складывать товары разных классов")

        return self.price * self.quantity + other.price * other.quantity

    # Реализация абстрактного метода
    def example_method(self) -> None:
        pass


# Создание классов-наследников

class Smartphone(Product):
    """Класс представляющий смартфоны"""
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    # Реализация абстрактного метода
    def example_method(self) -> None:
        pass


class LawnGrass(Product):
    """Класс представляющий газонную траву"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    # Реализация абстрактного метода
    def example_method(self) -> None:
        pass

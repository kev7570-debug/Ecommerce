# from src.product import Product
#
#
# def test_product_creation():
#     """
#     Тестирование создания объекта Product и его атрибутов.
#     """
#     product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     assert product.name == "Samsung Galaxy S23 Ultra"
#     assert product.description == "256GB, Серый цвет, 200MP камера"
#     assert product.price == 180000.0
#     assert product.quantity == 5
#
#
# def test_price_setter():
#     """
#     Тестирование работы сеттера для цены: проверка ограничений на установку отрицательных и нулевых цен.
#     """
#     product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#
#     # Устанавливаем допустимую цену
#     product.price = 200000.0
#     assert product.price == 200000.0
#
#     # Пробуем установить отрицательную цену
#     product.price = -100
#     assert product.price == 200000.0  # Цена не изменилась
#
#     # Пробуем установить нулевую цену
#     product.price = 0
#     assert product.price == 200000.0  # Цена не изменилась


import pytest
from src.product import Product


@pytest.fixture
def setup_products():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("iPhone 15", "512GB, Gray Space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


def test_product_str_representation(setup_products):
    """Тестирование строкового представления продукта"""
    product = setup_products[0]
    expected_output = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected_output


def test_product_addition(setup_products):
    """Тестирование сложения товаров"""
    product1 = setup_products[0]
    product2 = setup_products[1]
    expected_sum = 180000.0 * 5 + 210000.0 * 8
    assert product1 + product2 == expected_sum

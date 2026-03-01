import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def setup_category():
    """Создание базовой категории для тестирования"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 15", "512GB, Gray Space", 210000.0, 8)
    category = Category("Смартфоны", "Различные модели смартфонов", [product1, product2])
    return category


def test_add_product(setup_category):
    """
    Тестирование метода add_product(): проверяем, что новый продукт добавляется в категорию.
    """
    category = setup_category
    old_product_count = len(category.products_in_list)

    new_product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    category.add_product(new_product)

    # Проверяем, что количество товаров увеличилось
    assert len(category.products_in_list) == old_product_count + 1
    # Проверяем, что новый продукт содержится в списке
    assert new_product in category.products_in_list


def test_products_in_list(setup_category):
    """
    Тестирование свойства products_in_list: проверяем, что оно возвращает корректный список товаров.
    """
    category = setup_category
    products = category.products_in_list
    assert len(products) == 2  # Начальное количество товаров
    assert isinstance(products[0], Product)  # Первый элемент списка — это объект Product

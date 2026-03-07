import pytest
from src.category import Category
from src.product import Product


def test_products_format(setup_category):
    """
    Тестирование формата строки в геттере products.
    """
    category = setup_category
    products_str = category.products
    lines = products_str.split('\n')[:-1]  # Исключение пустой строки
    for line in lines:
        assert "руб." in line
        assert "шт." in line


@pytest.fixture
def setup_category():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("iPhone 15", "512GB, Gray Space", 210000.0, 8)
    category = Category("Смартфоны", "Различные модели смартфонов", [product1, product2])
    return category


# Добавляем фикстуру для сброса статических атрибутов перед каждым тестом
@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0


def test_category_init_with_products(setup_category):
    """Тестирование конструктора с товарами"""
    category = setup_category
    assert category.name == "Смартфоны"
    assert category.description == "Различные модели смартфонов"
    assert len(category._Category__products) == 2
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_init_without_products():
    """Тестирование конструктора без товаров"""
    category = Category("Без товаров", "")
    assert category.name == "Без товаров"
    assert category.description == ""
    assert len(category._Category__products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_str_representation(setup_category):
    """Тестирование строкового представления категории"""
    category = setup_category
    expected_output = "Смартфоны, количество продуктов: 13 шт."
    assert str(category) == expected_output


def test_category_empty_products():
    """Тестирование метода products с пустым списком товаров"""
    category = Category("Без товаров", "")
    products_str = category.products
    assert products_str == ""


def test_category_products_format(setup_category):
    """Тестирование формата строки в геттере products"""
    category = setup_category
    products_str = category.products
    lines = products_str.split('\n')[:-1]
    for line in lines:
        assert "руб." in line
        assert "шт." in line


def test_category_total_quantity(setup_category):
    """Тестирование расчёта общей суммы товаров в категории"""
    category = setup_category
    total_quantity = sum(product.quantity for product in category._Category__products)
    assert total_quantity == 13  # 5 + 8


def test_category_none_values():
    """Тестирование конструктора с None-значениями"""
    category = Category(None, None, None)
    assert category.name is None
    assert category.description is None
    assert len(category._Category__products) == 0
    assert Category.category_count == 1
    assert Category.product_count == 0

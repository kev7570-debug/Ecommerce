# import pytest
# from src.category import Category
# from src.product import Product
#
#
# @pytest.fixture
# def setup_products():
#     """Создание фикстуры с набором продуктов для тестирования"""
#     return [
#         Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
#         Product("iPhone 15", "512GB, Gray Space", 210000.0, 8),
#         Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#     ]
#
#
# @pytest.fixture
# def setup_categories(setup_products):
#     """Создание фикстуры с набором категорий для тестирования"""
#     categories = []
#     categories.append(Category("Смартфоны", "Различные модели смартфонов", setup_products[:]))
#     categories.append(Category("Ноутбуки", "Модели ноутбуков", []))
#     return categories
#
#
# def test_category_initialization(setup_categories):
#     """
#     Тестируем корректность инициализации объекта Category.
#     """
#     category = setup_categories[0]
#     assert isinstance(category, Category)
#     assert category.name == "Смартфоны"
#     assert category.description == "Различные модели смартфонов"
#     assert len(category.products) == 3
#
#
# def test_product_count(setup_categories):
#     """
#     Тестируем правильный подсчёт общего количества продуктов.
#     """
#     expected_total_products = sum([len(cat.products) for cat in setup_categories])
#     actual_total_products = Category.product_count
#     assert expected_total_products == actual_total_products
#
#
# def test_category_count(setup_categories):
#     """
#     Тестируем правильный подсчёт общего количества категорий.
#     """
#     expected_total_categories = len(setup_categories)
#     actual_total_categories = Category.category_count
#     assert expected_total_categories == actual_total_categories


import pytest
from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_category_counters():
    """Автоматически сбрасывает счетчики перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def setup_products():
    """Создание фикстуры с набором продуктов для тестирования"""
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("iPhone 15", "512GB, Gray Space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    ]


@pytest.fixture
def setup_categories(setup_products):
    """Создание фикстуры с набором категорий для тестирования"""
    categories = []
    categories.append(Category("Смартфоны", "Различные модели смартфонов", setup_products[:]))
    categories.append(Category("Ноутбуки", "Модели ноутбуков", []))
    return categories


def test_category_initialization(setup_categories):
    """
    Тестируем корректность инициализации объекта Category.
    """
    category = setup_categories[0]
    assert isinstance(category, Category)
    assert category.name == "Смартфоны"
    assert category.description == "Различные модели смартфонов"
    assert len(category.products) == 3


def test_product_count(setup_categories):
    """
    Тестируем правильный подсчёт общего количества продуктов.
    """
    expected_total_products = sum([len(cat.products) for cat in setup_categories])
    actual_total_products = Category.product_count
    assert expected_total_products == actual_total_products


def test_category_count(setup_categories):
    """
    Тестируем правильный подсчёт общего количества категорий.
    """
    expected_total_categories = len(setup_categories)
    actual_total_categories = Category.category_count
    assert expected_total_categories == actual_total_categories

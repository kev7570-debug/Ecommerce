import pytest
from src.category import Category
from src.product import Product, Smartphone


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


# Новые тесты для новой функциональности
# Фикстуры для создания тестовых объектов
@pytest.fixture
def category_fixture():
    product1 = Product("Product 1", "Desc 1", 100.0, 10)
    product2 = Product("Product 2", "Desc 2", 200.0, 20)
    return Category("Test Category", "Test Desc", [product1, product2])


@pytest.fixture
def empty_category_fixture():
    return Category("Empty Category", "No products here")


# Тестирование конструктора
def test_category_constructor(category_fixture):
    assert category_fixture.name == "Test Category"
    assert len(category_fixture._Category__products) == 2


def test_empty_category_constructor(empty_category_fixture):
    assert empty_category_fixture.name == "Empty Category"
    assert len(empty_category_fixture._Category__products) == 0


# Тестирование метода __str__
def test_category_str(category_fixture):
    assert str(category_fixture) == "Test Category, количество продуктов: 30 шт."


# Тестирование метода products
def test_category_products(category_fixture):
    products_str = category_fixture.products
    assert "Product 1" in products_str
    assert "Product 2" in products_str


def test_empty_category_products(empty_category_fixture):
    assert empty_category_fixture.products == ""


# Тестирование метода add_product
def test_add_valid_product(category_fixture):
    new_product = Product("New Product", "New Desc", 300.0, 30)
    category_fixture.add_product(new_product)
    assert len(category_fixture._Category__products) == 3


def test_add_invalid_product(category_fixture):
    with pytest.raises(TypeError):
        category_fixture.add_product("Invalid Product")


def test_add_subclass_product(category_fixture):
    smartphone = Smartphone("Samsung", "Desc", 1000.0, 10, 95.0, "Model", 256, "Black")
    category_fixture.add_product(smartphone)
    assert len(category_fixture._Category__products) == 3

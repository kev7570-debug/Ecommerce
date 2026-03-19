import pytest
from src.product import Product, Smartphone, LawnGrass


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


# новые тесты для новой функциональности
# Фикстуры для создания тестовых объектов
@pytest.fixture
def smartphone_fixture():
    return Smartphone("Samsung", "Description", 1000.0, 10, 95.0, "Model", 256, "Black")


@pytest.fixture
def lawn_grass_fixture():
    return LawnGrass("Grass", "Green Grass", 50.0, 100, "USA", "7 days", "Green")


@pytest.fixture
def base_product_fixture():
    return Product("Base Product", "Base Description", 500.0, 5)


# Тестирование конструкторов
def test_smartphone_constructor(smartphone_fixture):
    assert smartphone_fixture.name == "Samsung"
    assert smartphone_fixture.efficiency == 95.0
    assert smartphone_fixture.model == "Model"
    assert smartphone_fixture.memory == 256
    assert smartphone_fixture.color == "Black"


def test_lawn_grass_constructor(lawn_grass_fixture):
    assert lawn_grass_fixture.name == "Grass"
    assert lawn_grass_fixture.country == "USA"
    assert lawn_grass_fixture.germination_period == "7 days"
    assert lawn_grass_fixture.color == "Green"


# Тестирование метода __str__
def test_product_str(base_product_fixture):
    assert str(base_product_fixture) == "Base Product, 500.0 руб. Остаток: 5 шт."


def test_smartphone_str(smartphone_fixture):
    assert str(smartphone_fixture) == "Samsung, 1000.0 руб. Остаток: 10 шт."


def test_lawn_grass_str(lawn_grass_fixture):
    assert str(lawn_grass_fixture) == "Grass, 50.0 руб. Остаток: 100 шт."


# Тестирование метода __add__
def test_valid_addition(smartphone_fixture, lawn_grass_fixture):
    result = smartphone_fixture + smartphone_fixture
    assert result == 20000.0  # 1000*10 + 1000*10


def test_invalid_addition(smartphone_fixture, lawn_grass_fixture):
    with pytest.raises(TypeError):
        smartphone_fixture + lawn_grass_fixture


# Тестирование геттера и сеттера для цены
def test_price_getter_and_setter(base_product_fixture):
    assert base_product_fixture.price == 500.0
    base_product_fixture.price = 600.0
    assert base_product_fixture.price == 600.0


def test_invalid_price_setting(base_product_fixture, capsys):
    base_product_fixture.price = -100.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной!" in captured.out


#  новые тесты для новой функциональности для абстрактного класса и класса-миксина
# Тесты для миксина CreationLoggerMixin
def test_creation_logger_mixin(capsys, base_product_fixture):
    """Тестирование миксина CreationLoggerMixin"""
    captured = capsys.readouterr()
    expected_output = "Product(name='Base Product', description='Base Description', price=500.0, quantity=5)\n"
    assert captured.out == expected_output


# Тесты для конструкторов классов-наследников
def test_smartphone_constructor_with_defaults():
    """Тестирование конструктора Smartphone с дефолтными значениями"""
    smartphone = Smartphone("Default Phone", "Default Desc", 1000.0, 10, 90.0, "Model", 128, "White")
    assert smartphone.name == "Default Phone"
    assert smartphone.efficiency == 90.0
    assert smartphone.model == "Model"
    assert smartphone.memory == 128
    assert smartphone.color == "White"


def test_lawn_grass_constructor_with_defaults():
    """Тестирование конструктора LawnGrass с дефолтными значениями"""
    grass = LawnGrass("Default Grass", "Default Desc", 50.0, 100, "UK", "10 days", "Yellow")
    assert grass.name == "Default Grass"
    assert grass.country == "UK"
    assert grass.germination_period == "10 days"
    assert grass.color == "Yellow"


# Тесты для строкового представления
def test_smartphone_str_representation(smartphone_fixture):
    """Тестирование строкового представления смартфона"""
    expected_output = "Samsung, 1000.0 руб. Остаток: 10 шт."
    assert str(smartphone_fixture) == expected_output


def test_lawn_grass_str_representation(lawn_grass_fixture):
    """Тестирование строкового представления травы"""
    expected_output = "Grass, 50.0 руб. Остаток: 100 шт."
    assert str(lawn_grass_fixture) == expected_output


# Тесты для геттера и сеттера цены
def test_price_setter_with_negative_value(base_product_fixture, capsys):
    """Тестирование сеттера цены с отрицательным значением"""
    base_product_fixture.price = -100.0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевой или отрицательной!" in captured.out
    assert base_product_fixture.price == 500.0  # Цена не должна измениться


# Тесты для обработки исключения ValueError при создании продукта с нулевым количеством
def test_product_creation_with_zero_quantity():
    """Тестирование создания продукта с нулевым количеством"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Test Desc", 100.0, 0)


def test_product_creation_with_positive_quantity():
    """Тестирование создания продукта с положительным количеством"""
    product = Product("Valid Product", "Valid Desc", 100.0, 10)
    assert product.quantity == 10

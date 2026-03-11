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

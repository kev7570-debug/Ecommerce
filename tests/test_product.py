from src.product import Product


def test_product_creation():
    """
    Тестирование создания объекта Product и его атрибутов.
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter():
    """
    Тестирование работы сеттера для цены: проверка ограничений на установку отрицательных и нулевых цен.
    """
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    # Устанавливаем допустимую цену
    product.price = 200000.0
    assert product.price == 200000.0

    # Пробуем установить отрицательную цену
    product.price = -100
    assert product.price == 200000.0  # Цена не изменилась

    # Пробуем установить нулевую цену
    product.price = 0
    assert product.price == 200000.0  # Цена не изменилась

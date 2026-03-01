import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    """Подготовка экземпляра продукта для тестирования"""
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product_initialization(sample_product):
    """
    Тестируем корректность инициализации объекта Product.
    """
    assert isinstance(sample_product, Product)
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Серый цвет, 200MP камера"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5

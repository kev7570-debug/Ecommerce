from src.product import Product


class Category:
    """Модуль позволяющий создавать категории товаров"""
    name: str
    description: str
    __products: list  # Приватный атрибут

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        # Исправленный метод: считаем общую сумму остатков всех товаров
        total_quantity = sum(product.quantity for product in self.__products)
        return f'{self.name}, количество продуктов: {total_quantity} шт.'

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'Название продукта: {product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str

    # Задание 3: Ограничение добавления продуктов
    def add_product(self, product):
        # Проверяем, что добавляемый объект является продуктом или его наследником
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1

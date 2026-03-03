from src.product import Product


class Category:
    """Класс с описанием категории продуктов"""
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

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f'Название продукта: {product.name}, Стоимость: {product.price}, Остаток: {product.quantity}\n'
        return product_str

    @property
    def products_in_list(self):
        return self.__products

    def add_product(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1

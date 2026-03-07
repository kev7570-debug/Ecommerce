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

    # def __str__(self):
    #     count_product = 0
    #     for product in self.__products:
    #         count_product += product.quantity
    #     return f'{self.name}, количество продуктов: {count_product} шт.'

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
    #
    # @property
    # def products_in_list(self):
    #     return self.__products
    #
    # def add_product(self, product: Product):
    #     self.__products.append(product)
    #     Category.product_count += 1

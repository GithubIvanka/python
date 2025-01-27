class Product:

    __slots__ = ("name", "weight", "category")

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __file_name = "products.txt"

    def get_products(self):
        file = open(self.__file_name, "r")
        products = file.read()
        file.close()
        return products

    def add(self, *products: Product):
        products_in_shop = self.get_products()

        for product in products:
            if product.name in products_in_shop:
                print(f"Продукт {product.name} уже есть в магазине.")
            else:
                file = open(self.__file_name, "a")
                file.write(str(product) + "\n")
                file.close()


if __name__ == "__main__":
    s1 = Shop()

    p1 = Product("Potato", 50.5, "Vegetables")
    p2 = Product("Spaghetti", 3.4, "Groceries")
    p3 = Product("Potato", 5.5, "Vegetables")

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

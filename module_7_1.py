class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight},{self.category}')


class Shop():
    def __init__(self):
        __file_name = 'products.txt'
        file = open(__file_name, 'a')
        file.close()

    def get_products(self):
        get_file = open('products.txt', 'r')
        name_prod = get_file.read()
        get_file.close()
        return name_prod

    def add(self, *products):
        for product in products:
            if str(product) not in self.get_products():
                file = open('products.txt', 'a')
                file.write(f'{str(product)}')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

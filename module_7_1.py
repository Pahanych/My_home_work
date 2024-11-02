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




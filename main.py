class Computer:
    def init(self, name, price, model, color, year):
        self.name = name
        self.price = price
        self.model = model
        self.color = color
        self.year = year

    def get_data(self):
        return f'{self.name}, {self.price} сом, {self.model}, {self.color}, {self.year}'


comp2 = Computer('Samsung', 45000, 'l5', 'White', 2019)
print(comp2.get_data())


class Laptop(Computer):
    def init(self, name, price, model, color, year, storage):
        super().init(name, price, model, color, year)
        self.storage = storage

    def get_data(self):
        return f'{self.name}, {self.price} сом, {self.model}, {self.color}, {self.year}, {self.storage} Гб'


lap1 = Laptop('Macbook', 120000, 'Pro', 'Silver', 2020, 265)
print(lap1.get_data()

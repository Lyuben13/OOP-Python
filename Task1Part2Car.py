class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_capacity=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Enter car model: ")
        self.year = int(input("Enter year of release: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_capacity = float(input("Enter engine capacity (L): "))
        self.color = input("Enter color: ")
        self.price = float(input("Enter price: "))

    def display_info(self):
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Manufacturer: {self.manufacturer}")
        print(f"Engine Capacity: {self.engine_capacity} L")
        print(f"Color: {self.color}")
        print(f"Price: ${self.price}")

    def __str__(self):
        return f"Car(model={self.model}, year={self.year}, manufacturer={self.manufacturer}, " \
               f"engine_capacity={self.engine_capacity}, color={self.color}, price={self.price})"

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.model == other.model and self.year == other.year and self.manufacturer == other.manufacturer

    def __lt__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return self.price <= other.price

car1 = Car()
car1.input_data()
print(car1)

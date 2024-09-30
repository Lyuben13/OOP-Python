class Car:
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
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

car = Car("", 0, "", 0.0, "", 0.0)
car.input_data()
car.display_info()

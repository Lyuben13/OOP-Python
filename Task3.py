class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Enter stadium name: ")
        self.opening_date = input("Enter opening date (YYYY-MM-DD): ")
        self.country = input("Enter country: ")
        self.city = input("Enter city: ")
        self.capacity = int(input("Enter seating capacity: "))

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Opening Date: {self.opening_date}")
        print(f"Country: {self.country}")
        print(f"City: {self.city}")
        print(f"Capacity: {self.capacity}")

stadium = Stadium("", "", "", "", 0)
stadium.input_data()
stadium.display_info()

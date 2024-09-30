class Stadium:
    def __init__(self, name="", opening_date="", country="", city="", capacity=0):
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

    def __str__(self):
        return f"Stadium(name={self.name}, opening_date={self.opening_date}, country={self.country}, " \
               f"city={self.city}, capacity={self.capacity})"

    def __eq__(self, other):
        if not isinstance(other, Stadium):
            return False
        return self.name == other.name and self.city == other.city

    def __lt__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity < other.capacity

    def __le__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return self.capacity <= other.capacity

stadium1 = Stadium()
stadium1.input_data()
print(stadium1)

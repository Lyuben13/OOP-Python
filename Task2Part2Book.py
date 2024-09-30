class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Enter book title: ")
        self.year = int(input("Enter year of release: "))
        self.publisher = input("Enter publisher: ")
        self.genre = input("Enter genre: ")
        self.author = input("Enter author: ")
        self.price = float(input("Enter price: "))

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Publisher: {self.publisher}")
        print(f"Genre: {self.genre}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

    def __str__(self):
        return f"Book(title={self.title}, year={self.year}, publisher={self.publisher}, " \
               f"genre={self.genre}, author={self.author}, price={self.price})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price < other.price

    def __le__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.price <= other.price

book1 = Book()
book1.input_data()
print(book1)

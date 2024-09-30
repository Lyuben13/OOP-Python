class Book:
    def __init__(self, title, year, publisher, genre, author, price):
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

book = Book("", 0, "", "", "", 0.0)
book.input_data()
book.display_info()

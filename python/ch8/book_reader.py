"""
Design the data structures
for an online book reader system
"""


class Book():

    def __init__(self, name, author, url, pages):
        self.name = name
        self.author = author
        self.url = url
        self.pages = pages


class Reader():

    def __init__(self, name):
        self.username = name
        self.books = []
        self.current = None

    def read(self, book):
        if book in self.books:
            self.current = (book, self.books[book])
            return book.pages[self.books[book]]
        else:
            self.books[book] = 0
            return self.read(book)

    def pagedown(self):
        if not current:
            raise ValueError
        else:
            self.books[current[0]] += 1
            self.read(current[0])

    def close(self):
        self.current = None


class System():
    books = []
    users = []

    def __init__(self):
        pass

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, book):
        self.books.remove(book)

    def add_user(self, user):
        self.users.append(user)

    def del_user(self, user):
        self.users.remove(user)

    def search(self, keyword):
        for i in books:
            if keyword in i.name:
                yield i
            elif keyword in i.author:
                yield i

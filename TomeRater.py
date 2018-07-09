from Book import *
from Fiction import Fiction
from NonFiction import NonFiction
from User import User


class TomeRater(object):
    def __init__(self):
        # dictionary that will have user email as their keys to their User object
        self.users = {}

        # dictionary where the key is the Book object and the amount of users read it as values
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return NonFiction(title, subject, level, isbn)

    # This needs to be fixed
    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email, "No user with email: {email}".format(email=email))

        if user:
            user.read_book(book, rating)
            book.add_rating(rating)

            # If the book exists in books dict, then increment +1 else add the book and set value to 1
            self.books[book] = self.books.get(book, 1) + 1

        #print(self.books)

    def add_user(self, name, email, books=None):
        self.users[email] = User(name, email)
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books:
            print(book)

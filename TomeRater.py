from Book import *
from Fiction import Fiction
from NonFiction import NonFiction
from User import *


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
            self.books[book] = self.books.get(book, 0) + 1

        #print(self.books)

    def add_user(self, name, email, books=None):
        self.users[email] = User(name, email)
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)

    # Only iterate through the keys and not the value which have the ratings
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    # Print the User objects (values)
    def print_users(self):
        for user in self.users.values():
            print(user)

    # returns the key with maximum value
    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        highest_rated = Book
        temp_average = 0
        for book in self.books:

            if book.get_average_rating() > temp_average:
                highest_rated = book
                temp_average = book.get_average_rating()
        return highest_rated

    def most_positive_user(self):
        # To get the highest rated number
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())

        return [user for user in self.users.values() if user.get_average_rating() == highest_rated]

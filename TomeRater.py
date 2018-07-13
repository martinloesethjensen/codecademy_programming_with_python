from Book import *
from Fiction import Fiction
from NonFiction import NonFiction
from User import *
import re


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

    def add_user(self, name, email, books=None):
        if email not in self.users:
            self.users[email] = User(name, email)
            if books is not None:
                for book in books:
                    self.add_book_to_user(book, email)
        else:
            print("This user already exists.")

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
        # To get the highest rated number
        highest_rated = max(rating.get_average_rating() for rating in self.books.keys())

        # Return the book if the book is the one with the highest rated number. Also return without '[]'
        return str([book for book in self.books.keys() if book.get_average_rating() == highest_rated]).strip('[]')

    def most_positive_user(self):
        # To get the highest rated number
        highest_rated = max(rating.get_average_rating() for rating in self.users.values())

        # Return the book if the book is the one with the highest rated number. Also return without '[]'
        return str([user for user in self.users.values() if user.get_average_rating() == highest_rated]).strip('[]')

    # Returning the books in an order
    def get_n_read_books(self):
        count = len(self.books)  # counter for the place
        # Sort on the keys instead of values since dictionaries are orderless, we need a list representation.
        # I have decided to print out formatted and not return a tuple, because this is immutable.
        # 'key=lambda kv: kv[1]' sort by the values of each entry
        for book, read in sorted(self.books.items(), key=lambda key_value: key_value[1]):  # Descending order
            print("Place: {place}\n{book}Read: {read} times.\n".format(place=count, book=book, read=read))
            count -= 1  # decrement counter to keep track of place for the book
        return ""
        # reverse=True to have the order ascending
        #return str(sorted(self.books.items(), key=lambda kv: kv[1], reverse=True)).strip('[]')

    # Returning the most read book
    def get_most_read_book(self):
        max_read_count = max(book for book in self.books.values())

        return str([book for book, read_count in self.books.items() if read_count == max_read_count]).strip('[]')
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Dictionary that is going to hold the user's rating of the book
        # and keep count on how many books they have read.
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, new_email):
        self.email = new_email
        return "This user's emil has been changed to: {email}".format(email=new_email)

    def __repr__(self):
        return "User: {name}\n" \
               "Email: {email}\n" \
               "Books read: {books}\n"\
            .format(name=self.name,
                    email=self.email,
                    books=len(self.books)
                    )

    # It only checks for equality and not identity of two object.
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        # returns a float value, because the divider has inbuilt float
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)

    def get_book_read_count(self):
        return len(self.books)

    # Returns a hash value for the book object
    def __hash__(self):
        return hash((self.name, self.email))
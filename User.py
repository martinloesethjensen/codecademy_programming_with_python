class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Dictionary that is going to hold the user's rating of the book
        self.books = {}

    # Method that returns an email on the user
    def get_email(self):
        return self.email

    # Method to change the email on the selected user
    def change_email(self, new_email):
        self.email = new_email
        return "This user's emil has been changed to: {email}".format(email=new_email)

    # The format on how the User object should be printed
    def __repr__(self):
        return "User: {name}\n" \
               "Email: {email}\n" \
               "Books read: {books}\n"\
            .format(name=self.name,
                    email=self.email,
                    books=len(self.books)
                    )

    # Returns True if two users have the same email and name.
    # It only checks for equality and not identity of two object.
    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email
        # return self.name, self.email == other_user.name, other_user.email
        # check if you can check: self.name, self.email == o.name, o.email

    # adds the book and rating to the dictionary
    def read_book(self, book, rating=None):
        self.books[book] = rating

    # Iterates through the dictionary, books, and calculates the average rating for all the books
    def get_average_rating(self):
        # returns a float value
        return sum([rating for rating in self.books.values() if rating is not None]) / len(self.books)


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Empty dictionary that is going to hold the user's rating of the book
        self.books = {}

    # Method that returns an email on the user
    def get_email(self):
        return self.email

    # Method to change the email on the selected user
    def change_email(self, address):
        self.email = address

    def __repr__(self):
        pass

    def __eq__(self, other_user):
        pass
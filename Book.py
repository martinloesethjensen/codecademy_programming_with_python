class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        # List with all the ratings for the book
        self.ratings = []

    # Method to return the title of the book
    def get_title(self):
        return self.title

    # Returns the ISBN number
    def get_isbn(self):
        return self.isbn

    # Sets new ISBN number for the book
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been changed to: {isbn}".format(isbn=new_isbn)

    # Method to add a rating to ratings list if it's a valid number
    def add_rating(self, rating):

        # What to do about rating being a NoneType?
        try:
            if 0 <= rating <= 4:
                self.ratings.append(rating)
            else:
                return "Invalid Rating."
        except TypeError:
            "Invalid Type."

    def __repr__(self):
        return "Title: {book}\n" \
               "ISBN: {isbn}\n"\
            .format(book=self.title,
                    isbn=self.isbn)

    # The comparator to see if they are equal
    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn
        #Check for same in thhe TomeRater file __eq__ method

    # Calculates the average for the ratings for the book
    def get_average_rating(self):
        average = 0.0
        # [rating for rating in self.ratings]

        for rating in self.ratings:
            average += rating

        return average / len(self.ratings) # float(sum(avg) ...)

    # Returns a hash value for the book object
    def __hash__(self):
        return hash((self.title, self.isbn))

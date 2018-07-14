class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        # List with all the ratings for the book
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return "This book's ISBN has been changed to: {isbn}".format(isbn=new_isbn)

    def add_rating(self, rating):
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

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        return sum([rating for rating in self.ratings]) / len(self.ratings)

    # Returns a hash value for the book object
    def __hash__(self):
        return hash((self.title, self.isbn))

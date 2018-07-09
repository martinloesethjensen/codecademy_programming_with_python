from Book import Book


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "Title: {title}\n" \
               "Author: {author}\n" \
               "ISBN: {isbn}\n"\
            .format(title=self.title,
                    author=self.author,
                    isbn=self.isbn)

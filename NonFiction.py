from Book import Book


class NonFiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "Title: {title}\n" \
               "Level: {level}\n" \
               "Subject: {subject}\n" \
               "ISBN: {isbn}\n"\
            .format(title=self.title,
                    level=self.level,
                    subject=self.subject,
                    isbn=self.isbn)
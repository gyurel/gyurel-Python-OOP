class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):
        if book_name in library.books_available[author]:
            self.books.append(book_name)
            library.books_available[author].remove(book_name)
            if self.username in library.rented_books:
                library.rented_books[self.username][book_name] = days_to_return
            else:
                library.rented_books[self.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        return f'The book "{book_name}" is already rented and will be available in ' \
               f"{''.join([str(vl) for key, val in library.rented_books.items() for ky, vl in val.items() if ky == book_name])} days!"

    def return_book(self, author, book_name, library):
        if book_name in self.books:
            library.rented_books[self.username].pop(book_name)
            library.books_available[author].append(book_name)
            self.books.remove(book_name)

        return f"{self.username} doesn't have this book in his/her records!"

    def info(self):
        return f"{', '.join([x for x in self.books])}"

    def __str__(self):
        return f"{self.user_id}, {self.username}, {[x for x in self.books]}"

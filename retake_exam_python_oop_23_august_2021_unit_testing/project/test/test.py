from project.library import Library
from unittest import TestCase, main


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library('Library')

    def test_initialization_library_class(self):
        name = 'Library'
        books_by_author = {}
        readers = {}

        self.assertEqual(name, self.library.name)
        self.assertEqual(books_by_author, self.library.books_by_authors)
        self.assertEqual(readers, self.library.readers)

    def test_initialization_library_class_with_name_empty_string(self):
        name = ''

        with self.assertRaises(Exception) as context:
            self.library.name = name

        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test_add_book_if_author_not_in_books_by_author(self):
        author = 'Tolstoy'
        title = 'War and peace'
        expected = ['War and peace']
        self.library.add_book(author, title)

        self.assertEqual(expected, self.library.books_by_authors[author])

    def test_add_book_if_author_in_books_by_author_titel_not_in(self):
        author = 'Tolstoy'
        title = 'War and peace'
        second_title = 'Anna Karenina'
        expected = ['War and peace', 'Anna Karenina']
        self.library.add_book(author, title)
        self.library.add_book(author, second_title)

        self.assertEqual(expected, self.library.books_by_authors[author])

    def test_add_reader_if_the_name_not_in_readers(self):
        reader_name = 'Gosho'
        expected = []
        self.library.add_reader(reader_name)

        self.assertEqual(expected, self.library.readers[reader_name])

    def test_add_reader_if_the_name_is_already_in_readers(self):
        reader_name = 'Gosho'
        expected = f"{reader_name} is already registered in the {self.library.name} library."
        self.library.add_reader(reader_name)

        self.assertEqual(expected, self.library.add_reader(reader_name))

    def test_rent_book_if_reader_not_in_readers(self):
        reader_name = 'Gosho'
        book_author = 'Tolstoy'
        book_title = 'War and Peace'
        expected = f"{reader_name} is not registered in the {self.library.name} Library."

        self.assertEqual(expected, self.library.rent_book(reader_name, book_author, book_title))

    # def test_rent_book_if_reader_not_in_readers(self):
    #     reader_name = 'Gosho'
    #     book_author = 'Tolstoy'
    #     book_title = 'War and Peace'
    #     expected = f"{reader_name} is not registered in the {self.library.name} Library."
    #
    #     self.assertEqual(expected, self.library.rent_book(reader_name, book_author, book_title))

    def test_rent_book_if_book_author_not_in_books_by_author(self):
        reader_name = 'Gosho'
        book_author = 'Tolstoy'
        book_title = 'War and Peace'
        expected = f"{self.library.name} Library does not have any {book_author}'s books."

        self.library.add_reader(reader_name)

        self.assertEqual(expected, self.library.rent_book(reader_name, book_author, book_title))

    def test_rent_book_if_book_title_not_in_books_by_author(self):
        reader_name = 'Gosho'
        book_author = 'Tolstoy'
        book_title = 'War and Peace'
        missing_book = 'Anna Karenina'
        expected = f"""{self.library.name} Library does not have {book_author}'s "{missing_book}"."""
        self.library.add_book(book_author, book_title)
        self.library.add_reader(reader_name)

        self.assertEqual(expected, self.library.rent_book(reader_name, book_author, missing_book))

    def test_rent_book_if_reader_book_title_and_author_present_in_library(self):
        reader_name = 'Gosho'
        book_author = 'Tolstoy'
        first_book = 'War and Peace'
        second_book = 'Anna Karenina'
        self.library.add_reader(reader_name)
        self.library.add_book(book_author, first_book)
        self.library.add_book(book_author, second_book)
        expected_books_by_author = ['War and Peace']
        expected_reders = {'Gosho': [{'Tolstoy': 'Anna Karenina'}]}

        self.library.rent_book(reader_name, book_author, second_book)

        self.assertEqual(expected_reders, self.library.readers)
        self.assertEqual(expected_books_by_author, self.library.books_by_authors[book_author])


if __name__ == '__main__':
    main()

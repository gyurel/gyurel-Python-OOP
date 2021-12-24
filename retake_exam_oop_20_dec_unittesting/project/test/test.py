from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.current_movie = Movie('Name', 2000, 50)

    def test_standart_initialization_of_movie_with_correct_arguments(self):
        expected_name = 'Name'
        expected_year = 2000
        expected_rating = 50
        expected_actors = []

        self.assertEqual(expected_name, self.current_movie.name)
        self.assertEqual(expected_year, self.current_movie.year)
        self.assertEqual(expected_rating, self.current_movie.rating)
        self.assertEqual(expected_actors, self.current_movie.actors)

    def test_initialization_of_movie_with_empty_string_name(self):
        expected_result = "Name cannot be an empty string!"

        with self.assertRaises(ValueError) as context:
            Movie('', 2000, 50)

        self.assertEqual(expected_result, str(context.exception))

    def test_initialization_of_movie_with_not_valid_year(self):
        expected_result = "Year is not valid!"

        with self.assertRaises(ValueError) as context:
            Movie('Name', 1700, 50)

        self.assertEqual(expected_result, str(context.exception))

    def test_add_actor_when_name_not_already_in_list(self):
        name_to_add = 'Travolta'
        expected = ['Travolta']

        self.current_movie.add_actor(name_to_add)

        self.assertEqual(expected, self.current_movie.actors)

    def test_add_actor_returns_correct_message_when_actor_already_in_list(self):
        name_to_add = 'Travolta'
        expected = f"{name_to_add} is already added in the list of actors!"

        self.current_movie.add_actor(name_to_add)

        self.assertEqual(expected, self.current_movie.add_actor(name_to_add))

    def test_greater_than_returns_correct_message_when_current_movie_has_bigger_rating_than_new_movie(self):
        new_movie = Movie('NewName', 2000, 40)
        expected_message = f'"{self.current_movie.name}" is better than "{new_movie.name}"'

        self.assertEqual(expected_message, self.current_movie > new_movie)

    def test_greater_than_returns_correct_message_when_new_movie_has_equal_rating_than_current(self):
        new_movie = Movie('NewName', 2000, 50)
        expected_message = f'"{new_movie.name}" is better than "{self.current_movie.name}"'

        self.assertEqual(expected_message, self.current_movie > new_movie)

    def test_greater_than_returns_correct_message_when_new_movie_has_bigger_rating_than_current(self):
        new_movie = Movie('NewName', 2000, 60)
        expected_message = f'"{new_movie.name}" is better than "{self.current_movie.name}"'

        self.assertEqual(expected_message, self.current_movie > new_movie)

    def test_represent_method_returns_correct_string(self):
        expected_name = 'Name'
        expected_year = 2000
        expected_rating = 50
        expected_actors = 'Travolta, Stalone, Capone'
        expected = f"Name: {expected_name}\n" \
               f"Year of Release: {expected_year}\n" \
               f"Rating: {expected_rating:.2f}\n" \
               f"Cast: {expected_actors}"

        self.current_movie.add_actor('Travolta')
        self.current_movie.add_actor('Stalone')
        self.current_movie.add_actor('Capone')

        self.assertEqual(expected, repr(self.current_movie))


if __name__ == '__main__':
    main()

from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestingMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal('name', 'mammal_type', 'sound')

    def test_mammal_initialization(self):
        name = 'Name'
        mammal_type = 'Type'
        sound = 'Sound'

        mammal = Mammal(name, mammal_type, sound)

        self.assertEqual(name, mammal.name)
        self.assertEqual(mammal_type, mammal.type)
        self.assertEqual(sound, mammal.sound)
        self.assertEqual("animals", mammal._Mammal__kingdom)

    def test_make_sound_method__if_returns_a_proper_string(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()

        self.assertEqual(expected, actual)

    def test_get_kingdom_method__should_return_animals(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_method__if_returns_a_proper_string(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()

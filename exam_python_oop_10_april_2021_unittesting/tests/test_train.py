from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train('PufPaf', 3)

    def test_initialization(self):
        name = 'PufPaf'
        capacity = 3
        TRAIN_FULL = "Train is full"
        PASSENGER_EXISTS = "Passenger {} Exists"
        PASSENGER_NOT_FOUND = "Passenger Not Found"
        PASSENGER_ADD = "Added passenger {}"
        PASSENGER_REMOVED = "Removed {}"
        ZERO_CAPACITY = 0

        self.assertEqual(name, self.train.name)
        self.assertEqual(capacity, self.train.capacity)
        self.assertEqual(TRAIN_FULL, self.train.TRAIN_FULL)
        self.assertEqual(PASSENGER_EXISTS, self.train.PASSENGER_EXISTS)
        self.assertEqual(PASSENGER_NOT_FOUND, self.train.PASSENGER_NOT_FOUND)
        self.assertEqual(PASSENGER_ADD, self.train.PASSENGER_ADD)
        self.assertEqual(PASSENGER_REMOVED, self.train.PASSENGER_REMOVED)
        self.assertEqual(ZERO_CAPACITY, self.train.ZERO_CAPACITY)

    def test_add_method_if_no_more_capacity_raises_value_error(self):
        self.train.add('Pesho')
        self.train.add('Gosho')
        self.train.add('Nasko')
        expected = "Train is full"

        with self.assertRaises(ValueError) as context:
            self.train.add('Gancho')

        self.assertEqual(expected, str(context.exception))

    def test_if_add_method_raises_when_passenger_name_already_in_passengers(self):
        passenger_name = 'Pesho'
        base_string = "Passenger {} Exists"
        expected_string = base_string.format(passenger_name)
        self.train.add(passenger_name)
        expected = "Train is full"

        with self.assertRaises(ValueError) as context:
            self.train.add(passenger_name)

        self.assertEqual(expected_string, str(context.exception))

    def test_if_add_method_adds_the_passenger_if_there_is_capacity_and_passenger_not_yet_in_passengers(self):
        passenger_name = 'Pesho'
        base_string = "Added passenger {}"
        expected_string = base_string.format(passenger_name)
        expected_passangers = ['Pesho']

        self.assertEqual(expected_string, self.train.add(passenger_name))
        self.assertEqual(expected_passangers, self.train.passengers)

    def test_remove_method_if_raises_value_error_when_passenger_not_in_passengers(self):
        passenger_name = 'Pesho'
        base_string = "Passenger Not Found"
        expected_string = base_string.format(passenger_name)

        with self.assertRaises(ValueError) as context:
            self.train.remove(passenger_name)

        self.assertEqual(expected_string, str(context.exception))

    def test_remove_method_if_removes_existing_passenger(self):
        passenger_name = 'Pesho'
        base_string = "Removed {}"
        expected_string = base_string.format(passenger_name)
        self.train.add(passenger_name)

        self.assertEqual(expected_string, self.train.remove(passenger_name))

if __name__ == '__main__':
    main()

from unittest import TestCase, main
from vehicle.project.vehicle import Vehicle


class TestingVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(100, 200)

    def test_vehicle_initialization(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(200, self.vehicle.horse_power)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_method_drive_should_raise_exeption_when_not_enough_fuel(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        with self.assertRaises(Exception) as context:
            self.vehicle.drive(max_distance + 1)

        self.assertEqual("Not enough fuel", str(context.exception))

    def test_method_drive_should_reduse_fuel_if_there_is_enough_for_the_distance(self):
        max_distance = self.vehicle.fuel / self.vehicle.fuel_consumption

        self.vehicle.drive(max_distance)
        self.assertEqual(0, self.vehicle.fuel)

    def test_method_refuel_should_raise_exeption_when_not_enough_capacity(self):

        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(101)

        self.assertEqual("Too much fuel", str(context.exception))

    def test_method_refuel_sould_add_the_fuel_if_there_is_sufficient_capacity(self):
        kilometers_to_drive_with_20_liters = 20 / self.vehicle.fuel_consumption

        start_fuel_level = self.vehicle.fuel
        self.vehicle.drive(kilometers_to_drive_with_20_liters)
        fuel_after_driving = start_fuel_level - 20

        expected_after_recharch_10 = fuel_after_driving + 10
        self.vehicle.refuel(10)

        self.assertEqual(expected_after_recharch_10, self.vehicle.fuel)

    def test__str__method_if_returns_proper_string(self):
        expected = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        actual = self.vehicle.__str__()

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()

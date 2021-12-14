from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race





class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        self.cars.append(self.create_car_object(car_type, model, speed_limit))
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                current_driver = driver

        if current_driver is None:
            raise Exception(f"Driver {driver_name} could not be found!")

        currnet_car = None
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type and not car.is_taken:
                currnet_car = car
                break

        if currnet_car is None:
            raise Exception(f"Car {car_type} could not be found!")

        if current_driver.car is not None:
            current_car_model = current_driver.car.model
            new_car_model = currnet_car.model
            current_driver.car.is_taken = False
            current_driver.car = currnet_car
            currnet_car.is_taken = True
            return f"Driver {current_driver.name} changed his car from {current_car_model} to {new_car_model}."

        current_driver.car = currnet_car
        currnet_car.is_taken = True
        return f"Driver {driver_name} chose the car {currnet_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        current_race = self.find_race(race_name)
        current_driver = self.find_driver(driver_name)

        if current_driver.car is None:
            raise Exception(f"Driver {current_driver.name} could not participate in the race!")

        if current_driver in current_race.drivers:
            return f"Driver {current_driver.name} is already added in {race_name} race."

        current_race.drivers.append(current_driver)
        return f"Driver {current_driver.name} added in {current_race.name} race."

    def start_race(self, race_name: str):
        race_to_start = self.find_race(race_name)

        if len(race_to_start.drivers) < 3:
            raise Exception(f"Race {race_to_start.name} cannot start with less than 3 participants!")

        fastest_3 = [x for x in sorted(race_to_start.drivers, key=lambda x: -x.car.speed_limit)][:3]

        return_string = []
        for x in fastest_3:
            x.number_of_wins += 1
            return_string.append(f"Driver {x.name} wins the {race_to_start.name} race with a speed of {x.car.speed_limit}.")

        return '\n'.join(x for x in return_string)

    def create_car_object(self, car_type, model, speed_limit):
        if car_type == "SportsCar":
            return SportsCar(model, speed_limit)
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)

    def find_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return race
        raise Exception(f"Race {race_name} could not be found!")

    def find_driver(self, driver_name):
        for drvr in self.drivers:
            if drvr.name == driver_name:
                return drvr
        raise Exception(f"Driver {driver_name} could not be found!")

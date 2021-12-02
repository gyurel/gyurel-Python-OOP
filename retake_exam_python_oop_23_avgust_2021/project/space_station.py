from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type, name):
        if Biologist.__name__ == astronaut_type or Geodesist.__name__ == astronaut_type \
                or Meteorologist.__name__ == astronaut_type:

            for astronaut in self.astronaut_repository.astronauts:
                if astronaut.name == name:
                    return f"{name} is already added."

            self.astronaut_repository.add(self.__create_astronaut(astronaut_type, name))
            return f"Successfully added {astronaut_type}: {name}."

        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items):
        for planet in self.planet_repository.planets:
            if planet.name == name:
                return f"{name} is already added."

        current_planet = Planet(name)
        [current_planet.items.append(item) for item in items.split(', ')]
        self.planet_repository.planets.append(current_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                self.astronaut_repository.astronauts.remove(astronaut)
                return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name):
        found_planet = False
        current_planet = None

        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                current_planet = planet
                found_planet = True

        if not found_planet:
            raise Exception("Invalid planet name!")

        chosen_astronauts = sorted([astronaut for astronaut in self.astronaut_repository.astronauts
                                   if astronaut.oxygen > 30], key=lambda astronaut: astronaut.oxygen, reverse=True)[0:5]

        if len(chosen_astronauts) == 0:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_participated = 0
        while chosen_astronauts:
            current_astronaut = chosen_astronauts.pop(0)
            astronauts_participated += 1

            while current_astronaut.oxygen > 0:
                current_astronaut.backpack.append(current_planet.items.pop())
                current_astronaut.breathe()

                if len(current_planet.items) == 0:
                    self.successful_missions += 1
                    return f"Planet: {planet_name} was explored. {astronauts_participated} " \
                           f"astronauts participated in collecting items."

        if len(current_planet.items) > 0:
            self.failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = f"{self.successful_missions} successful missions!\n"
        result += f"{self.failed_missions} missions were not completed!\n"
        result += "Astronauts' info:\n"

        for astro in self.astronaut_repository.astronauts:
            result += f"Name: {astro.name}\nOxygen: {astro.oxygen}\n"
            if len(astro.backpack) == 0:
                result += "none\n"
            else:
                result += f"Backpack items: {', '.join([x for x in astro.backpack])}\n"
        return result.strip()

    @staticmethod
    def __create_astronaut(astronaut_type, name):
        if astronaut_type == Biologist.__name__:
            return Biologist(name)
        if astronaut_type == Geodesist.__name__:
            return Geodesist(name)
        if astronaut_type == Meteorologist.__name__:
            return Meteorologist(name)

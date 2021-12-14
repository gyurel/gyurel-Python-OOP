from project.car.car import Car


class MuscleCar(Car):
    MIN_SPEED_LIMIT = 250
    MAX_SPEED_LIMIT = 450

    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    def is_valid(self, value, min_limit, max_limit):
        if value < self.MIN_SPEED_LIMIT or self.MAX_SPEED_LIMIT < value:
            raise ValueError(f"Invalid speed limit! Must be between {self.MIN_SPEED_LIMIT} and {self.MAX_SPEED_LIMIT}!")
        return value

    # @property
    # def speed_limit(self):
    #     return self.__speed_limit
    #
    # @speed_limit.setter
    # def speed_limit(self, value):
    #     self.is_valid(value, self.MIN_SPEED_LIMIT, self.MAX_SPEED_LIMIT)
    #     self.__speed_limit = value
    #

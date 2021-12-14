from abc import ABC, abstractmethod


class Car(ABC):
    MIN_SPEED_LIMIT = None
    MAX_SPEED_LIMIT = None

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @abstractmethod
    def is_valid(self, value, min_limit, max_limit):
        pass
        # if value < cls.MIN_SPEED_LIMIT or cls.MAX_SPEED_LIMIT < value:
        #     raise ValueError(f"Invalid speed limit! Must be between {cls.MIN_SPEED_LIMIT} and {cls.MAX_SPEED_LIMIT}!")
        # return value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(list(value)) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        self.is_valid(value, self.MIN_SPEED_LIMIT, self.MAX_SPEED_LIMIT)
        self.__speed_limit = value

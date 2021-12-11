from project.table.table import Table


class InsideTable(Table):
    __TABLE_NUMBER_MESSAGE = "Inside table's number must be between 1 and 50 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 1 or value > 50:
            raise ValueError(self.__TABLE_NUMBER_MESSAGE)
        self.__table_number = value

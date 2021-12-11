from project.table.table import Table


class OutsideTable(Table):
    __TABLE_NUMBER_MESSAGE = "Outside table's number must be between 51 and 100 inclusive!"

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 51 or value > 100:
            raise ValueError(self.__TABLE_NUMBER_MESSAGE)
        self.__table_number = value

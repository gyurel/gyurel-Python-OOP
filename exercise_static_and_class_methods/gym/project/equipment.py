class Equipment:
    id = 1

    def __init__(self, name):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        current = Equipment.id
        Equipment.id += 1
        return current

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

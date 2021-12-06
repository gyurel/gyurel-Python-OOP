class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    # TODO: check if the argument passed is an object
    def remove(self, decoration):
        for el in self.decorations:
            if el == decoration:
                self.decorations.remove(el)
                return True
        return False

    def find_by_type(self, decoration_type: str):
        for el in self.decorations:
            if el.__class__.__name__ == decoration_type:
                return el
        return "None"

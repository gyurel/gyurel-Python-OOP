class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if len(self.animals) == self.__animal_capacity:
            return "Not enough space for animal"

        if price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self. __budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) == self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"

        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = 0
        for worker in self.workers:
            total_salaries += worker.salary

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"

        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_expenses = 0
        for animal in self.animals:
            expenses = animal.money_for_care
            total_expenses += expenses

        if self.__budget >= total_expenses:
            self.__budget -= total_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def __types_of_objects(self, obj_list, obj_type):
        objects_str = [str(x) for x in obj_list if x.__class__.__name__ == obj_type]

        result = f"----- {len(objects_str)} {obj_type}s:" + "\n"

        for obj_str in objects_str:
            result += obj_str
            result += "\n"

        return result

    def animals_status(self):
        result = f"You have {len(self.animals)} animals" + "\n"

        result += self.__types_of_objects(self.animals, 'Lion')
        result += self.__types_of_objects(self.animals, 'Tiger')
        result += self.__types_of_objects(self.animals, 'Cheetah')

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers" + "\n"

        result += self.__types_of_objects(self.workers, 'Keeper')
        result += self.__types_of_objects(self.workers, 'Caretaker')
        result += self.__types_of_objects(self.workers, 'Vet')

        return result.strip()

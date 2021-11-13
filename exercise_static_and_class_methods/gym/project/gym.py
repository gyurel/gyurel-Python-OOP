class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        info = ''
        current_subscription = self.get_object_by_id(subscription_id, self.subscriptions)
        info += str(current_subscription) + '\n'
        current_customer = self.get_object_by_id(current_subscription.customer_id, self.customers)
        info += str(current_customer) + '\n'
        current_trainer = self.get_object_by_id(current_subscription.trainer_id, self.trainers)
        info += str(current_trainer) + '\n'
        current_plan = self.get_object_by_id(current_subscription.exercise_id, self.plans)
        current_equipment = self.get_object_by_id(current_plan.equipment_id, self.equipment)
        info += str(current_equipment) + '\n'
        info += str(current_plan)

        return info

    @staticmethod
    def get_object_by_id(current_id, list_of_objects):
        for obj in list_of_objects:
            if obj.id == current_id:
                return obj

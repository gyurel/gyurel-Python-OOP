class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer):
        if len(self.customers) < self.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd):
        if len(self.dvds) < self.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)

        if self.__get_object_by_id(customer.rented_dvds, dvd_id):
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return f"DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self.__get_object_by_id(self.customers, customer_id)
        dvd = self.__get_object_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        customers = '\n'.join([str(x) for x in self.customers])
        dvds = '\n'.join([str(x) for x in self.dvds])

        return customers + '\n' + dvds

    @staticmethod
    def __get_object_by_id(objects_collection, id):
        for obj in objects_collection:
            if obj.id == id:
                return obj

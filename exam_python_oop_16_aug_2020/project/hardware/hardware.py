class Hardware:

    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: list = []
        self.initial_capacity = capacity
        self.initial_memory = memory

    def install(self, software):
        if software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")
        if software.memory_consumption > self.memory:
            raise Exception("Software cannot be installed")

        self.software_components.append(software)
        self.capacity -= software.capacity_consumption
        self.memory -= software.memory_consumption


    def uninstall(self, software):
        self.software_components.remove(software)
        self.capacity += software.capacity_consumption
        self.memory += software.memory_consumption

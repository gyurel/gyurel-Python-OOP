from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware = None
        for h_ware in System._hardware:
            if h_ware.name == hardware_name:
                current_hardware = h_ware

        if current_hardware is None:
            return "Hardware does not exist"

        current_software = ExpressSoftware(name, capacity_consumption, memory_consumption)

        current_hardware.install(current_software)

        System._software.append(current_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        current_hardware = None
        for h_ware in System._hardware:
            if h_ware.name == hardware_name:
                current_hardware = h_ware

        if current_hardware is None:
            return "Hardware does not exist"

        current_software = LightSoftware(name, capacity_consumption, memory_consumption)

        current_hardware.install(current_software)

        System._software.append(current_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_hardware = None
        for h_ware in System._hardware:
            if h_ware.name == hardware_name:
                current_hardware = h_ware

        current_software = None
        for s_ware in System._software:
            if s_ware.name == software_name:
                current_software = s_ware

        if current_hardware is None or current_software is None:
            return "Some of the components do not exist"

        current_hardware.uninstall(current_software)
        System._software.remove(current_software)

    @staticmethod
    def analyze():
        result = f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([x.memory_consumption for x in System._software])}\
 / {sum([x.initial_memory for x in System._hardware])}
Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])}\
 / {sum([x.initial_capacity for x in System._hardware])}"""
        return result

    @staticmethod
    def system_split():
        string_list = []

        for h_ware in System._hardware:
            string_list.append(f"Hardware Component - {h_ware.name}")
            string_list.append(f"Express Software Components: \
{len([x for x in h_ware.software_components if x.__class__.__name__ == 'ExpressSoftware'])}")
            string_list.append(f"Light Software Components: \
{len([x for x in h_ware.software_components if x.__class__.__name__ == 'LightSoftware'])}")
            string_list.append(f"Memory Usage: \
{sum([x.memory_consumption for x in h_ware.software_components])} / {h_ware.initial_memory}")
            string_list.append(f"Capacity Usage: \
{sum([x.capacity_consumption for x in h_ware.software_components])} / {h_ware.initial_capacity}")
            string_list.append(f"Type: {h_ware.hardware_type}")
            # string_list.append(f"Software Components: {', '.join([x.name for x in h_ware.software_components])}")
            result = []
            for x in h_ware.software_components:
                result.append(x.name)
            if len(result) > 0:
                string_list.append(f"Software Components: {', '.join(x for x in result)}")
            else:
                string_list.append(f"Software Components: 'None'")

        return '\n'.join([x for x in string_list])

from project.space_station import SpaceStation


new_spacestation = SpaceStation()
print(new_spacestation.add_astronaut('Biologist', 'BioOne'))
print(new_spacestation.add_astronaut('Biologist', 'BioTwo'))
print(new_spacestation.add_astronaut('Meteorologist', 'MeteoOne'))
print(new_spacestation.add_astronaut('Meteorologist', 'MeteoTwo'))
print(new_spacestation.add_astronaut('Meteorologist', 'MeteoThree'))
print(new_spacestation.add_astronaut('Biologist', 'BioThree'))
print(new_spacestation.add_astronaut('Biologist', 'BioFour'))
print(new_spacestation.add_astronaut('Geodesist', 'GeoOne'))
print(new_spacestation.add_astronaut('Geodesist', 'GeoTwo'))

print(new_spacestation.add_planet('Mars', 'diamon, saphir, gold, silver, cobalt, cooper, platin, gas, lava'))
print(new_spacestation.send_on_mission('Mars'))
print(new_spacestation.report())

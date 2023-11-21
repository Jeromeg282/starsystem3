import random
import sqlite3

class stargeneration():
    def __init__(self):
        self.mainworld = 0
        self.atmosphere = 0
        self.populus = 0
        self.hydros = 0
        self.gov = 0
        self.techlevel = 0
        self.lawlevel = 0
        self.info = {"dice roll": self.mainworld}

    def load_definitions(self, filename):
        with open(filename, 'r') as file:
            definitions = dict(line.strip().split(':') for line in file.readlines())
        return definitions

    def get_definition(self, value, definitions):
        return definitions.get(value, "Undefined")

    def generate_data(self):
        self.mainworld = (random.randint(1, 6) + random.randint(1, 6) - 2)
        self.atmosphere = (random.randint(1, 6) + random.randint(1, 6) - 7 + self.mainworld)
        if self.mainworld == 0:
            self.atmosphere = 0
        self.hydros = (random.randint(1, 6) + random.randint(1, 6) - 7 + self.mainworld)
        self.populus = (random.randint(1, 6) + random.randint(1, 6) - 2)
        self.gov = (random.randint(1, 6) + random.randint(1, 6) - 7 + self.populus)
        self.lawlevel = (random.randint(1, 6) + random.randint(1, 6) - 7 + self.gov)
        self.info = {
            "mainworld": self.get_definition(self.mainworld, self.load_definitions('mainworld_definitions.txt')),
            "atmosphere": self.get_definition(self.atmosphere, self.load_definitions('atmosphere_definitions.txt')),
            "hydros": self.get_definition(self.hydros, self.load_definitions('hydros_definitions.txt')),
            "populus": self.get_definition(self.populus, self.load_definitions('populus_definitions.txt')),
            "gov": self.get_definition(self.gov, self.load_definitions('gov_definitions.txt')),
            "lawlevel": self.get_definition(self.lawlevel, self.load_definitions('lawlevel_definitions.txt'))
        }

# Example usage:
if __name__ == "__main__":
    data_generator = stargeneration()
    data_generator.generate_data()
    print(data_generator.info)

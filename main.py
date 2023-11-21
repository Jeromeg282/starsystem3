#Python3







import random

class StarSystemGenerator:
    def __init__(self, file_path):
        self.system_contents_table = self.read_system_contents_table(file_path)

    def roll_dice(self, sides):
        return random.randint(1, sides)

    def read_system_contents_table(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = [eval(line.strip()) for line in file]
            print(f"Data read from file: {data}")
            return data
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None
        except Exception as e:
            print(f"Error reading system contents table: {e}")
            return None


    def generate_star_system(self):
        system = random.choice(self.system_contents_table)

        die_roll = int(system["Die"])

        starport_die = self.roll_dice(6)
        if starport_die <= 2:
            system["Starport"] = "A"
        elif starport_die <= 4:
            system["Starport"] = "B"
        elif starport_die <= 6:
            system["Starport"] = "C"

        if system["Starport"] not in ["C", "D", "E", "X"]:
            system["Navel"] = "yes"

        if system["Starport"] not in ["E", "X"]:
            scout_base_die = self.roll_dice(6)
            if system["Starport"] == "C":
                scout_base_die -= 1
            elif system["Starport"] == "B":
                scout_base_die -= 2
            elif system["Starport"] == "A":
                scout_base_die -= 3

            if scout_base_die > 0:
                system["Scout"] = "yes"

        if self.roll_dice(6) <= 4:
            system["Gas"] = "no"

        main_world_name = f"Main World {die_roll}"

        main_world_upp = {
            "Starport": system["Starport"],
            "Size": self.roll_dice(6) + self.roll_dice(6) - 2,
            "Atmosphere": max(0, self.roll_dice(6) + self.roll_dice(6) - 7 + main_world_upp["Size"]),
            "Hydrographics": max(0, self.roll_dice(6) + self.roll_dice(6) - 7 + main_world_upp["Size"] - 4),
            "Population": self.roll_dice(6) + self.roll_dice(6) - 2,
            "Government": self.roll_dice(6) + self.roll_dice(6) - 7 + main_world_upp["Population"],
            "Law Level": self.roll_dice(6) + self.roll_dice(6) - 7 + main_world_upp["Government"],
            "Tech Level": self.roll_dice(6) + 4  
        }

        print("Star System Statistics:")
        print(system)
        print(f"Main World Name: {main_world_name}")
        print("Main World UPP:")
        print(main_world_upp)

# File path to the text file containing the system contents table
txt_file_path = "die.txt"

generator = StarSystemGenerator(txt_file_path)

# Generate a star system
generator.generate_star_system()










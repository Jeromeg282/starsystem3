import sqlite3
import random
import json
from enum import Enum


class StarportType(Enum):
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    X = 16


class StarSystem:
    def __init__(self, db_file='stardatabase.db') -> None:
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
        self.create_table_if_not_exists()

    def create_table_if_not_exists(self):
        query = """
        CREATE TABLE IF NOT EXISTS starsystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planetName TEXT,
            starport INT,
            navelbase BOOLEAN,
            gasgiant TEXT,
            planetoid INT,
            scoutbase TEXT,
            size INT,
            atm INT,
            hyd INT,
            population INT,
            govt INT,
            lawlvl INT,
            techlvl INT
        );
        """
        self.cursor.execute(query)

    def roll_dice(self, num=1):
        return [random.randint(1, 6) for _ in range(num)]

    def generate_starport_type(self):
        roll = sum(self.roll_dice(2))
        return StarportType(roll).value

    def generate_bool_based_on_roll(self, threshold):
        roll = sum(self.roll_dice(2))
        return roll > threshold

    def generate_name(self):
        return names.get_full_name()

    def generate_planet_size(self):
        return sum(self.roll_dice(2)) - 2

    def generate_atm(self, planet_size):
        if planet_size != 0:
            return (sum(self.roll_dice(2)) - 7) + planet_size
        return 0

    def generate_hyd(self, planet_size):
        hyd = (sum(self.roll_dice(2)) - 7) + planet_size
        return max(0, min(10, hyd)) if planet_size > 1 else 0

    def generate_population(self):
        return sum(self.roll_dice(2)) - 2

    def generate_govt(self, population):
        return (sum(self.roll_dice(2)) - 7) + population

    def generate_law_lvl(self, govt):
        return (sum(self.roll_dice(2)) - 7) + govt

    def generate_tech_lvl(self, starport, planet_size, atm, hyd, population, govt):
        tech_lvl = sum(self.roll_dice(1))

        if starport == StarportType.A.value:
            tech_lvl += 6
        elif starport == StarportType.B.value:
            tech_lvl += 4
        elif starport == StarportType.C.value:
            tech_lvl += 2
        elif starport == StarportType.X.value:
            tech_lvl -= 4

        if planet_size in {0, 1}:
            tech_lvl += 2
        elif planet_size in {2, 3, 4}:
            tech_lvl += 1

        if atm < 4:
            tech_lvl += 1
        if 9 < atm < 15:
            tech_lvl += 1
        if hyd == 9:
            tech_lvl += 1
        if hyd == 10:
            tech_lvl += 2
        if 0 < population < 6:
            tech_lvl += 1
        if population == 9:
            tech_lvl += 2
        if population == 10:
            tech_lvl += 4
        if govt == 0:
            tech_lvl += 1
        if govt == 5:
            tech_lvl += 1
        if govt == 13:
            tech_lvl -= 2

        return tech_lvl

    def insert_into_database(self):
        query = f"INSERT INTO starsystem (planetname,starport,navelbase,gasgiant,planetoid,scoutbase,size,atm,hyd,population,govt,lawlvl,techlvl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
        values = (self.generate_name(), self.generate_starport_type(), self.generate_bool_based_on_roll(7),
                  self.generate_bool_based_on_roll(9), self.generate_bool_based_on_roll(6), self.generate_planet_size(),
                  self.generate_atm(0), self.generate_hyd(0), self.generate_population(),
                  self.generate_govt(0), self.generate_law_lvl(0), self.generate_tech_lvl(0, 0, 0, 0, 0, 0))

        self.cursor.execute(query, values)
        self.connection.commit()

    def pretty_print(self):
        query = "SELECT * FROM starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()

        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Planetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)


class CreateUniverse:
    def __init__(self) -> None:
        self.star_system = StarSystem()
        self.search_query()

    def search_query(self):
        print("The options to search for are: planetName (1), size (2), atm (3), hyd (4), population (5), govt (6), lawlvl (7), techlvl (8), getall (9), run Create Star (10)")
        try:
            self.selection = int(input("Enter what you want to search for: "))
        except ValueError:
            self.search_query()

        self.symbol = input("Enter the symbol you want to search with, ex: >, <, = : ")
        if self.selection == 1:
            self.search_name()
        elif self.selection == 2:
            self.search_size()
        elif self.selection == 3:
            self.search_atm()
        elif self.selection == 4:
            self.search_hyd()
        elif self.selection == 5:
            self.search_pop()
        elif self.selection == 6:
            self.search_gov()
        elif self.selection == 7:
            self.search_law()
        elif self.selection == 8:
            self.search_tech()
        elif self.selection == 9:
            self.get_all()
        elif self.selection == 10:
            self.create_star()
        else:
            self.search_query()

    def search_tech(self):
        try:
            tech_select = int(input(f"Enter the tech level that you want to find {self.symbol} results for: "))
        except ValueError:
            self.search_tech()

        query = f"SELECT * FROM starsystem WHERE techlvl {self.symbol}={tech_select}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_name(self):
        name = input("Enter the planet name you want to search for: ")
        name = f"'{name}'"
        query = f"SELECT * FROM starsystem WHERE planetName{self.symbol}={name}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def get_all(self):
        query = f"SELECT * FROM starsystem"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def pretty_print_result(self, result):
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Planetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)

    def create_star(self):
        self.star_system.insert_into_database()
        self.search_query()

    def search_size(self):
        try:
            size = int(input("Enter the planet size you want to search for: "))
        except ValueError:
            self.search_size()

        query = f"SELECT * FROM starsystem WHERE size{self.symbol}={size}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_atm(self):
        try:
            atm = int(input("Enter the planet atmosphere you want to search for: "))
        except ValueError:
            self.search_atm()

        query = f"SELECT * FROM starsystem WHERE atm{self.symbol}={atm}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_hyd(self):
        try:
            hyd = int(input("Enter the planet hydrogeneics you want to search for: "))
        except ValueError:
            self.search_hyd()

        query = f"SELECT * FROM starsystem WHERE hyd{self.symbol}={hyd}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_pop(self):
        try:
            pop = int(input("Enter the planet population you want to search for: "))
        except ValueError:
            self.search_pop()

        query = f"SELECT * FROM starsystem WHERE population{self.symbol}={pop}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_gov(self):
        try:
            govt = int(input("Enter the planet govt you want to search for: "))
        except ValueError:
            self.search_gov()

        query = f"SELECT * FROM starsystem WHERE govt{self.symbol}={govt}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)

    def search_law(self):
        try:
            law = int(input("Enter the planet law level you want to search for: "))
        except ValueError:
            self.search_law()

        query = f"SELECT * FROM starsystem WHERE lawlvl{self.symbol}={law}"
        self.star_system.cursor.execute(query)
        result = self.star_system.cursor.fetchall()
        self.pretty_print_result(result)


if __name__ == "__main__":
    CreateUniverse()

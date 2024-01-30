import sqlite3
import random
import json
import names

class Star:
    def __init__(self) -> None:
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.create_table()
        self.populate_database()
        self.look_pretty()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS starsystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planetName TEXT,
            starport INTEGER,
            navelbase BOOLEAN,
            gasgiant TEXT,
            planetoid INTEGER,
            scoutbase TEXT,
            size INTEGER,
            atm INTEGER,
            hyd INTEGER,
            population INTEGER,
            govt INTEGER,
            lawlvl INTEGER,
            techlvl INTEGER
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def populate_database(self):
        query = f"""
        INSERT INTO starsystem (planetname, starport, navelbase, gasgiant, planetoid, scoutbase, size, atm, hyd, population, govt, lawlvl, techlvl)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        self.cursor.execute(query, self.generate_star_data())
        self.connection.commit()

    def look_pretty(self):
        query = "SELECT * FROM starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}  Naval Base: {i[3]}\nGasGiant: {i[4]}  Plantetoid: {i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}  Hydrogeneics: {i[9]}\nPopulation: {i[10]}  Government: {i[11]}\nLaw level: {i[12]}  Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)

    def generate_star_data(self):
        return (
            names.get_full_name(),
            self.starport_type(),
            self.is_navel_base(),
            self.is_gas_giant(),
            self.is_planetoids(),
            self.is_scout_base(),
            self.generate_planet_size(),
            self.generate_atm(),
            self.generate_hyd(),
            self.generate_population(),
            self.generate_govt(),
            self.law_level(),
            self.tech_level()
        )

    def dice(self, num=1):
        return [random.randint(1, 6) for _ in range(num)]

    def starport_type(self):
        roll = sum(self.dice(2))
        if roll <= 4:
            return 10
        elif roll <= 6:
            return 11
        elif roll <= 8:
            return 12
        elif roll == 9:
            return 13
        elif roll <= 11:
            return 14
        else:
            return 16

    def is_navel_base(self):
        return sum(self.dice(2)) > 7

    def is_gas_giant(self):
        return sum(self.dice(2)) <= 9

    def is_planetoids(self):
        return sum(self.dice(2)) <= 6

    def is_scout_base(self):
        return sum(self.dice(2)) > 6

    def generate_planet_size(self):
        return sum(self.dice(2)) - 2

    def generate_atm(self):
        return max(0, sum(self.dice(2)) - 7 + self.generate_planet_size())

    def generate_hyd(self):
        hyd = max(0, sum(self.dice(2)) - 7 + self.generate_planet_size())
        return min(10, hyd)

    def generate_population(self):
        return sum(self.dice(2)) - 2

    def generate_govt(self):
        return sum(self.dice(2)) - 7 + self.generate_population()

    def law_level(self):
        return sum(self.dice(2)) - 7 + self.generate_govt()

    def tech_level(self):
        techlvl = sum(self.dice(1))
        if self.starport_type() == 10:
            techlvl += 6
        elif self.starport_type() == 11:
            techlvl += 4
        elif self.starport_type() == 12:
            techlvl += 2
        elif self.starport_type() == 16:
            techlvl -= 4
        if self.generate_planet_size() in (0, 1):
            techlvl += 2
        elif self.generate_planet_size() in (2, 3, 4):
            techlvl += 1
        if self.generate_atm() < 4:
            techlvl += 1
        if 9 < self.generate_atm() < 15:
            techlvl += 1
        if self.generate_hyd() == 9:
            techlvl += 1
        if self.generate_hyd() == 10:
            techlvl += 2
        if 0 < self.generate_population() < 6:
            techlvl += 1
        if self.generate_population() == 9:
            techlvl += 2
        if self.generate_population() == 10:
            techlvl += 4
        if self.generate_govt() == 0:
            techlvl += 1
        if self.generate_govt() == 5:
            techlvl += 1
        if self.generate_govt() == 13:
            techlvl -= 2
        return techlvl

class CreateUniverse:
    def __init__(self) -> None:
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.search_query()

    def search_query(self):
        print("Options to search for: planetName (1), size (2), atm (3), hyd (4), population (5), govt (6), lawlvl (7), techlvl (8), getall (9), run Create Star (10)")
        try:
            selection = int(input("Enter what you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.search_query()
            return

        symbol = input("Enter the symbol you want to search with, ex: >, <, = : ")
        if selection in (1, 2, 3, 4, 5, 6, 7, 8):
            self.search(selection, symbol)
        elif selection == 9:
            self.get_all()
        elif selection == 10:
            Star()
        else:
            print("Invalid selection. Please choose a valid option.")
            self.search_query()

    def search(self, selection, symbol):
        try:
            value = int(input(f"Enter the value you want to find with {symbol}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.search_query()
            return

        query = f"SELECT * FROM starsystem WHERE {'planetName' if selection == 1 else 'size' if selection == 2 else 'atm' if selection == 3 else 'hyd' if selection == 4 else 'population' if selection == 5 else 'govt' if selection == 6 else 'lawlvl' if selection == 7 else 'techlvl'} {symbol} {value}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}  Naval Base: {i[3]}\nGasGiant: {i[4]}  Plantetoid: {i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}  Hydrogeneics: {i[9]}\nPopulation: {i[10]}  Government: {i[11]}\nLaw level: {i[12]}  Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.search_query()

    def get_all(self):
        query = "SELECT * FROM starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}  Naval Base: {i[3]}\nGasGiant: {i[4]}  Plantetoid: {i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}  Hydrogeneics: {i[9]}\nPopulation: {i[10]}  Government: {i[11]}\nLaw level: {i[12]}  Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.search_query()

if __name__ == "__main__":
    CreateUniverse()

import sqlite3
import random
import names
from prettytable import PrettyTable


class Star:
    def __init__(self):
        file = 'database.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS starsystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planetName TEXT,
            starport INT,
            navalbase BOOLEAN,
            gasgiant TEXT,
            planetoid INT,
            scoutbase BOOLEAN,
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
        self.planet_upp()
        query = "select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Num, Name, StarportLevel, NavelBase, GasGiant, ScoutBase, Size, Atm, Hyd, Population, Government, LawLevel, TechLevel\n")
        for i in result:
            print(i)
        

    def starport_type(self):
        roll = sum(self.dice(2))

        if roll in [2, 3, 4]:
            self.starport = 10
        elif roll in [5, 6]:
            self.starport = 11
        elif roll in [7, 8]:
            self.starport = 12
        elif roll == 9:
            self.starport = 13
        elif roll in [10, 11]:
            self.starport = 14
        elif roll == 12:
            self.starport = 16

        return self.starport

    def is_naval_base(self):
        roll = sum(self.dice(2))
        self.navalbase = roll > 7
        return self.navalbase

    def is_gas_giant(self):
        roll = sum(self.dice(2))
        self.gasgiant = roll > 9
        return self.gasgiant

    def is_planetoids(self):
        roll = sum(self.dice(2))
        self.planetoids = roll > 6
        return self.planetoids

    def is_scout_base(self):
        roll = sum(self.dice(2))
        self.scoutbase = roll > 6
        return self.scoutbase

    def gen_name(self):
        return names.get_first_name()

    def gen_planet_size(self):
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize

    def planet_upp(self):
        query = f"""
        INSERT INTO starsystem (
            planetName, starport, navalbase, gasgiant, planetoid, scoutbase,
            size, atm, hyd, population, govt, lawlvl, techlvl
        ) VALUES (
            '{self.gen_name()}', '{self.starport_type()}',
            '{self.is_naval_base()}', '{self.is_gas_giant()}',
            '{self.is_planetoids()}', '{self.is_scout_base()}',
            '{self.gen_planet_size()}', '{self.generate_atmosphere()}',
            '{self.generate_hydrosphere()}',
            '{self.generate_population()}', '{self.generate_government()}',
            '{self.generate_law_level()}', '{self.calculate_tech_lvl()}'
        );
        """
        self.cursor.execute(query)
        self.connection.commit()

    def dice(self, num=1):
        rand_list = []
        for i in range(num):
            die = random.randint(1, 6)
            rand_list.append(die)
        return rand_list

    def is_travel(self):
        pass

    def generate_atmosphere(self):
        if self.planetsize != 0:
            self.atm = max(0, sum(self.dice(2)) - 7 + self.planetsize)
        return self.atm

    def generate_hydrosphere(self):
        self.hyd = max(0, min(10, sum(self.dice(2)) - 7 + self.planetsize))
        return self.hyd

    def generate_population(self):
        self.population = max(0, sum(self.dice(2)) - 2)
        return self.population

    def generate_government(self):
        self.govt = max(0, sum(self.dice(2)) - 7 + self.population)
        return self.govt

    def generate_law_level(self):
        self.law = max(0, sum(self.dice(2)) - 7 + self.govt)
        return self.law

    def calculate_tech_lvl(self):
        self.techlvl = sum(self.dice(1))
        if self.starport == 10:
            self.techlvl += 6
        elif self.starport == 11:
            self.techlvl += 4
        elif self.starport == 12:
            self.techlvl += 2
        elif self.starport == 16:
            self.techlvl -= 4
        if self.planetsize in {0, 1}:
            self.techlvl += 2
        elif self.planetsize in {2, 3, 4}:
            self.techlvl += 1
        if self.atm < 4:
            self.techlvl += 1
        elif 9 < self.atm < 15:
            self.techlvl += 1
        if self.hyd == 9:
            self.techlvl += 1
        elif self.hyd == 10:
            self.techlvl += 2
        if 0 < self.population < 6:
            self.techlvl += 1
        elif self.population == 9:
            self.techlvl += 2
        elif self.population == 10:
            self.techlvl += 4
        if self.govt == 0:
            self.techlvl += 1
        elif self.govt == 5:
            self.techlvl += 1
        elif self.govt == 13:
            self.techlvl -= 2
        return self.techlvl


class UniverseGeneration:
    def __init__(self):
        self.file = 'database.db'
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()
        self.search_query()

    def search_query(self):
        print("""
            \n\n***************************Welcome to the Star Systems Console*****************************  
            \nThe menu options are: \n
            \033[38;5;221mOption[1]\033[0m <---Search By Planet Name---> 
            \033[38;5;221mOption[2]\033[0m <---Search By Planet Size--->
            \033[38;5;221mOption[3]\033[0m <---Search By Planet Atmosphere---> 
            \033[38;5;221mOption[4]\033[0m <---Search By Planet Hydrographics---> 
            \033[38;5;221mOption[5]\033[0m <---Search By Planet Population---> 
            \033[38;5;221mOption[6]\033[0m <---Search By Planet Government---> 
            \033[38;5;221mOption[7]\033[0m <---Search By Planet Law level---> 
            \033[38;5;221mOption[8]\033[0m <---Search By Planet Technical level--->  
            \033[38;5;221mOption[9]\033[0m <---Print All Planet Info--->  
            \033[38;5;221mOption[10]\033[0m <---Generate Star System--->              
            \n********************************************************************************************  
              
        """)
        try:
            self.selection = int(input("Please enter your menu option here: \n\n"))
        except ValueError:
            self.search_query()

        self.symbol = input("Enter the operator symbol for planet search (e.g., >, <, =), or just hit Enter key to bypass: ")

        if self.selection == 1:            
            return(self.search_name())
    
        elif self.selection == 2:            
            return(self.search_size())
        
        elif self.selection == 3:    
            return(self.search_atm())
        
        elif self.selection == 4:           
            return(self.search_hyd())
        
        elif self.selection == 5:
            return(self.search_pop())
        
        elif self.selection == 6:
            return(self.search_gov())
        
        elif self.selection == 7:           
            return(self.search_law())
        
        elif self.selection == 8:    
            return(self.search_tech())
        
        elif self.selection == 9:
            return(self.get_all())
        
        elif self.selection == 10:
            self.generate_star()
            #self.search_query()
        
        else:
            self.search_query()


    def search_by_category(self):
        search_functions = [
            self.search_name, self.search_size, self.search_atm,
            self.search_hyd, self.search_pop, self.search_gov,
            self.search_law, self.search_tech
        ]
        search_functions[self.selection - 1]()

    def display_result(self, result):
        t = PrettyTable(['Planet Name', 'Star Port', 'Naval Base', 'Gas Giant', 'Planetoid', 'Scout Base', 'Planet Size', 'Atmosphere', 'Hydrographics', 'Population', 'Government', 'Law Level', 'Technical Level'])
        for i in result:
            t.add_row([{i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}, {i[6]}, {i[7]}, {i[8]}, {i[9]}, {i[10]}, {i[11]}, {i[12]}, {i[13]}])
        print(t)

    def execute_query(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.display_result(result)
        self.search_query()

    def search_name(self):
        name = input("Enter the name of the planet to search for: ")
        query = f"SELECT * FROM starsystem WHERE planetName {self.symbol} '{name}'"
        self.execute_query(query)

    def search_size(self):
        size = 0
        try:
            size = int(input("Enter the planet size(1-6) to search for: "))
        except ValueError:
            self.search_size()
        query = f"SELECT * FROM starsystem WHERE size {self.symbol} {size}"
        self.execute_query(query)

    def search_atm(self):
        atm = 0
        try:
            atm = int(input("Enter the planet atmosphere(1-6) to search for: "))
        except ValueError:
            self.search_atm()
        query = f"SELECT * FROM starsystem WHERE atm {self.symbol} {atm}"
        self.execute_query(query)

    def search_hyd(self):
        hyd = 0
        try:
            hyd = int(input("Enter the planet hydrogeneics(1-6) to search for: "))
        except ValueError:
            self.search_hyd()
        query = f"SELECT * FROM starsystem WHERE hyd {self.symbol} {hyd}"
        self.execute_query(query)

    def search_pop(self):
        pop = 0
        try:
            pop = int(input("Enter the planet population(1-6) to search for: "))
        except ValueError:
            self.search_pop()
        query = f"SELECT * FROM starsystem WHERE population {self.symbol} {pop}"
        self.execute_query(query)

    def search_gov(self):
        govt = 0
        try:
            govt = int(input("Enter the planet government(1-6) to search for: "))
        except ValueError:
            self.search_gov()
        query = f"SELECT * FROM starsystem WHERE govt {self.symbol} {govt}"
        self.execute_query(query)

    def search_law(self):
        law = 0
        try:
            law = int(input("Enter the planet law level(1-6) to search for: "))
        except ValueError:
            self.search_law()
        query = f"SELECT * FROM starsystem WHERE lawlvl {self.symbol} {law}"
        self.execute_query(query)

    def search_tech(self):
        tech = 0
        try:
            tech = int(input("Enter the planet tech level(1-6) to search for: "))
        except ValueError:
            self.search_tech()
        query = f"SELECT * FROM starsystem WHERE techlvl {self.symbol} {tech}"
        self.execute_query(query)

    def get_all(self):
        query = f"SELECT * FROM starsystem"
        self.execute_query(query)

    def generate_star(self):
        star = Star()
        star.planet_upp()


if __name__ == "__main__":
    UniverseGeneration()

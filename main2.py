import sqlite3
import random
import names
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


    def genName(self):
       
        self.Planetname = names.get_full_name()
        return self.Planetname
    
    def genPlanetSize(self): 
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize




    def generate_planet_size(self):
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize


    def PlanetUPP(self):
        
        '''
        self.genAtm()
        self.genHyd()
        self.genPopulation()
        self.genGovt()
        self.Lawlvl()
        self.dtTechlvl()
        '''
        query = f"""
    INSERT INTO starsystem (
        planetname, starport, navelbase, gasgiant, planetoid, scoutbase,
        size, atm, hyd, population, govt, lawlvl, techlvl
    ) VALUES (
        '{self.genName()}', '{self.starport_type()}',
        '{self.is_naval_base()}', '{self.is_gas_giant()}',
        '{self.is_planetoids()}', '{self.is_scout_base()}',
        '{self.genPlanetSize()}', '{self.generate_atmosphere()}',
        '{self.generate_hydrosphere()}',
        '{self.generate_population()}', '{self.generate_government()}',
        '{self.generate_law_level()}', '{self.calculate_tech_lvl()}'
    );
"""
        self.cursor.execute(query)
        self.connection.commit()




    def dice(self,num=1):  
        randList = []  
        for i in range(num):
            die = random.randint(1,6)
            randList.append(die)
        return randList
    
    def isTravel(self):
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

    def dice(self, n):
        return [random.randint(1, 6) for _ in range(n)]


class CreateUniverse:
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.connect_to_database()
        self.search_query()

    def connect_to_database(self):
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def search_query(self):
        options = {
            1: self.search_name,
            2: self.search_size,
            3: self.search_atm,
            4: self.search_hyd,
            5: self.search_pop,
            6: self.search_gov,
            7: self.search_law,
            8: self.search_tech,
            9: self.get_all,
            10: self.create_star
        }

        print("The options to search for are: planetName (1), size (2), atm (3), hyd (4), population (5), govt (6), lawlvl (7), techlvl (8), getall (9), run Create Star (10)")

        while True:
            try:
                selection = int(input("Enter what you want to search for: "))
                symbol = input("Enter the symbol you want to search with, ex: >, <, = : ")
                options[selection](symbol)
            except ValueError:
                print("Invalid input. Please enter a number.")
            except KeyError:
                print("Invalid option. Please select a valid option.")

    def search_tech(self, symbol):
        tech_select = int(input(f"Enter the tech level that you want to find return {symbol} results for: "))
        query = f"SELECT * FROM starsystem WHERE techlvl {symbol} = ?"
        self.cursor.execute(query, (tech_select,))
        self.display_results()

    def search_name(self, symbol):
        name = input("Enter the planet name you want to search for: ")
        query = f"SELECT * FROM starsystem WHERE planetName {symbol} ?"
        self.cursor.execute(query, (name,))
        self.display_results()

    def get_all(self, symbol):
        query = "SELECT * FROM starsystem"
        self.cursor.execute(query)
        self.display_results()

    def search_size(self, symbol):
        try:
            planet_size = int(input("Enter the planet size you want to search for: "))
            query = f"SELECT * FROM starsystem WHERE size {symbol} ?"
            self.cursor.execute(query, (planet_size,))
            self.display_results()
        except ValueError:
            print("Invalid input. Please enter a number.")


    def search_atm(self, symbol):
        return


    def display_results(self):
        result = self.cursor.fetchall()
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Planetoid: {i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogenics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)

if __name__ == "__main__":
    CreateUniverse()

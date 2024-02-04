#Python3

import sqlite3
import random
import json
import names




class star():
    def __init__(self) -> None:
        #Func
        #self.genName()1
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        create table if not exists starsystem (
            id integer primary key autoincrement,
            planetName tinytext,
            starport int,
            navelbase boolean,
            gasgiant tinytext,
            planetoid int,
            scoutbase tinytext,
            size int,
            atm int,
            hyd int,
            population int,
            govt int,
            lawlvl int,
            techlvl int);
        """
        self.cursor.execute(query)
        self.PlanetUPP()
        query = "select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        print("Num, Name, Starport LVL, Is Navel Base?, Is gas giant?, is stciut base?, Size, Atm,Hyd,Population,govt,lawlvl,techlvl\n")
       # for i in result:
        #    print(i)
        self.look_pretty()

    def look_pretty(self):
        query = "select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:
            '''
            planetName tinytext,
            starport int,
            navelbase boolean,
            gasgiant tinytext,
            planetoid int,
            scoutbase tinytext,
            size int,
            atm int,
            hyd int,
            population int,
            govt int,
            lawlvl int,
            techlvl int
            '''
            
            for i in result:
                   
                txt = f"            Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
                new_str = txt.center(500)
                print(new_str)
    
    
    def starportType(self):
        roll = sum(self.dice(2))
        if roll == 2 or roll == 3 or roll == 4:
            self.starport = 10
        elif roll == 5 or roll == 6:
            self.starport = 11
        elif roll == 7 or roll == 8:
            self.starport = 12
        elif roll == 9:
            self.starport = 13
        elif roll == 10 or roll == 11:
            self.starport = 14
        elif roll == 12:
            self.starport = 16
        return self.starport

    def isNavelBase(self):
        roll = sum(self.dice(2))
        if roll > 7:
            self.navelbase = True
        else:
            self.navelbase = False
        return self.navelbase
    
    def isGasGiant(self):
        roll = sum(self.dice(2))
        if roll > 9:
            self.gasgiant = False
        else:
            self.gasgiant = True
        return self.gasgiant
    

    def isPlanetoids(self):
        roll = sum(self.dice(2))
        if roll > 6:
            self.planetoids = False 
        else:
            self.planetoids = True
        return self.planetoids
        
    def isScoutBase(self):
        roll = sum(self.dice(2))
        if roll > 6:
             self.scout = True
        else:
            self.scout = False
        return self.scout

    def genName(self):
        #print(names.get_full_name())
        self.Planetname = names.get_full_name()
        return self.Planetname
    
    def genPlanetSize(self): #this is funny
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
        query = f"insert into starsystem (planetname,starport,navelbase,gasgiant,planetoid,scoutbase,size,atm,hyd,population,govt,lawlvl,techlvl) values ('{self.genName()}','{self.starportType()}','{self.isNavelBase()}','{self.isGasGiant()}','{self.isPlanetoids()}','{self.isScoutBase()}','{self.genPlanetSize()}','{self.genAtm()}','{self.genHyd()}','{self.genPopulation()}','{self.genGovt()}','{self.Lawlvl()}','{self.dtTechlvl()}');"
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
        
        
    
    def genAtm(self):
        if self.planetsize != 0:
            self.atm = (sum((self.dice(2))) - 7) + self.planetsize
        
        return self.atm
    
    
    def genHyd(self):
        self.hyd = (sum((self.dice(2))) - 7) + self.planetsize
        if self.planetsize <= 1:
            self.hyd = 0
        if self.hyd < 0:
            self.hyd = 0
        if self.hyd > 10:
            self.hyd = 10
        return self.hyd
        
    def genPopulation(self):
        self.population = (sum(self.dice(2)) - 2)
        return self.population

        
    def genGovt(self):
        self.govt = (sum(self.dice(2)) - 7) + self.population
        return self.govt

    def Lawlvl(self):
        self.law = (sum(self.dice(2)) - 7) + self.govt
        return self.law
        
    def dtTechlvl(self):
        self.techlvl = sum(self.dice(1))
        if self.starport == 10:
            self.techlvl += 6
        if self.starport == 11:
            self.techlvl += 4
        if self.starport == 12:
            self.techlvl += 2
        if self.starport == 16:
            self.techlvl -= 4
        if self.planetsize == 0 or self.planetsize == 1:
            self.techlvl += 2
        if self.planetsize == 2 or self.planetsize == 3 or self.planetsize == 4:
            self.techlvl += 1
        if self.atm < 4:
            self.techlvl += 1
        if self.atm > 9 and self.atm < 15:
            self.techlvl += 1
        if self.hyd == 9:
            self.techlvl += 1
        if self.hyd == 10:
            self.techlvl += 2
        if self.population > 0 and self.population < 6:
            self.techlvl +=1
        if self.population == 9:
            self.techlvl += 2
        if self.population == 10:
            self.techlvl += 4
        if self.govt == 0:
            self.techlvl +=1
        if self.govt == 5:
            self.techlvl +=1
        if self.govt == 13:
            self.techlvl -=2
        return self.techlvl
        
        


#class universe():


class CreateUniverse:
    COLOR_BOLD_YELLOW = "\033[38;5;221m"
    COLOR_RESET = "\033[0m"

    def __init__(self) -> None:
        self.connection = self.connect_to_database()
        self.cursor = self.connection.cursor()
        self.search_query()

    def connect_to_database(self):
        file = 'stardatabase.db'
        return sqlite3.connect(file)

    def search_query(self):
        print("""
            The options to search for are: 
            {}(1){} planet Name 
            {}(2){} size
            {}(3){} atmosphere 
            {}(4){} hyd 
            {}(5){} population 
            {}(6){} government 
            {}(7){} law level 
            {}(8){} tech level  
            {}(9){} Fetch all  
            {}(10){} Generate Star
              """.format(
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET,
            self.COLOR_BOLD_YELLOW, self.COLOR_RESET
        ))

        try:
            self.selection = int(input("Enter your search query: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_query()

        self.symbol = str(input("Enter the symbol you wish to use for the search (e.g., >, <, =) "))

        if 1 <= self.selection <= 10:
            getattr(self, f'search_{self.selection}')()
        else:
            print("Invalid selection. Please enter a valid number.")
            self.search_query()

    def print_results(self, result):
        for i in result:
            txt = f"Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Planetoid: {i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogenics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)

    def search_tech(self):
        try:
            self.tech_select = int(input(f"Enter the desired tech level to fetch {self.symbol} results for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_tech()

        query = f"select * from starsystem where tech_level {self.symbol}={self.tech_select}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_name(self):
        name = input("Enter the name of the planet you wish to search for: ")
        name = "'" + name + "'"
        query = f"select * from starsystem where planet_name {self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def get_all(self):
        query = f"select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_size(self):
        try:
            size = int(input("Enter the planet size you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_size()

        query = f"select * from starsystem where size {self.symbol}={size}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_atm(self):
        try:
            atmosphere = int(input("Enter the planet atmosphere you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_atm()

        query = f"select * from starsystem where atmosphere {self.symbol}={atmosphere}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_hyd(self):
        try:
            hyd = int(input("Enter the planet hydrogeneics you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_hyd()

        query = f"select * from starsystem where hydrogeneics {self.symbol}={hyd}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_pop(self):
        try:
            population = int(input("Enter the planet population you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_pop()

        query = f"select * from starsystem where population {self.symbol}={population}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_gov(self):
        try:
            govt = int(input("Enter the planet govt you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_gov()

        query = f"select * from starsystem where govt {self.symbol}={govt}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

    def search_law(self):
        try:
            law_level = int(input("Enter the planet law level you want to search for: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            self.search_law()

        query = f"select * from starsystem where law_level {self.symbol}={law_level}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.print_results(result)
        self.search_query()

if __name__ == "__main__":
    CreateUniverse()
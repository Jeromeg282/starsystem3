import sqlite3
import random
import json
import names




class star():
    def __init__(self) -> None:
        #Func
        #self.genName()
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
            #print(f"Planet Name: {i[1]}, Starport:  {i[2]}, Navel Base:  {i[3]}, Gasgiant:  {i[4]}, Planetoid:  {i[5]}, Scout Base:  {i[6]}, Planet Size:  {i[7]}\nAtmosphere:  {i[8]}, Hydogenics:  {i[8]}, Population:  {i[10]}, Government level:  {i[11]}, Law Level:  {i[12]}, Tech Level:  {i[13]}\n")
            for i in result:
                    #print(f"\n          Planet Name: {i[1]}\n--------------------------------------\n  Starport:  {i[2]}         Navel Base: {i[3]}\n  Gasgiant: {i[4]}           Planetoid: {i[5]}\n  Scout Base: {i[6]}        Planet Size: {i[7]}\n  Atmosphere: {i[8]}         Hydrogeneics: {i[9]}\n  Population: {i[10]}         Government : {i[11]}\n  Law level: {i[12]}           Tech level: {i[13]}\n")
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
        #I'm a goofy goober
        #I agree with the comment above
        #I challenge you to a debate

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


class createUniverse():
    def __init__(self) -> None:
        #star()
        file = 'stardatabase.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        self.searchQuery()
    def searchQuery(self):
        print("The options to search for are: planetName (1), size (2), atm (3), hyd (4), population (5), govt (6), lawlvl (7), techlvl (8), getall (9), run Create Star (10)")
        try:
            self.selection = int(input("Enter what you want to seach for: "))
        except:
            self.searchQuery()
        self.symbol = str(input("Enter the symbol you want to search with, ex: >, <, = : "))
        if self.selection == 1:
            
            self.searchName()
        elif self.selection == 2:
            
            self.searchSize()
        elif self.selection == 3:
            
            self.searchAtm()
        elif self.selection == 4:
            
            self.searchHyd()
        elif self.selection == 5:
            
            self.searchPop()
        elif self.selection == 6:
            
            self.searchGov()
        elif self.selection == 7:
            
            self.searchLaw()
        elif self.selection == 8:
            
            self.searchTech()
        elif self.selection == 9:
            self.getall()
        else:
            self.searchQuery()
    def searchTech(self):
        self.techselect = int(input(f"Enter the tech level that you want to find return {self.symbol} results for: "))
        query = f"select * from starsystem where techlvl {self.symbol}={self.techselect}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchName(self):
        name = input("Enter the planet name you want to search for: ")
        name = "'" + name + "'"
        query = f"select * from starsystem where planetName{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        
        self.searchQuery()
    def getall(self):
        query = f"select * from starsystem"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    
    def searchSize(self):
        name = 0
        try:
            name = int(input("Enter the planet size you want to search for: "))
        except:
            self.searchSize()
        query = f"select * from starsystem where size{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchAtm(self):
        name = 0
        try:
            name = int(input("Enter the planet atmosphere you want to search for: "))
        except:
            self.searchAtm()
        query = f"select * from starsystem where atm{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchHyd(self):
        name = 0
        try:
            name = int(input("Enter the planet hydrogeneics you want to search for: "))
        except:
            self.searchHyd()
        query = f"select * from starsystem where hyd{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchPop(self):
        name = 0
        try:
            name = int(input("Enter the planet population you want to search for: "))
        except:
            self.searchPop()
        query = f"select * from starsystem where population{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchGov(self):
        name = 0
        try:
            name = int(input("Enter the planet govt you want to search for: "))
        except:
            self.searchGov()
        query = f"select * from starsystem where govt{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()
    def searchLaw(self):
        name = 0
        try:
            name = int(input("Enter the planet law level you want to search for: "))
        except:
            self.searchLaw()
        query = f"select * from starsystem where lawlvl{self.symbol}={name}"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for i in result:         
            txt = f"                                                                                  Planet Name: {i[1]}\n------------------------------\nStarPort: {i[2]}       Naval Base: {i[3]}\nGasGiant: {i[4]}     Plantetoid:{i[5]}\nScout Base: {i[6]}  Planet Size: {i[7]}\nAtmosphere: {i[8]}      Hydrogeneics: {i[9]}\nPopulation: {i[10]}      Government: {i[11]}\nLaw level: {i[12]}       Tech Level: {i[13]}\n"
            new_str = txt.center(500)
            print(new_str)
        self.searchQuery()

if __name__ == "__main__":
    createUniverse()
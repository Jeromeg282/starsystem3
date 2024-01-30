#Python3

import sqlite3
import random
import json
import names





class Star():
    def __init__(self) -> None:
        file = 'database.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS starsystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planetName TINYTEXT,
            starport INT,
            navelbase BOOLEAN,
            gasgiant TINYTEXT,
            planetoid INT,
            scoutbase TINYTEXT,
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
    

    def starportType(self):
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



    def isNavelBase(self):
        roll = sum(self.dice(2))
        self.navelbase = roll > 7
        return self.navelbase
        

    def isGasGiant(self):
        roll = sum(self.dice(2))
        self.Gasgiant = roll > 9
        return self.Gasgiant
    
    
    def isPlanetoids(self):
        roll = sum(self.dice(2))
        self.planetoids = roll > 6
        return self.planetoids
        
    def isScoutBase(self):
        roll = sum(self.dice(2))
        self.scoutbase = roll > 6
        return self.scoutbase


    def generatePlanetsize(self):
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize


    def generateName(self):
        self.Planetname = names.get_full_name()
        return self.Planetname

 
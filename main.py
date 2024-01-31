#Python3

import sqlite3
import random
import json






import sqlite3
import random

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

    def generate_planet_size(self):
        self.planetsize = sum(self.dice(2)) - 2
        return self.planetsize

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




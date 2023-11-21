import random
import sqlite3
import os
import json

class StarSystemGenerator:
    def __init__(self, system_name):
        self.system_name = system_name
        self.mainworld = {}

    def load_definitions(self, filename):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)
        #with open(file_path, 'r') as file:
        with open(filename, 'r') as file:
            definitions = json.load(file)
        return definitions

    def generate_mainworld(self):
        #UPP
        definitions_starport = self.load_definitions('starport_definitions.json')
        definitions_size = self.load_definitions('size_definitions.json')
        definitions_atmosphere = self.load_definitions('atmosphere_definitions.json')
        definitions_hydros = self.load_definitions('hydros_definitions.json')
        definitions_populus = self.load_definitions('populus_definitions.json')
        definitions_gov = self.load_definitions('gov_definitions.json')
        definitions_lawlevel = self.load_definitions('lawlevel_definitions.json')
        definitions_techlevel = self.load_definitions('techlevel_definitions.json')

        self.mainworld["starport"] = self.get_definition(
            random.choice(definitions_starport["values"]), definitions_starport["descriptions"])
        self.mainworld["size"] = self.get_definition(
            random.choice(definitions_size["values"]), definitions_size["descriptions"])
        self.mainworld["atmosphere"] = self.get_definition(
            random.choice(definitions_atmosphere["values"]), definitions_atmosphere["descriptions"])
        self.mainworld["hydrographics"] = self.get_definition(
            random.choice(definitions_hydros["values"]), definitions_hydros["descriptions"])
        self.mainworld["population"] = self.get_definition(
            random.choice(definitions_populus["values"]), definitions_populus["descriptions"])
        self.mainworld["government"] = self.get_definition(
            random.choice(definitions_gov["values"]), definitions_gov["descriptions"])
        self.mainworld["law_level"] = self.get_definition(
            random.choice(definitions_lawlevel["values"]), definitions_lawlevel["descriptions"])
        self.mainworld["tech_level"] = self.get_definition(
            random.choice(definitions_techlevel["values"]), definitions_techlevel["descriptions"])

    def save_to_database(self, db_filename='star_systems.db'):
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS star_systems (
                id INTEGER PRIMARY KEY,
                system_name TEXT,
                starport TEXT,
                size TEXT,
                atmosphere TEXT,
                hydrographics TEXT,
                population TEXT,
                government TEXT,
                law_level TEXT,
                tech_level TEXT
            )
        ''')

    
        cursor.execute('''
            INSERT INTO star_systems 
            (system_name, starport, size, atmosphere, hydrographics, population, government, law_level, tech_level) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.system_name,
            self.mainworld["starport"],
            self.mainworld["size"],
            self.mainworld["atmosphere"],
            self.mainworld["hydrographics"],
            self.mainworld["population"],
            self.mainworld["government"],
            self.mainworld["law_level"],
            self.mainworld["tech_level"]
        ))

        
        conn.commit()
        conn.close()

    def load_from_database(self, db_filename='star_systems.db'):
        conn = sqlite3.connect(db_filename)
        cursor = conn.cursor()

        
        cursor.execute('SELECT * FROM star_systems WHERE system_name = ?', (self.system_name,))
        row = cursor.fetchone()

    
        if row:
            print("Star System:", row[1])
            print("Starport:", row[2])
            print("Size:", row[3])
            print("Atmosphere:", row[4])
            print("Hydrographics:", row[5])
            print("Population:", row[6])
            print("Government:", row[7])
            print("Law Level:", row[8])
            print("Tech Level:", row[9])
        else:
            print(f"No data found for the star system {self.system_name}")

        
        conn.close()

    def get_definition(self, value, definitions):
        return definitions.get(str(value), "Undefined")


if __name__ == "__main__":
    system_name = "SampleSystem"
    star_system_generator = StarSystemGenerator(system_name)
    star_system_generator.generate_mainworld()
    star_system_generator.save_to_database()
    star_system_generator.load_from_database()

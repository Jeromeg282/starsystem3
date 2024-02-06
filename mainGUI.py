import sqlite3
import random
import names
import prettytable
from prettytable import PrettyTable
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QComboBox, QInputDialog


class Star:
    def __init__(self):
        file = 'database.db'
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()
        query = """
        CREATE TABLE IF NOT EXISTS starsystem (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            planetname TEXT,
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
        self.cursor.connection.commit
        
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


class UniverseGeneration(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

        self.file = 'database.db'
        self.connection = sqlite3.connect(self.file)
        self.cursor = self.connection.cursor()
        
        self.columns =['id', 'planetname', 'starport', 'navalbase', 'gasgiant', 'planetoid',
            'scoutbase','size','atm','hyd','population','govt','lawlvl','techlvl'
        ]


    def init_ui(self):

        self.label1 = QLabel('Enter search criteria with parameters:')
        self.label2 = QLabel('Search results:')

        # Create a QComboBox for menu option
        self.option = QComboBox(self)
        self.option.addItem('Search By Planet Name')
        self.option.addItem('Search By Planet Size')
        self.option.addItem('Search By Planet Atmosphere')
        self.option.addItem('Search By Planet Hydrographics')
        self.option.addItem('Search By Planet Population')
        self.option.addItem('Search By Planet Government')
        self.option.addItem('Search By Planet Law Level')
        self.option.addItem('Search By Planet Technical Level')
        self.option.addItem('Print All Planet Info')
        self.option.addItem('Generate Star System')
        self.option.currentIndexChanged.connect(self.onOptionChange)

        # Create a QComboBox for search opeator
        self.operator = QComboBox(self)
        self.operator.addItem('<')
        self.operator.addItem('=')
        self.operator.addItem('>')
        self.operator.currentIndexChanged.connect(self.onOperatorChange)

        # Create a QLineEdit for search value
        self.input = QLineEdit()
        self.input.textChanged.connect(self.onInputChange)

        # Create a QPushButton for the submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.onSubmit)

        # Create a QPushButton for the reset button
        self.reset_button = QPushButton('Reset', self)
        self.reset_button.clicked.connect(self.onReset)

        # Create a QLabel to display the result
        self.result_label = QLabel(self)

        # Create a table widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setMinimumSize(800, 700)
        self.table_widget.cellClicked.connect(self.onCellClicked)
        # Create a QVBoxLayout
        vbox = QVBoxLayout()
        vbox.addWidget(self.label1)
        vbox.addWidget(self.option)
        vbox.addWidget(self.operator)
        vbox.addWidget(self.input)
        vbox.addWidget(self.submit_button)
        vbox.addWidget(self.reset_button)
        vbox.addWidget(self.result_label)
        vbox.addWidget(self.label2)
        vbox.addWidget(self.table_widget)
        vbox.addStretch(2)

        # Set the layout for the QWidget
        self.setLayout(vbox)

        # Set the window properties
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Star Systems Application')
        self.show()

    def onOptionChange(self):
        self.selected_index = self.option.currentIndex()+1
        #self.label.setText(f'Menu option: {self.selected_index}')
        
    def onOperatorChange(self):
        self.selected_option = self.operator.currentText()
        #self.label.setText(f'Menu option: {self.selected_option} ')

    def onInputChange(self):
        self.selected_option = self.input.text()
        #self.label.setText(f'Menu option: {self.selected_option} ')         

    def onReset(self):
        self.input.setText("")
        self.option.setCurrentIndex(0)
        self.operator.setCurrentIndex(0)    
        self.result_label.setText("")
        self.cursor.connection.commit


    def onSubmit(self):
        self.input_text = self.input.text()
        result = f"Entered search criteria : {self.option.currentText()} {self.operator.currentText()} {self.input_text} \n"    
        self.result_label.setText(result)

        if (self.option.currentIndex() == 0):        
            query = f"SELECT * FROM starsystem WHERE planetName {self.operator.currentText()}'{self.input_text}'"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 1): 
            query = f"SELECT * FROM starsystem WHERE size {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 2): 
            query = f"SELECT * FROM starsystem WHERE atm {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 3): 
            query = f"SELECT * FROM starsystem WHERE hyd {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 4): 
            query = f"SELECT * FROM starsystem WHERE population {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 5): 
            query = f"SELECT * FROM starsystem WHERE govt {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)
 
        elif (self.option.currentIndex() == 6): 
            query = f"SELECT * FROM starsystem WHERE lawlvl {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)
            
        elif (self.option.currentIndex() == 7): 
            query = f"SELECT * FROM starsystem WHERE techlvl {self.operator.currentText()} {self.input_text}"
            self.execute_query_gui(query)
  
        elif (self.option.currentIndex() == 8): 
            query = f"SELECT * FROM starsystem"
            self.execute_query_gui(query)

        elif (self.option.currentIndex() == 9): 
            star = Star()
            star.planet_upp()

    def onCellClicked(self, row, column):
        item = self.table_widget.item(row,  column)
        new_value, ok = QInputDialog.getText(self, "Update Cell Value", "Enter new value here:")
        if ok:
            item.setText(new_value)
            query = f"UPDATE starsystem SET {self.columns[column]} = {new_value} WHERE id = {row+1}"
            self.cursor.execute(query)
            self.connection.commit
            self.get_all_gui

    def search_query(self):
        print("""
            \n\n***************************  Welcome to the Star Systems Console  *****************************  
            \nThe menu options are: \n
            \033[38;5;221mOption[1]\033[0m <---Search By Planet Name---> 
            \033[38;5;221mOption[2]\033[0m <---Search By Planet Size--->
            \033[38;5;221mOption[3]\033[0m <---Search By Planet Atmosphere---> 
            \033[38;5;221mOption[4]\033[0m <---Se   arch By Planet Hydrographics---> 
            \033[38;5;221mOption[5]\033[0m <---Search By Planet Population---> 
            \033[38;5;221mOption[6]\033[0m <---Search By Planet Government---> 
            \033[38;5;221mOption[7]\033[0m <---Search By Planet Law Level---> 
            \033[38;5;221mOption[8]\033[0m <---Search By Planet Technical Level--->  
            \033[38;5;221mOption[9]\033[0m <---Print All Planet Info--->  
            \033[38;5;221mOption[10]\033[0m <---Generate Star System--->              
            \n*************************************************************************************************              
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


    def execute_query_gui(self, query):
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.build_table(results) 

    def build_table(self, data):
        # Clear existing rows and columns in the table
        self.table_widget.setRowCount(0)
        self.table_widget.setColumnCount(0)

        if not data:
            return

        # Set the column count based on the number of columns in the query result
        column_count = len(data[0])
        self.table_widget.setColumnCount(column_count)

        # Set the column headers
        for col, header in enumerate(self.cursor.description):
            self.table_widget.setHorizontalHeaderItem(col, QTableWidgetItem(header[0]))

        # Populate the table with data
        for row, row_data in enumerate(data):
            self.table_widget.insertRow(row)
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.table_widget.setItem(row, col, item)

        #resize        
        self.table_widget.resizeColumnsToContents()        
        

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

    def get_all_gui(self):
        query = f"SELECT * FROM starsystem"
        self.execute_query_gui(query)    

    def generate_star(self):
        star = Star()
        star.planet_upp()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UniverseGeneration()
    sys.exit(app.exec_())


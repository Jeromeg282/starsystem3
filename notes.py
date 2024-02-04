#query = f"insert into starsystem (planetname,starport,navelbase,gasgiant,planetoid,scoutbase,size,atm,hyd,population,govt,lawlvl,techlvl)
        #values ('{self.genName()}','{self.starport_type()}','{self.is_naval_base()}','{self.is_gas_giant()}','{self.is_planetoids()}','{self.is_scout_base()}','{self.genPlanetSize()}','{self.generate_atmosphere()}','{self.generate_hydrosphere()}','{self.generate_population()}','{self.generate_government()}','{self.generate_law_level()}','{self.calculate_tech_lvl()}');"
        #self.cursor.execute(query)
        #self.connection.commit()
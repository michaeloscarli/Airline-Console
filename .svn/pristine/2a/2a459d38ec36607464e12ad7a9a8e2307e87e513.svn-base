'''
Created on Feb 25, 2014

@author: Oscar
'''
import ast
import json
class Metro(object):
    '''
    A Metro object representing a node of the graph
    '''
    code = ""
    name = ""
    country = ""
    continent = ""
    timezone = 0
    coordinates = {}
    population = 0
    region = 0
    routes = {}    #Where Key is the destination metro's name
    djikstras_visit = False
    djikstras_distance = float('+inf')
    prev = None
    
    def __init__(self, code, name, country, continent, timezone, coordinates, population, region, routes):
        '''
        Constructor for the Metro
        '''
        self.code = code
        self.name = name
        self.country = country
        self.continent = continent
        self.timezone = timezone
        self.coordinates = coordinates
        self.population = population 
        self.region = region
        self.routes = routes
        
    def printInformation(self):
        '''
        Prints all the information about the Metro
        '''
        destinations = ""
        print "Code: " + self.code
        print "Name: " + self.name
        print "Country: " + self.country
        print "Continent: " + self.continent
        print "Timezone:", self.timezone
        print "Coordinates:",
        for key in self.coordinates:
            print key + ":", self.coordinates[key],
        print
        print "Population:", self.population
        print "Region:", self.region
        print "Destinations:",
        destinations = [(self.routes[key].destination.name + " at " + str(self.routes[key].distance) + " kilometers") for key in self.routes]
        print ", ".join(destinations)
        
    def setCode(self, code):
        if type(code) is not str:
            print "Please enter a valid code."
        else:
            self.code = code
        
    def setName(self, name):
        if type(name) is not str:
            print "Please enter a valid name."
        else:
            self.name = name
        
    def setCountry(self, country):
        if type(country) is not str:
            print "Please enter a valid country."
        else:
            self.country = country
        
    def setContinent(self, continent):
        if (continent != "North America" and continent != "South America" and continent != "Antarctica" and 
            continent != "Europe" and continent != "Asia" and continent != "Australia" and continent!="Africa"):
            print "Please enter a valid continent (North America, South America, Antarctica, Europe, Asia, or Australia, or Africa)."
        else:
            self.continent = continent
        
    def setTimezone(self, timezone):
        if type(timezone) is not int:
            print "Please enter a valid timezone value."
        else:
            self.timezone = timezone
        
    def setCoordinates(self):
        coordOneDir = raw_input("What is the first heading of the coordinate? ")
        coordOneVal = raw_input("What is the degree of the first heading? ")
        coordTwoDir = raw_input("What is the second heading of the coordinate? ")
        coordTwoVal = raw_input("What is the degree of the second heading? ")
        self.coordinates = {coordOneDir: coordOneVal, coordTwoDir: coordTwoVal}
            
    def setPopulation(self, population):
        if population<0 or type(population) is not int:
            print "Please enter a valid population value."
        else:
            self.population = population
        
    def setRegion(self, region):
        if region<0 or type(region) is not int:
            print "Please enter a valid region value."
        else: 
            self.region = region
    
        
        
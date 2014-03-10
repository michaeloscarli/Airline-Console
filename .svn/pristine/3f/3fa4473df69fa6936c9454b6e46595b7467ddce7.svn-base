'''
Created on Feb 27, 2014

@author: Oscar
'''
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Node import Metro

class TestNode(unittest.TestCase):

    def setUp(self):
        '''
        Sets up a simple Metro object to run tests on
        '''
        self.metro = Metro("NYC", "New York City", "United States", 
                      "North America", 69, {"W": 69, "N": 69}, 
                      6969696969, 455, {"testRoute": None})
        
    def testConstructor(self):
        '''
        Tests the constructor for the Metro class. Ensures that things
        are being initialized properly.
        '''
        self.assertEqual("NYC", self.metro.code)
        self.assertEqual("New York City", self.metro.name)
        self.assertEqual("United States", self.metro.country)
        self.assertEqual("North America", self.metro.continent)
        self.assertEqual(69, self.metro.timezone)
        self.assertEqual(69, self.metro.coordinates["W"])
        self.assertEqual(69, self.metro.coordinates["N"])
        self.assertEqual(6969696969, self.metro.population)
        self.assertEqual(455, self.metro.region)
        self.assertEqual(None, self.metro.routes["testRoute"])
    
    
    def testPrintInformation(self):
        '''
        Tests to make sure that a Metro has the right values in its variables
        before print statements are called on its variables to display its information
        '''
        self.assertEqual("NYC", self.metro.code)
        self.assertEqual("New York City", self.metro.name)
        self.assertEqual("United States", self.metro.country)
        self.assertEqual("North America", self.metro.continent)
        self.assertEqual(69, self.metro.timezone)
        self.assertEqual(69, self.metro.coordinates["W"])
        self.assertEqual(69, self.metro.coordinates["N"])
        self.assertEqual(6969696969, self.metro.population)
        self.assertEqual(455, self.metro.region)
        self.assertEqual(None, self.metro.routes["testRoute"])
    
    def test_set_code(self):
        self.metro.setCode("JJJ")
        self.assertEqual("JJJ", self.metro.code)
        
    def test_set_name(self):
        self.metro.setName("Chicago")
        self.assertEqual("Chicago", self.metro.name)
    
    def test_set_country(self):
        self.metro.setCountry("China")
        self.assertEqual("China", self.metro.country)
        
    def test_set_continent(self):
        self.metro.setContinent("Australia")
        self.assertEqual("Australia", self.metro.continent)
    
    def test_set_timezone(self):
        self.metro.setTimezone(5)
        self.assertEqual(5, self.metro.timezone)
        
    def test_set_coordinates(self):
        self.metro.coordinates = {"N": 35, "S": 15}
        self.assertEqual(True, self.metro.coordinates.has_key("N"))
        self.assertEqual(True, self.metro.coordinates.has_key("S"))
        self.assertEqual(35, self.metro.coordinates["N"])
        self.assertEqual(15, self.metro.coordinates["S"])
        
    def test_set_population(self):
        self.metro.setPopulation(1422322)
        self.assertEqual(1422322, self.metro.population)
        
    def test_set_region(self):
        self.metro.setRegion(123)
        self.assertEqual(123, self.metro.region)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
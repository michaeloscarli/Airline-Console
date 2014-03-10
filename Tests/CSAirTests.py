'''
Created on Feb 27, 2014

@author: Oscar
'''
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
import json
from Node import Metro
from Edge import Route
import numpy as np

class TestCSAir(unittest.TestCase):
    

    def setUp(self):
        self.listOfMetros = {}   #Where Key is the country's code
        self.listOfRoutes = []   #A list of the routes
        self.userQuery = ""      #The buffer that holds the user input
        self.data = json.loads(open('../map_data.json').read()) #The data that is read from the .json file

        self.cityData = self.data["metros"]   #A list of the metro data
        self.routeData = self.data["routes"]  #A list of the route data
        for x in range (0,len(self.cityData)):
            self.listOfMetros[self.cityData[x]['code']] = Metro(self.cityData[x]['code'], self.cityData[x]['name'], self.cityData[x]['country'], 
                                                                self.cityData[x]['continent'], self.cityData[x]['timezone'], self.cityData[x]['coordinates'], 
                                                                self.cityData[x]['population'], self.cityData[x]['region'], {})
        for x in range(0,len(self.routeData)):
            route = Route(self.listOfMetros[self.routeData[x]['ports'][0]], self.listOfMetros[self.routeData[x]['ports'][1]], self.routeData[x]['distance'])
            returnRoute = Route(self.listOfMetros[self.routeData[x]['ports'][1]], self.listOfMetros[self.routeData[x]['ports'][0]], self.routeData[x]['distance'])
            self.listOfRoutes.append(route)
        
            #Add the route to the specific city
            self.listOfMetros[self.routeData[x]['ports'][0]].routes[self.routeData[x]['ports'][1]] = route
            self.listOfMetros[self.routeData[x]['ports'][1]].routes[self.routeData[x]['ports'][0]] = returnRoute
    
    '''
    Asserts that there are 48 cities to print
    '''    
    def testPrintCities(self):
        locations = [str(city) for city in self.listOfMetros]
        self.assertEquals(48, len(locations))
        
    '''
    Asserts that the shortest route is successfully located
    '''
    def testShortestRoute(self):
        shortestRoute = self.listOfRoutes[0]
        for route in self.listOfRoutes:
            if route.distance < shortestRoute.distance:
                shortestRoute = route
        self.assertEquals("Washington", shortestRoute.origin.name)
        
    '''
    Asserts that the longest route is successfully located
    '''
    def testLongestRoute(self):
        longestRoute = self.listOfRoutes[0]
        for route in self.listOfRoutes:
            if route.distance > longestRoute.distance:
                longestRoute = route
        self.assertEquals("Sydney", longestRoute.origin.name)
     
    '''
    Asserts that the average flight distance is correctly calculated
    '''   
    def testAverageFlight(self):
        distances = []
        for route in self.listOfRoutes:
            distances.append(route.distance)
        self.assertEquals(2300.2765957446809, np.mean(distances))
    
    '''
    Asserts that the hub cities are correctly identified
    '''
    def testHubCities(self):
        maxRoutes = 0
        hubCities = []
        for key in self.listOfMetros:
            if len(self.listOfMetros[key].routes) > maxRoutes:
                maxRoutes = len(self.listOfMetros[key].routes)
        for key in self.listOfMetros:
            if len(self.listOfMetros[key].routes) == maxRoutes:
                hubCities.append(self.listOfMetros[key].name)
        self.assertEquals("Istanbul", hubCities[0])
        self.assertEquals("Hong Kong", hubCities[1])
        
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''
Created on Mar 3, 2014

@author: Oscar
'''
import copy
import json
import numpy as np
import webbrowser
from Edge import Route
from Node import Metro

class Network(object):
    '''
    The graph class that represents an airline's network
    '''
    list_of_metros = {}   #Where Key is the country's code
    list_of_routes = []   #A list of the routes
    city_data = []       #The city data directly parsed from the .json file
    route_data = []      #The route data directly parsed from the.json file

    def __init__(self, data):
        self.city_data = data["metros"]
        self.route_data = data["routes"]
        self.makeListOfMetros()
        self.makeListOfRoutes()
        self.changeKeyToName()

    def print_cities(self):
        '''
        Prints all cities serviced by CSAir by iterating through list_of_metros
        '''
        locations = [str(city) for city in self.list_of_metros]
        print ", ".join(locations)
    
    def print_city_information(self):
        '''
        Prints all the information about a city by calling each city's printInformation function    
        '''
        userQuery = raw_input("What city would you like to know about? ")
        self.list_of_metros[userQuery].printInformation()
    
    
    def print_longest_flight(self):
        '''    
        Prints the longest flight that is serviced by CSAir by using max over the route list 
        '''    
        longestRoute = self.list_of_routes[0]
        for route in self.list_of_routes:
            if route.distance > longestRoute.distance:
                longestRoute = route
            
        print "The longest flight is between", longestRoute.origin.name + " and", longestRoute.destination.name + "."
    
    
    def print_shortest_flight(self):
        '''    
        Prints the shortest flight that is serviced by CSAir by using min over the route list
        '''
        shortestRoute = self.list_of_routes[0]
        for route in self.list_of_routes:
            if route.distance < shortestRoute.distance:
                shortestRoute = route
            
        print "The shortest flight is between", shortestRoute.origin.name + " and", shortestRoute.destination.name + "."
    
    def print_average_flight_distance(self):
        '''
        Prints the average flight distance of all routes serviced by CSAir by using np.mean over the route list
        '''
        distances = []
        for route in self.list_of_routes:
            distances.append(route.distance)
        print "The average flight distance is: " + str(np.mean(distances)) + " kilometers."
    
    
    def print_city_with_largest_pop(self):
        '''
        Prints the largest city (by population) that is serviced by CSAir by iterating over the city list and comparing populations
        '''
        largestCity = self.list_of_metros.keys()[0]
        for key in self.list_of_metros:
            if self.list_of_metros[largestCity].population < self.list_of_metros[key].population:
                largestCity = self.list_of_metros[key].name
        print "The largest city by population is:", largestCity
    
    def print_city_with_smallest_pop(self):
        '''
        Prints the smallest city (by population) that is serviced by CSAir by iterating over the city list and comparing populations
        '''
        smallestCity = self.list_of_metros.keys()[0]
        for key in self.list_of_metros:
            if self.list_of_metros[smallestCity].population > self.list_of_metros[key].population:
                smallestCity = self.list_of_metros[key].name
        print "The smallest city by population is:", smallestCity
    
    def print_average_city_pop(self):
        '''    
        Prints the average population of cities serviced by CSAir by iterating over the entire city list and average populations
        '''
        populations = [self.list_of_metros[key].population for key in self.list_of_metros]
        print "The average population of serviced cities is:", np.mean(populations)
    
    def print_continents_and_cities(self):
        '''
        Prints a list of serviced continents and cities by interating 
        '''
        continents = {"North America": [], "South America": [], "Europe": [], "Asia": [], "Africa": [], "Antarctica": [], "Australia": []}
        for key in self.list_of_metros:
            continents[self.list_of_metros[key].continent].append(self.list_of_metros[key].name)
        for continent in continents:
            if len(continents[continent])!=0:
                print continent + ": " + ', '.join(continents[continent])
    
    def print_hub_cities(self):
        '''
        Prints a list of CSAir's hub cities
        '''
        maxRoutes = 0
        hubCities = []
        for key in self.list_of_metros:
            if len(self.list_of_metros[key].routes) > maxRoutes:
                maxRoutes = len(self.list_of_metros[key].routes)
        for key in self.list_of_metros:
            if len(self.list_of_metros[key].routes) == maxRoutes:
                hubCities.append(self.list_of_metros[key].name)
        print "CSAir's hub cities are: " + ', '.join(hubCities)
    
    def open_route_map(self):
        '''
        Opens a map of the routes serviced by CSAir    
        '''
        flightList = []
        for route in self.route_data:
            flightList.append(route["ports"][0] + "-" + route["ports"][1])
        urlString = "http://www.gcmap.com/mapui?P="
        urlString += ",+".join(flightList)
        webbrowser.open(urlString)
    
    def makeListOfMetros(self):
        '''
        Compiles the dictionary of metros by iterating through the city_data list parsed from the json file
        ''' 
        for x in range (0,len(self.city_data)):
            self.list_of_metros[self.city_data[x]['code']] = Metro(self.city_data[x]['code'], self.city_data[x]['name'], self.city_data[x]['country'], 
                                                      self.city_data[x]['continent'], self.city_data[x]['timezone'], self.city_data[x]['coordinates'], 
                                                      self.city_data[x]['population'], self.city_data[x]['region'], {})
         
    def makeListOfRoutes(self):
        '''
        Compiles the list of routes by iterating through the route_data list parsed from the json file
        Also adds the route to its corresponding cities
        '''   
        for x in range(0,len(self.route_data)):
            #Adds the routes to the dictionary
            route = Route(self.list_of_metros[self.route_data[x]['ports'][0]], self.list_of_metros[self.route_data[x]['ports'][1]], self.route_data[x]['distance'])
            returnRoute = Route(self.list_of_metros[self.route_data[x]['ports'][1]], self.list_of_metros[self.route_data[x]['ports'][0]], self.route_data[x]['distance'])
            self.list_of_routes.append(route)
        
            #Add the route to the specific city
            self.list_of_metros[self.route_data[x]['ports'][0]].routes[self.route_data[x]['ports'][1]] = route
            self.list_of_metros[self.route_data[x]['ports'][1]].routes[self.route_data[x]['ports'][0]] = returnRoute
        
    def changeKeyToName(self):
        '''
        changes the key of the dictionary list_of_metros from codes of cities to names
        '''  
        for key in self.list_of_metros:
            name = self.list_of_metros[key].name
            self.list_of_metros[str(name)] = self.list_of_metros.pop(key)
            
    def remove_city(self):
        '''
        removes a city from the graph
        '''
        userQuery = raw_input("Please enter the city you would like to remove. ")
        removedCity = self.list_of_metros.pop(userQuery)
        for route in removedCity.routes:
            destination_city = removedCity.routes[route].destination
            for returnRoute in destination_city.routes.keys():
                if returnRoute == removedCity.code:
                    del destination_city.routes[returnRoute]
        self.list_of_routes = [route for route in self.list_of_routes if not (route.destination.name == userQuery or route.origin.name == userQuery)]
        print self.list_of_routes            
                    
    def remove_route(self):
        '''
        removes a route connecting cityOne and cityTwo from the graph
        '''
        
        user_query_one = ""      #The buffer that holds the user input
        user_query_one = raw_input("Please enter the first city of the route you want to remove. ")
        
        user_query_two = ""
        user_query_two = raw_input("Please enter the second city of the route you want to remove. ")
        
        cityOne = self.list_of_metros[user_query_one]
        cityTwo = self.list_of_metros[user_query_two]        
        self.list_of_routes = [route for route in self.list_of_routes if not ((route.destination.name == cityOne.name and route.origin.name == cityTwo.name)
                                                                          or (route.destination.name == cityTwo.name and route.origin.name == cityOne.name))]
        
        for destination in cityOne.routes.keys():
            if (destination == cityTwo.code):
                del cityOne.routes[destination]
                    
        for destination in cityTwo.routes.keys():
            if (destination == cityOne.code):
                del cityTwo.routes[destination]
                
    def add_city(self):
        '''
        Adds a city (node) to the graph
        '''
        code = raw_input("What is the metro's code? ")
        name = raw_input("What is the metro's name? ")
        country = raw_input("Where country is the metro in? ")
        continent = raw_input("What continent is the metro in? ")
        timezone = raw_input("What timezone is the metro in? ")
        coordOneDir = raw_input("What is the first heading of the coordinate? ")
        coordOneVal = raw_input("What is the degree of the first heading? ")
        coordTwoDir = raw_input("What is the second heading of the coordinate? ")
        coordTwoVal = raw_input("What is the degree of the second heading? ")
        coordinates = {coordOneDir: coordOneVal, coordTwoDir: coordTwoVal}
        population = raw_input("What is the population of the metro? ")
        region = raw_input("What is the region of the metro? ")
        city = Metro(code, name, country, continent, timezone, coordinates, population, region, {})
        self.list_of_metros[city.name] = city
        city.printInformation()
        
    def add_route(self):
        '''
        Adds a route (edge) to the graph
        '''
        user_query_one = raw_input("Please enter the first city of the route you want to add. ")
        user_query_two = raw_input("Please enter the second city of the route you want to add. ")
        routeDistance = raw_input("Please enter the distance between the two cities. ")
        
        cityOne = self.list_of_metros[user_query_one]
        cityTwo = self.list_of_metros[user_query_two]
        
        route = Route(cityOne, cityTwo, routeDistance)
        returnRoute = Route(cityTwo, cityOne, routeDistance)
        
        cityOne.routes[cityTwo.code] = route
        cityTwo.routes[cityOne.code] = returnRoute
        
        self.list_of_routes.append(route)
        
    def edit_city(self):
        '''
        Edits a specified city
        '''
        city = raw_input("What city would you like to edit? ")
        city = self.list_of_metros[city]
        attribute = raw_input("Which attribute would you like to edit? ")
        if (attribute == "code"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setCode(change)
        elif (attribute == "name"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            self.list_of_metros[change] = city
            del self.list_of_metros[city.name]
            city.setName(change)
        elif (attribute == "country"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setCountry(change)
        elif (attribute == "continent"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setContinent(change)
        elif (attribute == "timezone"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setTimezone(change)
        elif (attribute == "coordinates"):
            city.setCoordinates()
        elif (attribute == "population"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setPopulation(change)
        elif (attribute == "region"):
            change = raw_input("What would you like to change " + attribute + " to? ")
            city.setRegion(change)

    def save_to_file(self):
        '''
        saves the current network to a user-specified file name
        '''
        fileName = raw_input('Where would you like to save the network data? Please end the name with ".json')
        json_file = {}
        json_file["data sources"] = ["http://www.gcmap.com/" ,
                                    "http://www.theodora.com/country_digraphs.html" ,
                                    "http://www.citypopulation.de/world/Agglomerations.html" ,
                                    "http://www.mongabay.com/cities_urban_01.htm" ,
                                    "http://en.wikipedia.org/wiki/Urban_agglomeration" ,
                                    "http://www.worldtimezone.com/standard.html"]
        json_file["metros"] = []
        json_file["routes"] = []
        for key in self.list_of_metros:
            dict = {"code": self.list_of_metros[key].code,
                    "name": self.list_of_metros[key].name,
                    "country": self.list_of_metros[key].country,
                    "continent": self.list_of_metros[key].continent,
                    "timezone": self.list_of_metros[key].timezone,
                    "coordinates": self.list_of_metros[key].coordinates,
                    "population": self.list_of_metros[key].population,
                    "region": self.list_of_metros[key].region
                    }          
            json_file["metros"].append(dict)
        for route in self.list_of_routes:
            portList = [route.origin.code, route.destination.code]
            dict = {"ports": portList,
                    "distance": route.distance
                    }
            json_file["routes"].append(dict)                
        with open(fileName, 'a') as outfile:
            json.dump(json_file, outfile, indent=4, separators = (',',':'))
        
    def calculate_distance_cost_and_time(self):
        '''
        Calculates the distance, cost, and time to travel to user specified locations in one trip
        '''
        travel_list = []
        user_input = raw_input("Where are you currently? ")
        origin = user_input
        while(user_input!="exit"):
            user_input= raw_input("Where would you like to travel? ")
            if self.list_of_metros.has_key(user_input):
                travel_list.append(user_input)
            elif (user_input!="exit"):
                print "Please enter a valid location. Type 'exit' to complete your list."
        if not self.is_valid_path(origin, travel_list):
            print "This is not a valid path"
            return
        distance = self.calculate_distance(origin, travel_list)
        cost = self.calculate_cost(origin, travel_list)
        time = self.calculate_time(origin, travel_list)
        print "The total distance of your trip is", str(distance) + " kilometers."
        print "The total cost of your trip is", str(cost) + " dollars."
        print "The total time for your trip is", str(time) + " minutes."
    
    def is_valid_path(self, origin, travel_list):
        '''
        checks if a specified path is valid
        '''    
        current = origin
        for location in travel_list:
            current_city = self.list_of_metros[current]
            destination_city = self.list_of_metros[location]
            if not current_city.routes.has_key(destination_city.code):
                return False
            current = location
        return True
        
    def calculate_distance(self, origin, travel_list):
        '''
        returns the total distance of a travel_list
        '''
        total_len = 0
        current = origin
        if len(travel_list) == 0:
            return total_len
        for location in travel_list:
            current_city = self.list_of_metros[current]
            destination_city = self.list_of_metros[location]
            total_len += current_city.routes[destination_city.code].distance
            current = location
        return total_len
    
    def calculate_cost(self, origin, travel_list):
        '''
        returns the total cost of a travel_list
        '''
        leg_num = 0
        current = origin
        total_cost = 0
        if len(travel_list) == 0:
            return total_cost
        for location in travel_list:
            if leg_num > 7:
                leg_num = 7
            current_city = self.list_of_metros[current]
            destination_city = self.list_of_metros[location]
            total_cost += (current_city.routes[destination_city.code].distance) * (.35-.05*leg_num)
            leg_num+=1
            current = location
        return total_cost
    
    def calculate_time(self, origin, travel_list):
        '''
        returns the total travel time of the travel_list
        '''
        current = origin
        total_time = 0.0
        first_leg = True
        if len(travel_list) == 0:
            return total_time
        for location in travel_list:
            current_city = self.list_of_metros[current]
            destination_city = self.list_of_metros[location]
            if not first_leg:
                total_time += len(current_city.routes)*10
            distance = current_city.routes[str(destination_city.code)].distance
            if distance < 400:
                acceleration = (750.0**2.0)/(distance)
                total_time += (2.0*((distance/acceleration)**.5))*60.0
            else:
                acceleration = (750.0**2.0)/(2.0*200.0)
                distance -= 400.0
                total_time += (2.0*((400.0/acceleration)**.5))*60.0
                total_time += (distance/750.0)*60.0
            current = location
            first_leg = False
        return total_time
            
    def calculate_shortest_path(self):
        '''
        Runs djikstra's algorithm
        '''
        origin = raw_input("Where are you currently? ")
        destination = raw_input("What is your destination? ")
        travel_list = []
        unvisited = copy.deepcopy(self.list_of_metros)
        current = unvisited[origin]
        destination = self.list_of_metros[destination]
        current.djikstras_distance = 0
        while (len(unvisited)!=0):
            best = unvisited[unvisited.keys()[0]]
            for node in unvisited:
                node = unvisited[node]
                if (node.djikstras_distance < best.djikstras_distance):
                    best = node            
            current = best
            if (current.djikstras_distance == float('+inf')):
                return
            current.djikstras_visit = True
            if current.name == destination.name:
                break
            del unvisited[current.name]     
            
            for route in current.routes:
                route = current.routes[route]
                if (not route.destination.djikstras_visit and
                    current.djikstras_distance+route.distance < route.destination.djikstras_distance):
                    route.destination.prev = current
                    route.destination.djikstras_distance = current.djikstras_distance+route.distance            
        current = unvisited[destination.name]
        while (current.prev != None):
            travel_list.append(current.name)
            current = current.prev
        travel_list.reverse()
        distance = self.calculate_distance(origin, travel_list)
        cost = self.calculate_cost(origin, travel_list)
        time = self.calculate_time(origin, travel_list)
        print "The total distance of your trip is", str(distance) + " kilometers."
        print "The total cost of your trip is", str(cost) + " dollars."
        print "The total time for your trip is", str(time) + " minutes."
                    

        

            
              
                    
                    
                      
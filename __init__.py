# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:00:45 2014

@author: Oscar
"""

import json
import fileinput
import Graph
import sys
from Graph import Network


def print_options():
    '''
    Prints the options available to the user upon menu startup
    '''
    options = [str(x) + ". " + commands[x][0] for x in range(0, len(commands))]
    print '\n'.join(options)  

def exit_loop():
    '''    
    Exits the while loop by calling system's exit function
    '''
    print "Thank you for using CSAir!"
    sys.exit()
    
def generate_data(file_list):
    '''
    Loads and generates a compiled dictionary of jsonData to be parsed
    '''
    first_file = False
    master_data = json.loads(open(file_list[0]).read())
    for item in file_list:
        if (first_file):
            data = json.loads(open(item).read()) #The data that is read from the .json file
            for metro in data["metros"]:
                master_data["metros"].append(metro)
            for route in data["routes"]:
                master_data["routes"].append(route)
        first_file = True
    return master_data
  


'''
The main code that is actually executed
'''
file_list = []
file_name = ""
while (file_name !="exit"):
    file_name = raw_input("Please enter the files you want to populate the network with. ")
    if (file_name!="exit"):
        file_list.append(file_name)
json_data = generate_data(file_list)
CSAir = Network(json_data)

#A list of commands that includes the text printed for the query, and the function called as a result of selecting that query

commands = [["Print serviced cities.", CSAir.print_cities],
            ["Print a list of serviced continents with their serviced cities", CSAir.print_continents_and_cities],
            ["Print city information.", CSAir.print_city_information],
            ["Print the longest flight.", CSAir.print_longest_flight],
            ["Print the shortest flight.", CSAir.print_shortest_flight],
            ["Print the average flight distance.", CSAir.print_average_flight_distance],
            ["Print the largest city (by population) serviced.", CSAir.print_city_with_largest_pop],
            ["Print the smallest city (by population) serviced.", CSAir.print_city_with_smallest_pop],
            ["Print the average population of cities serviced.", CSAir.print_average_city_pop],
            ["Print CSAir's hub cities.", CSAir.print_hub_cities],
            ["Open map of CSAir's service routes.", CSAir.open_route_map],
            ["Remove a city from the network.", CSAir.remove_city],
            ["Remove a route from the network.", CSAir.remove_route],
            ["Add a city to the network.", CSAir.add_city],
            ["Add a route to the network.", CSAir.add_route],
            ["Edit an existing city.", CSAir.edit_city],
            ["Save the network to disk.", CSAir.save_to_file],
            ["Calculate data on a path.", CSAir.calculate_distance_cost_and_time],
            ["Find the shortest path between two cities and calculate data.", CSAir.calculate_shortest_path],
            ["Exit", exit_loop]
            ]
    
print "Welcome to the CSAir menu!"
while (1):
    print_options()
    user_query = raw_input("Please enter the number that matches your query. ")
    try:
        user_query = int(user_query)
        commands[user_query][1]()
    except SystemExit as e:
        sys.exit()
    except:
        print ("Please enter a valid input")
       
        
    
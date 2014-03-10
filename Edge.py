'''
Created on Feb 25, 2014

@author: Oscar
'''

class Route(object):
    origin = None
    destination = None
    distance = 0
    
    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance
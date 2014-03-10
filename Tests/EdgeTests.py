'''
Created on Feb 27, 2014

@author: Oscar
'''
import unittest
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from Edge import Route



class TestEdge(unittest.TestCase):

    '''
    Tests the constructor the make sure that things are being initialized properly
    '''
    def testConstructor(self):
        route = Route(None, None, 0)
        self.assertEqual(None, route.origin)
        self.assertEqual(None, route.destination)
        self.assertEqual(0, route.distance)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
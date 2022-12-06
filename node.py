from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

# Class to handle the objects in the grid
class Node:

    # Class attribute
    '''
    args are name + clockwise
    parameter
        north: o / i ("out" or "in" )
        east: o / i ("out" or "in" )
        south: o / i ("out" or "in" )
        west: o / i ("out" or "in" )
        type: r, i, m (road, intersection, or block)
        name: String (name of node)
    '''

    def __init__(self, name, type, TN, TE, TS, TW):
        self.TN = TN
        self.TS = TS
        self.TE = TE
        self.TW = TW
        self.name = name
        self.type = type

        # if type == "Block":
        #     self.is_obstacle = True
        # else:
        #     self.is_obstacle = False

    def __str__(self):
        return f"\nTN: {self.TN}\nTE: {self.TE}\nTS: {self.TS}\nTW: {self.TW}"


    def set_obstacle(self):
        self.TN = False
        self.TS = False
        self.TE = False
        self.TW = False
        self.is_obstacle = True

    def get_x(self):
        return int(self.name[0])
    
    def get_y(self):
        return int(self.name[1])

    

    




map = [[
    Node("00", "Intersection", True, True, True, True),
    Node("01", "Road", False, True, False, True),
    Node("02", "Intersection", True, True, True, True),
    Node("03", "Road", False, True, False, True),
    Node("04", "Intersection", True, True, True, True)
],
       [
           Node("10", "Road", True, False, True, True),
           Node("11", "Block", False, False, False, False),
           Node("12", "Road", True, False, True, True),
           Node("13", "Block", False, False, False, False),
           Node("14", "Road", True, False, True, True)
       ],
       [
           Node("20", "Intersection", True, True, True, True),
           Node("21", "Road", False, True, False, True),
           Node("22", "Intersection", True, True, True, True),
           Node("23", "Road", False, True, False, True),
           Node("24", "Intersection", True, True, True, True)
       ],
       [
           Node("30", "Road", True, False, True, True),
           Node("31", "Block", False, False, False, False),
           Node("32", "Road", True, False, True, True),
           Node("33", "Block", False, False, False, False),
           Node("34", "Road", True, False, True, True)
       ],
       [
           Node("40", "Intersection", True, True, True, True),
           Node("41", "Road", False, True, False, True),
           Node("42", "Intersection", True, True, True, True),
           Node("43", "Block", False, False, False, False),
           Node("44", "Intersection", True, True, True, True)
       ]]



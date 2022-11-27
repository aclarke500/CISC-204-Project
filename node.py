from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood

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



        


# North, East, South, West
# Read map as array Anm
map = [
        [Node("00", "Intersection", False, True, True, False), Node("01", "Road", False, True, False, True), Node("02", "Intersection", False, False, True, True)],

        [Node("10", "Road", True, False, True, False), Node("11", "Block", False, False, False, False), Node("12", "Road", True, False, True, False)],


        [Node("20", "Intersection", True, True, False, False), Node("21", "Road",False, True, False, True), Node("22", "Intersection", True, False, False, True)]
    ]

    # returns true or false
    # determn
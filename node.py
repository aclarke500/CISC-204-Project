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

        if type == "Block":
            self.is_obstacle = True
        else:
            self.is_obstacle = False

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
def move(start, target):
        if target.is_obstacle:
            return False
    # where are these objects in relation to eachother
        start_x = int(start.name[0])
        start_y = int(start.name[1])

        target_x = int(target.name[0])
        target_y = int(target.name[1])
        print(f'Start x: {start_x}, Target x: {target_x}')

        print(f'Start y: {start_y}, Target y: {target_y}')
        
    # what is our direction
        # if target is above start
        if start_x > target_x:
            if start.TN == False:
                return False
            if target.TS == False:
                return False
            else:
                return True
        # if target is above start     
        elif start_x < target_x:
            if start.TS == False:
                return False
            if target.TN == False:
                return False
            else:
                return True
        # we are going to the left (west)
        elif start_y > target_y:

            if start.TW == False:
                return False
            if target.TE == False:
                return False
            else:
                return True

        # we are going to the right (east)
        elif start_y < target_y:
            if start.TE == False:
                return False
            if target.TW == False:
                return False
            else:
                return True

            

    # can we leave start in that direction
    # can we go to target from that direction

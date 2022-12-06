from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map


def make_move(start, end, dir):

    E = Encoding()


    # all propositions should have these vars
    @proposition(E)
    class DirectionPropositions:
        def __init__(self, data):
            self.data = data
        
        def __repr__(self):
            return f"A.{self.data}"

    E.clear_constraints()

    # move_direction represents if we are moving in that direction
    move_east = DirectionPropositions("move_east")
    move_west = DirectionPropositions("move_west")
    move_north = DirectionPropositions("move_north")
    move_south = DirectionPropositions("move_south")

    # these represent where the end is in relation to the current node
    above = DirectionPropositions("above")
    below = DirectionPropositions("below")
    left = DirectionPropositions("left")
    right = DirectionPropositions("right")


    # where end is in relation to start needs to align with the direction we are currently attempting
    E.add_constraint((right & move_east) | (above & move_north) | (below & move_south) | (left & move_west) )

    '''
    For each direction we want to try, set moving_direction to true,
    and all others to false. This means all of the other disjuncts will fail if the
    node is not in the right relation (i.e right and move_east) and only the cases we want
    to pass will.
    '''
    
    
    if dir == "east":
        E.add_constraint(move_east)
        E.add_constraint(~move_west)
        E.add_constraint(~move_north)
        E.add_constraint(~move_south)
    elif dir == "west":
        E.add_constraint(~move_east)
        E.add_constraint(move_west)
        E.add_constraint(~move_north)
        E.add_constraint(~move_south)
        
    elif dir == "south":
        E.add_constraint(~move_east)
        E.add_constraint(~move_west)
        E.add_constraint(~move_north)
        E.add_constraint(move_south)
    elif dir == "north":
        E.add_constraint(~move_east)
        E.add_constraint(~move_west)
        E.add_constraint(move_north)
        E.add_constraint(~move_south)
    

    '''
    Depending on the direction we are checking, we want to compare the x and y values. 
    Similair to above, we want to set the constraints such that only the one case we want to pass, passes.
    We set all others to false to ensure no false positives. 
    '''

    if (dir == "north" or dir == "south") and (start.get_x() > end.get_x()):
        E.add_constraint(above)
        E.add_constraint(~below)
        E.add_constraint(~left)
        E.add_constraint(~right)

    elif (dir == "north" or dir == "south") and (start.get_x() < end.get_x()):
        E.add_constraint(~above)
        E.add_constraint(below)
        E.add_constraint(~left)
        E.add_constraint(~right)

    elif (dir == "west" or dir == "east") and (start.get_y() > end.get_y()):
        E.add_constraint(~above)
        E.add_constraint(~below)
        E.add_constraint(left)
        E.add_constraint(~right)

    
    elif (dir == "west" or dir == "east") and (start.get_y() < end.get_y()):
        E.add_constraint(~above)
        E.add_constraint(~below)
        E.add_constraint(~left)
        E.add_constraint(right)

    
    return E




'''
This function will automatically create a path (legal or not) based on the input of the user.
It will check where the end is in relation to the start, and horizontally align itself.
Then, it will check whether it is north or south, and vertically align itsef.

@param beginning - starting node
@param end - ending node
'''
def create_path(beginning, end):

    path =[[],
            []]

    # add beginning to lists
    print(f"Starting node: {beginning.get_x()}{beginning.get_y()}")
    path[0].append(map[beginning.get_x()][beginning.get_y()])


    current_node = beginning

    # we prioritize horizintal paths then vertical paths

    d = "east" # check if we are east
    T = make_move(current_node, end, d)
    T = T.compile()

    if (T.satisfiable()):
        # if heading east is valid
        while(current_node.get_y() < end.get_y()  ):
            # head east till horizontally aligned
            current_node=map[current_node.get_x()][current_node.get_y()+1]
            path[0].append(current_node)

    else:
        
        d = "west"
        T = make_move(current_node, end, d)
        T = T.compile()

        if (T.satisfiable()):
            # if heading west is valid
            while(current_node.get_y() > end.get_y()):
                # head west to horizontally aligned
                current_node=map[current_node.get_x()][current_node.get_y()-1]
                path[0].append(current_node)



    # NOW WE ARE HORIZONTALLY ALIGNED
    d = "north"
    T = make_move(current_node, end, d)

    T = T.compile()

    if (T.satisfiable()):
        # if going north is valid
        while(current_node.get_x() > end.get_x()):
            # head north till vertically aligned
            current_node=map[current_node.get_x()-1][current_node.get_y()]
            path[0].append(current_node)

    else:
        
        d = "south"
        T = make_move(current_node, end, d)

        T = T.compile()    
        if (T.satisfiable()):
            # if going south is valid
            while(current_node.get_x() < end.get_x()):
                # travel south until vertically aligned
                current_node=map[current_node.get_x()+1][current_node.get_y()]
                path[0].append(current_node)


    return path
    


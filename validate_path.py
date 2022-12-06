from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map

'''
This function will validate whether a path is valid or not by using 
logic and the conditions set on the grid. 

@param start - starting node
@param targert - target node
'''
def verus_theory(start, target):
 #___DECLARING__CLASSES__AND__PROPOSITIONS

    # moved this into the function for scoping reasons
    E = Encoding()


    # Proposition for location
    @proposition(E)
    class LocationPropositions:
        def __init__(self, data):
            self.data = data
        
        def __repr__(self):
            return f"A.{self.data}"


    # _______PROPOSITIONS__________

    # Propositions for which direction we ARE moving
    move_east = LocationPropositions("move_east")
    move_west = LocationPropositions("move_west")
    move_north = LocationPropositions("move_north")
    move_south = LocationPropositions("move_south")

    # Propositions for which directions a node allows us to move to
    start_north = LocationPropositions("start_north")
    start_south = LocationPropositions("start_south")
    start_east = LocationPropositions("start_east")
    start_west = LocationPropositions("start_west")

    # Propositions for which directions we can come into a node
    target_north = LocationPropositions("target_north")
    target_south = LocationPropositions("target_south")
    target_east = LocationPropositions("target_east")
    target_west = LocationPropositions("target_west")


    #__LOGIC STARTS___HERE___
    '''
    Obs: Assume matrix notation Amn, with m being rows and n being columns.
    Example of matrix, with index mn
    00   01    02
    10   11    12
    20   21    22
    '''
    start_row = int(start.name[0])
    target_row = int(target.name[0])
    
    start_column = int(start.name[1])
    target_column = int(target.name[1])


    #Checking if our target is a block (i.e., doesn't accept us coming from any coordinate.)
    if not (target.TN or target.TS or target.TW or target.TE):
        E.add_constraint(~(target_north| target_south | target_west | target_east))

    #__ADD__DIRECTIONAL___CONTRAINTS  
    # Checking if the start node allows us to go a certain direction     
    E.add_constraint(start_north) if (start.TN) else E.add_constraint(~start_north)
    E.add_constraint(start_east) if (start.TE) else E.add_constraint(~start_east)
    E.add_constraint(start_south) if (start.TS) else E.add_constraint(~start_south)
    E.add_constraint(start_west) if (start.TW) else E.add_constraint(~start_west)
    
    # Checking if the target node allows us to come from a certain direction     
    E.add_constraint(target_north) if (target.TN) else E.add_constraint(~target_north)
    E.add_constraint(target_east) if (target.TE) else E.add_constraint(~target_east)
    E.add_constraint(target_south) if (target.TS) else E.add_constraint(~target_south)
    E.add_constraint(target_west) if (target.TW) else E.add_constraint(~target_west)

    #___FIND____DIRECTION_______
    # if the target row is smaller than the start row, then we can go north, hence can't go south
    if (target_row < start_row):
        E.add_constraint(move_north)
        E.add_constraint(~move_south)
    else:
        E.add_constraint(~move_north)
    # if the target row is greater than the start row, then we can go south, hence can't go north
    if (target_row > start_row):
        E.add_constraint(move_south)
        E.add_constraint(~move_north)
    else:
         E.add_constraint(~move_south)
    # if the target column is smaller than the start column, then we can go west, hence can't go east
    if (target_column < start_column):
        E.add_constraint(move_west)
        E.add_constraint(~move_east)
    else:
         E.add_constraint(~move_west)
    # if the target column is greater than the start column, then we can go east, hence can't go west
    if (target_column > start_column):
        E.add_constraint(move_east)
        E.add_constraint(~move_west)
    else:
         E.add_constraint(~move_east)


    # Moving diagonally is not allowed, hence per say if we are moving east, we can't move south, north, and west.
    E.add_constraint(move_east >> ~(move_south | move_north | move_west))
    E.add_constraint(move_west >> ~(move_south | move_north | move_east))
    E.add_constraint(move_south >> ~(move_east | move_north | move_west))
    E.add_constraint(move_north >> ~(move_east | move_south | move_west))

    
    # CHecking if the target and start nodes are the same, if so, the code should break.
    if ((target_row == start_row) and (target_column == start_column)):
        print("Already in target, please choose another target")
        # if already on target, bugger the model
        E.add_constraint(move_north & ~move_north)
        E.add_constraint(move_east & ~move_east)
        E.add_constraint(move_south & ~move_south)
        E.add_constraint(move_west & ~move_west)


    #__ADD_IMPLICATIONS___TO__VALIDATE
    # If we are moving north, our target should allow us to come from south and the start node should allow us to leave through north
    E.add_constraint(move_north >> (target_south & start_north))
    # If we are moving south, our target should allow us to come from north and the start node should allow us to leave through south
    E.add_constraint(move_south >> (target_north & start_south))
    # If we are moving east, our target should allow us to come from west and the start node should allow us to leave through east
    E.add_constraint(move_east >> (target_west & start_east))
    # If we are moving west, our target should allow us to come from east and the start node should allow us to leave through west
    E.add_constraint(move_west >> (target_east & start_west))
    return E
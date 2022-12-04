from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map
from allMoves import PossiblePaths
from termcolor import colored



def move_east_theory(start, end):

E = Encoding()




'''
WIP
    takes in beginning and end point

    start by moving on horizontal axis until beginning and end are lined up
    then go up or down until they match
    appends nodes to a path (the hops)
    this path is then validated
'''
def path_creator(beginning, end):
    #___DECLARING__CLASSES__AND__PROPOSITIONS

    # moved this into the function for scoping reasons
    E = Encoding()

    beginning_row = int(beginning.name[0])
    end_row = int(end.name[0])
    
    beginning_column = int(beginning.name[1])
    end_column = int(end.name[1])


    # all propositions should have these vars
    @proposition(E)
    class LocationPropositions:
        def __init__(self, data):
            self.data = data
        
        def __repr__(self):
            return f"A.{self.data}"


    # declaring propositions

    # we are moving in this direction
    move_east = LocationPropositions("move_east")
    move_west = LocationPropositions("move_west")
    move_north = LocationPropositions("move_north")
    move_south = LocationPropositions("move_south")


    if (end_row > beginning_row):
        E.add_constraint(move_north) 
        #move(north)
    else:
         E.add_constraint(~move_north)


    E.add_constraint(move_north) if (end_row > beginning_row) else E.add_constraint(~move_north)
    # if target is to the left of start
    E.add_constraint(move_south) if (end_row < beginning_row) else E.add_constraint(~move_west)
    # if target is above start
    E.add_constraint(move_west) if (end_column < beginning_column) else E.add_constraint(~move_north)
    # if target is below start
    E.add_constraint(move_east) if (end_column > beginning_column) else E.add_constraint(~move_east)

    
    



def nodes_equal(node_1, node_2):
    return (node_1.name[0]==node_2.name[0] and node_1.name[1]==node_2.name[1])


def move(start, dir):

    row = int(start.name[0])
    column = int(start.name[1])
    
    if dir == "north":
        return map[str(row-1)][str(column)]
    elif dir == "south":
        return map[str(row+1)][str(column)]
    elif dir == "east":
        return map[str(row)][str(column+1)]
    elif dir == "west":
        return map[str(row)][str(column-1)]












# tool to validate a given path
def verus_theory(start, target):


 #___DECLARING__CLASSES__AND__PROPOSITIONS

    # moved this into the function for scoping reasons
    E = Encoding()


    # all propositions should have these vars
    @proposition(E)
    class LocationPropositions:
        def __init__(self, data):
            self.data = data
        
        def __repr__(self):
            return f"A.{self.data}"


    # declaring propositions

    # we are moving in this direction
    move_east = LocationPropositions("move_east")
    move_west = LocationPropositions("move_west")
    move_north = LocationPropositions("move_north")
    move_south = LocationPropositions("move_south")

    # we can travel in this direction
    start_north = LocationPropositions("start_north")
    start_south = LocationPropositions("start_south")
    start_east = LocationPropositions("start_east")
    start_west = LocationPropositions("start_west")

    # we can travel in this direction
    target_north = LocationPropositions("target_north")
    target_south = LocationPropositions("target_south")
    target_east = LocationPropositions("target_east")
    target_west = LocationPropositions("target_west")


    #__LOGIC STARTS___HERE___
    # given two adjacent nodes, can you make that jump
    start_row = int(start.name[0])
    target_row = int(target.name[0])
    
    start_column = int(start.name[1])
    target_column = int(target.name[1])


    if not (target.TN or target.TS or target.TW or target.TE):
        E.add_constraint(~(target_north| target_south | target_west | target_east))

    #__ADD__DIRECTIONAL___CONTRAINTS       

    E.add_constraint(start_north) if (start.TN) else E.add_constraint(~start_north)
    E.add_constraint(start_east) if (start.TE) else E.add_constraint(~start_east)
    E.add_constraint(start_south) if (start.TS) else E.add_constraint(~start_south)
    E.add_constraint(start_west) if (start.TW) else E.add_constraint(~start_west)
    
    E.add_constraint(target_north) if (target.TN) else E.add_constraint(~target_north)
    E.add_constraint(target_east) if (target.TE) else E.add_constraint(~target_east)
    E.add_constraint(target_south) if (target.TS) else E.add_constraint(~target_south)
    E.add_constraint(target_west) if (target.TW) else E.add_constraint(~target_west)

    #___FIND____DIRECTION_______

    # if target is to the right in the matrix

    # start = map[2][0]
    # target = map[2][1]

    # row = 2
    # column 1
    E.add_constraint(move_north) if (target_row < start_row) else E.add_constraint(~move_north)
    # if target is to the left of start
    E.add_constraint(move_south) if (target_row > start_row) else E.add_constraint(~move_south)
    # if target is above start
    E.add_constraint(move_west) if (target_column < start_column) else E.add_constraint(~move_west)
    # if target is below start
    E.add_constraint(move_east) if (target_column > start_column) else E.add_constraint(~move_east)



    # If diagonal
    E.add_constraint(move_east >> ~(move_south | move_north | move_west))
    E.add_constraint(move_west >> ~(move_south | move_north | move_east))
    E.add_constraint(move_south >> ~(move_east | move_north | move_west))
    E.add_constraint(move_north >> ~(move_east | move_south | move_west))

    
    if ((target_row == start_row) and (target_column == start_column)):
        print("Already in target, please choose another target")
        # if already on target, bugger the model
        E.add_constraint(move_north & ~move_north)
        E.add_constraint(move_east & ~move_east)
        E.add_constraint(move_south & ~move_south)
        E.add_constraint(move_west & ~move_west)


    #__ADD_IMPLICATIONS___TO__VALIDATE
    
    E.add_constraint(move_north >> (target_south & start_north))
    E.add_constraint(move_south >> (target_north & start_south))
    E.add_constraint(move_east >> (target_west & start_east))
    E.add_constraint(move_west >> (target_east & start_west))


    return E


# def print_grid(map_of_nodes, node_name):
#     for row in map_of_nodes:
#         for element in row:
#             value = element.name
#             if value == node_name:
#                 value = colored(element.name, "green")
#             print(value, end= ' ')
#             element.name = colored(element.name, "white")
#         print()

        

if __name__ == "__main__":

    start = map[1][0]
    target = map[1][1]


    sample_path=[map[0][0],map[0][1], map[0][2], map[1][2], map[2][2], map[2][1]]

   
    for i in range(len(sample_path)-1):
        print(f"From {sample_path[i].name} to {sample_path[i+1].name}")
        T = verus_theory(sample_path[i], sample_path[i+1])
        T = T.compile()

        #print_grid(map, sample_path[i].name)

        
        print("\nSatisfiable: %s" % T.satisfiable())
        print("# Solutions: %d" % count_solutions(T))
        print("   Solution: %s" % T.solve())

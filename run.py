from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map, move
from termcolor import colored


# Encoding that will store all of your constraints
E = Encoding()

# To create Propositionss, create classes for them first, annotated with "@Propositions" and the Encoding

#TODO create our own Propositions types


class RoadPropositions:
    
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"A.{self.data}"


#Intersections need to be able to go atleast one place
@proposition(E)
class IntersectionPropositions:

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"A.{self.data}"
        
@proposition(E)
class BlockPropositons:    
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return f"A.{self.data}"

@proposition(E)
class DirectionPropositions:
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        return f"A.{self.data}"

    

#is the given node a intersection
i = IntersectionPropositions("i")

i_n = DirectionPropositions("i_n") #Intersection North
i_e = DirectionPropositions("i_e") #Intersection East
i_s = DirectionPropositions("i_s") #Intersection South
i_w = DirectionPropositions("i_w") #Intersection West

r = DirectionPropositions("r")

block = BlockPropositons("block")

def intersection_theory():
    # You need to be able to go in atleast one direction
    E.add_constraint(i >> (i_n | i_s | i_e | i_s))
    return E


def block_theory():
    E.add_constraint(block >> ~(i_n | i_s | i_w | i_e))

def road_theory():
    E.add_constraint(r >> ((i_w | i_e) >> ~(i_n | i_s)))
    E.add_constraint(r >> ((i_n | i_s) >> ~(i_w | i_e)))

    # constraint.add_exactly_one(E, a, b)

    return E


if __name__ == "__main__":



    # Don't compile until you're finished adding all your constraints!
    # After compilation (and only after), you can check some of the properties
    F = intersection_theory()
    F = F.compile()

    # G = intersection_theory()
    # G = G.compile()
    # of your model:
    # print("\nSatisfiable: %s" % F.satisfiable())
    # print("# Solutions: %d" % count_solutions(F))
    # print("   Solution: %s" % F.solve())

    # print("\nVariable likelihoods:")

    # print()

#set to node we are starting on
# cur_node = map[0][2]
# print(cur_node.name)

target = "20"
 
for i in map:
    for j in i:
        if j.name == target:
            text = colored(j.name, 'green')
        else:
            text=j.name
        print(text, end =' ')

    print()
    
if move(map[1][0], map[2][0]):
    text = colored(map[2][0], 'green')
    print(text, end =' ')
else:
    print("Invalid jump")

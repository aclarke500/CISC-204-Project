from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map
from termcolor import colored
from allMoves import PossiblePaths


# Encoding that will store all of your constraints
E = Encoding()

# To create Propositionss, create classes for them first, annotated with "@Propositions" and the Encoding

#TODO create our own Propositions types
@constraint.at_most_one(E)
@proposition(E)
class LocationPropositions:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"A.{self.data}"

a = LocationPropositions("a")
b = LocationPropositions("b")
l = LocationPropositions("l")
r = LocationPropositions("r")

@proposition(E)
class DirectionPropositions:
    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return f"A.{self.data}"


s_n = DirectionPropositions("s_n")
s_w = DirectionPropositions("s_w")
s_e = DirectionPropositions("s_e")
s_s = DirectionPropositions("s_s")

t_n = DirectionPropositions("t_n")
t_w = DirectionPropositions("t_w")
t_e = DirectionPropositions("t_e")
t_s = DirectionPropositions("t_s")

# E idk why this is here

i_n = DirectionPropositions("i_n") #Intersection North
i_e = DirectionPropositions("i_e") #Intersection East
i_s = DirectionPropositions("i_s") #Intersection South
i_w = DirectionPropositions("i_w") #Intersection West
# fail = DirectionPropositions("fail") # used to auto fail 



def main(start, target):
    E.clear_constraints()
    # make sure are adjacent or else everything goes wonky
    print("Target object: ", str(target))
    print("\nStart object", str(start))
    # relative location
    start_x = int(start.name[0])
    start_y = int(start.name[1])

    target_x = int(target.name[0])
    target_y = int(target.name[1])

    #If is block:
    if not (target.TN or target.TS or target.TW or target.TE):
        E.add_constraint(~(t_n | t_s | t_w | t_e))
        
    # add these constraints
    E.add_constraint(a >> (s_n & t_s))
    E.add_constraint(b >> (s_s & t_n))

    E.add_constraint(r >>(s_w & t_e))
    E.add_constraint(l >>(s_e & t_w))


    # is above
    if start_x - target_x == 1:
        print("Added constraint: a")
        E.add_constraint(a)
    # is below
    elif target_x - start_x   == 1:
        print("Added constraint: b")
        E.add_constraint(b)

    # we are going to the left (west)
    elif target_y - start_y  == 1:
        print("Added constraint: l")
        E.add_constraint(l)

    elif start_y - target_y == 1:
        print("Added constraint: r")
        E.add_constraint(r)

    else:
        # if no if statements fire, bugger the whole model
        print("state")
        # fore to be unsolveable 
        # E.add_constraint(fail & ~fail)
    # directional truthiness
    
    # E.add_constraint(~(t_e | t_n | t_s | t_w))
    E.add_constraint(s_n) if start.TN else E.add_constraint(~s_n)
    #TODO change to implications to beef up code 
    E.add_constraint(s_s) if start.TS else E.add_constraint(~(s_s))

    E.add_constraint(s_e) if start.TE else E.add_constraint(~(s_e))

    E.add_constraint(s_w) if start.TW else E.add_constraint(~(s_w))                
    
    E.add_constraint(t_n) if target.TN else E.add_constraint(~(t_n))
  
    E.add_constraint(t_s) if target.TS else E.add_constraint(~(t_s))
  
    E.add_constraint(t_e) if target.TE else E.add_constraint(~(t_e)) 

    E.add_constraint(t_w) if target.TW else E.add_constraint(~(t_w))

    return E


def move2(start, target):

    start_x = int(start.name[0])
    start_y = int(start.name[1])

    target_x = int(target.name[0])
    target_y = int(target.name[1])

    if start_x > target_x:
        print("Added constraint: a")
        E.add_constraint(a)

    elif start_x < target_x:
        print("Added constraint: b")
        E.add_constraint(b)

    # we are going to the left (west)
    elif start_y > target_y:
        print("Added constraint: l")
        E.add_constraint(l)

    elif start_y < target_y:
        print("Added constraint: r")
        E.add_constraint(r)


if __name__ == "__main__":
    # Don't compile until you're finished adding all your constraints!
    # After compilation (and only after), you can check some of the properties
    valid = []

    sample_path=[map[2][0],map[2][1], map[2][2]]
    violated = False
    for m in range(len(sample_path) - 1):
        
        T = main(sample_path[m],sample_path[m+1])
        #print(str(sample_path[m]),str(sample_path[m+1]))
        T = T.compile()
        if not T.satisfiable():
            print(f"M not satisfiable: {str(m)}")
            print("Start:", sample_path[m].name, "Target:", sample_path[m+1].name)
            print(str(sample_path[m]))
            print(str(sample_path[m+1]))
            violated=True
            # constraints = T.debug_constraints()
            # print(constraints)
            break    
        T = T.clear_constraints()

    if not violated:
        valid.append(sample_path)
print(valid)
        

    


        


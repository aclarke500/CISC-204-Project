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


@proposition(E)
class start_x_minus_target_x_equals_one:
    def __init__(self, data, start_x, target_x, condition=False):
        self.data = data
        self.target_x = int(target_x)
        self.start_x = int(start_x)
        self.condition = condition

        if (self.start_x - self.target_x) > 0:
            self.condition = True



@proposition(E)
class target_x_minus_start_x_equals_one:
    def __init__(self, data, target_x, start_x, condition=False):
        self.data = data
        self.target_x = int(target_x)
        self.start_x = int(start_x)
        self.condition = condition

        if (self.target_x - self.start_x) > 0:
            self.condition = True


@proposition(E)
class target_y_minus_start_y_equals_one:
    def __init__(self, data, target_y, start_y, condition=False):
        self.target_y = int(target_y)
        self.start_y = int(start_y)
        self.data = data
        self.condition = condition

        if (self.target_y - self.start_y) > 0:
            self.condition = True


@proposition(E)
class start_y_minus_target_y_equals_one:
    def __init__(self, data, start_y, target_y, condition=False):
        self.data = data
        self.target_y = int(target_y)
        self.start_y = int(start_y)
        self.condition = condition

        if (self.start_y - self.target_y) > 0:
            self.condition = True


@proposition(E)
class directional_constraint:
    def __init__(self, data, condition):
        self.condition=condition

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



# def find_direction(start, target):
#     # return booleans as to relative location between start and target
#     start_x = int(start.name[0])
#     start_y = int(start.name[1])

#     target_x = int(target.name[0])
#     target_y = int(target.name[1])

#     start_x_minus_target_x_equals_one = start_x_minus_target_x_equals_one("start_x_minus_target_x_equals_one", start_x, target_x).condition
#     target_x_minus_start_x_equals_one = target_x_minus_start_x_equals_one("target_x_minus_start_x_equals_one", target_x, start_x).condition
#     target_y_minus_start_y_equals_one = target_y_minus_start_y_equals_one("target_y_minus_start_y_equals_one", target_y, start_y).condition
#     start_y_minus_target_y_equals_one = start_y_minus_target_y_equals_one("start_y_minus_target_y_equals_one", start_y, target_y).condition

#     E.add_constraint(start_x_minus_target_x_equals_one >> a)
#     E.add_constraint(start_x_minus_target_x_equals_one >> r)
#     E.add_constraint(target_y_minus_start_y_equals_one >> l)
#     E.add_constrain(target_x_minus_start_x_equals_one >> b)



# def add_directional_constraints():
#     E.add_constraint(a >> (s_n & t_s))
#     E.add_constraint(b >> (s_s & t_n))
#     E.add_constraint(r >>(s_w & t_e))
#     E.add_constraint(l >>(s_e & t_w))


# def check_directional_constraints(beginning, end):
#         # E.add_constraint(~(t_e | t_n | t_s | t_w))
#     start_n = directional_constraint("start_n", beginning.SN).condition

#     start_s = directional_constraint("start_s", beginning.SS).condition

#     start_e = directional_constraint("start_e", beginning.SE).condition

#     start_w = directional_constraint("start_w", beginning.SW).condition

#     target_n = directional_constraint("target_n", beginning.TN).condition

#     target_s = directional_constraint("target_s", beginning.TS).condition

#     target_e = directional_constraint("target_e", beginning.TE).condition

#     target_w = directional_constraint("target_w", beginning.TW).condition
    
#     E.add_constraint((start_s >> s_s) | (~start_s & (start_s >> ~s_s)))

#     E.add_constraint((start_e >> s_e) | (~start_e & (start_e >> ~s_e)))    

#     E.add_constraint((start_w >> s_w) | (~start_w & (start_w >> ~s_w)))  

#     E.add_constraint((start_n >> s_n) | (~start_n & (start_n >> ~s_n)))  


#     E.add_constraint((target_w >> t_w) | (~target_w & (target_w >> ~t_w)))   

#     E.add_constraint((target_s >> t_s) | (~target_s & (target_s >> ~t_s)))   

#     E.add_constraint((target_e >> t_e) | (~target_e & (target_e >> ~t_e)))   

#     E.add_constraint((target_n >> t_n) | (~target_n & (target_n >> ~t_n)))  


def main(beginning, end):
    # # defining rules of where can go, deciding where to go
    # E.clear_constraints()
    # # make sure are adjacent or else everything goes wonky
    # print("Start object: ", str(beginning))
    # print("\nTarget object", str(end))

    # start_x = beginning.name[0]
    # start_y = end.name[1]

    # target_x = beginning.name[0]
    # target_y = end.name[1]

    # #global start_x_minus_target_x_equals_one, target_x_minus_start_x_equals_one, target_y_minus_start_y_equals_one, start_y_minus_target_y_equals_one


    # # start_x_minus_target_x_equals_one = start_x_minus_target_x_equals_one("start_x_minus_target_x_equals_one", start_x, target_x)
    # # target_x_minus_start_x_equals_one = target_x_minus_start_x_equals_one("target_x_minus_start_x_equals_one", target_x, start_x)
    # # target_y_minus_start_y_equals_one = target_y_minus_start_y_equals_one("target_y_minus_start_y_equals_one", target_y, start_y)
    # # start_y_minus_target_y_equals_one = start_y_minus_target_y_equals_one("start_y_minus_target_y_equals_one", start_y, target_y)

    # # E.add_constraint(start_x_minus_target_x_equals_one >> a)
    # # E.add_constraint(start_y_minus_target_y_equals_one >> r)
    # # E.add_constraint(target_y_minus_start_y_equals_one >> l)
    # # E.add_constraint(target_x_minus_start_x_equals_one >> b)

    # if not (end.TN or end.TS or end.TW or end.TE):
    #     E.add_constraint(~(t_n | t_s | t_w | t_e))

    # # bugger
    # E.add_constraint(t_n & ~t_n)


    # E.add_constraint(a >> (s_n & t_s))
    # E.add_constraint(b >> (s_s & t_n))
    # E.add_constraint(r >>(s_w & t_e))
    # E.add_constraint(l >>(s_e & t_w))

    # # find direction
    # start_n = directional_constraint("start_n", beginning.TN)

    # start_s = directional_constraint("start_s", beginning.TS)

    # start_e = directional_constraint("start_e", beginning.TE)

    # start_w = directional_constraint("start_w", beginning.TW)

    # target_n = directional_constraint("target_n", end.TN)

    # target_s = directional_constraint("target_s", end.TS)

    # target_e = directional_constraint("target_e", end.TE)

    # target_w = directional_constraint("target_w", end.TW)
    
    # E.add_constraint((start_s >> s_s) | (~start_s & (start_s >> ~s_s)))

    # E.add_constraint((start_e >> s_e) | (~start_e & (start_e >> ~s_e)))    

    # E.add_constraint((start_w >> s_w) | (~start_w & (start_w >> ~s_w)))  

    # E.add_constraint((start_n >> s_n) | (~start_n & (start_n >> ~s_n)))

    # E.add_constraint((target_w >> t_w) | (~target_w & (target_w >> ~t_w)))   

    # E.add_constraint((target_s >> t_s) | (~target_s & (target_s >> ~t_s)))   

    # E.add_constraint((target_e >> t_e) | (~target_e & (target_e >> ~t_e)))   

    # E.add_constraint((target_n >> t_n) | (~target_n & (target_n >> ~t_n)))  

    # return E


    E.clear_constraints()
    # make sure are adjacent or else everything goes wonky
    print("Target object: ", str(end))
    print("\nStart object", str(beginning))
    # relative location
    start_x = int(beginning.name[0])
    start_y = int(beginning.name[1])

    target_x = int(end.name[0])
    target_y = int(end.name[1])

    #If is block:
    if not (end.TN or end.TS or end.TW or end.TE):
        E.add_constraint(~(t_n | t_s | t_w | t_e))
        
    # add these constraints
    E.add_constraint(a >> (s_n & t_s))
    E.add_constraint(b >> (s_s & t_n))

    E.add_constraint(r >>(s_w & t_e))
    E.add_constraint(l >>(s_e & t_w))



    # is above
    if start_x - target_x > 0:
        print("Added constraint: a")
        E.add_constraint(a)
    # is below
    elif target_x - start_x >  0:
        print("Added constraint: b")
        E.add_constraint(b)

    # we are going to the left (west)
    elif target_y - start_y  > 0:
        print("Added constraint: l")
        E.add_constraint(l)

    elif start_y - target_y > 0:
        print("Added constraint: r")
        E.add_constraint(r)

    else:
        # if no if statements fire, bugger the whole model
        print("state")
        # fore to be unsolveable 
        # E.add_constraint(fail & ~fail)
    # directional truthiness
    
    #E.add_constraint(~(t_e | t_n | t_s | t_w))
    
    start_n = directional_constraint("start_n", beginning.TN)

    start_s = directional_constraint("start_s", beginning.TS)

    start_e = directional_constraint("start_e", beginning.TE)

    start_w = directional_constraint("start_w", beginning.TW)

    target_n = directional_constraint("target_n", end.TN)

    target_s = directional_constraint("target_s", end.TS)

    target_e = directional_constraint("target_e", end.TE)

    target_w = directional_constraint("target_w", end.TW)

    E.add_constraint(~(target_n | target_s | target_w | target_e) >> ~(t_n | t_s | t_w | t_e))
    
    #E.add_constraint((start_s >> s_s) & (~start_s & (start_s >> ~s_s)))

    #E.add_constraint((start_s >> s_s) | ~(start_s >> s_s))
    E.add_constraint((start_s >> s_s) & (~start_s >> ~s_s))

    E.add_constraint((start_n >> s_n) & (~start_n >> ~s_n))

    E.add_constraint((start_e >> s_e) & (~start_e >> ~s_e))

    E.add_constraint((start_w >> s_w) & (~start_w >> ~s_w))


    # E.add_constraint((start_e >> s_e) & (~start_e & (start_e >> ~s_e)))    

    # E.add_constraint((start_w >> s_w) & (~start_w & (start_w >> ~s_w)))  

    # E.add_constraint((start_n >> s_n) & (~start_n & (start_n >> ~s_n)))

    E.add_constraint((target_w >> t_w) & (~target_w  >> ~t_w))

    E.add_constraint((target_s >> t_s) & (~target_s >> ~t_s))

    E.add_constraint((target_e >> t_e) & (~target_e  >> ~t_e))   

    E.add_constraint((target_n >> t_n) & (~target_n &  ~t_n))



    return E


if __name__ == "__main__":
    # Don't compile until you're finished adding all your constraints!
    # After compilation (and only after), you can check some of the properties
    beginning = map[0][2]
    end = map[1][2]

    T = main(beginning, end)

    T = T.compile()
    
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    # TODO next steps:
   
    
    # 2. d1, then d2, n-s priority over e-w


    # While start != end 

    # 3. Try to move in d1, if it fails, try d2, if that fails, we're fucked
    # we need a function to determine validity 
    # Set target to start + di 
    # Set start to target (generate this)
    # Set target to null

    # 4. Repeat until end or fail
        
   

   
        

    


        


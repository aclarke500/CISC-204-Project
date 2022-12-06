from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from node import Node, map
from termcolor import colored

E = Encoding()

@proposition(E)
class BasicPropositionss:
    
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"


# Different classes for Propositionss are useful because this allows for more dynamic constraint creation
# for Propositionss within that class. For example, you can enforce that "at least one" of the Propositionss
# that are instances of this class must be true by using a @constraint decorator.
# other options include: at most one, exactly one, at most k, and implies all.
# For a complete module reference, see https://bauhaus.readthedocs.io/en/latest/bauhaus.html
@constraint.at_least_one(E)
@proposition(E)
class FancyPropositionss:

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"A.{self.data}"

        
# Call your variables whatever you want
a = BasicPropositionss("a")
b = BasicPropositionss("b")   
c = BasicPropositionss("c")
d = BasicPropositionss("d")



# At least one of these will be true
x = FancyPropositionss("x")
y = FancyPropositionss("y")
z = FancyPropositionss("z")


# Build an example full theory for your setting and return it.
#
#  There should be at least 10 variables, and a sufficiently large formula to describe it (>50 operators).
#  This restriction is fairly minimal, and if there is any concern, reach out to the teaching staff to clarify
#  what the expectations are.
def example_theory():
    # Add custom constraints by creating formulas with the variables you created. 
    E.add_constraint((a | b) & ~x)
    # Implication
    E.add_constraint(y >> z)
    # Negate a formula
    E.add_constraint(~(x & y))
    # You can also add more customized "fancy" constraints. Use case: you don't want to enforce "exactly one"
    # for every instance of BasicPropositionss, but you want to enforce it for a, b, and c.:
    constraint.add_exactly_one(E, a, b, c)

    return E

if __name__ == "__main__":

    

    T = example_theory()
    # Don't compile until you're finished adding all your constraints!
    T = T.compile()


    # After compilation (and only after), you can check some of the properties


    # G = intersection_theory()
    # G = G.compile()
    # of your model:
    print("\nSatisfiable: %s" % T.satisfiable())
    print("# Solutions: %d" % count_solutions(T))
    print("   Solution: %s" % T.solve())

    print("\nVariable likelihoods:")
    # for v,vn in zip([a,b,c,x,y,z], 'abcxyz'): 
    #     # Ensure that you only send these functions NNF formulas
    #     # Literals are compiled to NNF here
    #     print(" %s: %.2f" % (vn, likelihood(T, v)))
    #     print('Nahh')

    for v,vn in zip([a,b,x],"abx"):
        print(" %s: %.2f" % (vn, likelihood(T, v)))

     
    print()




# # need to be nodes
# def add_directions(start, target):
#     E.add_constraint(s_n) if start.TN else E.add_constraint(~s_n)
#     #TODO change to implications to beef up code 
#     E.add_constraint(s_s) if start.TS else E.add_constraint(~(s_s))

#     E.add_constraint(s_e) if start.TE else E.add_constraint(~(s_e))

#     E.add_constraint(s_w) if start.TW else E.add_constraint(~(s_w))                
    
    
#     E.add_constraint(t_n) if target.TN else E.add_constraint(~(t_n))
  
#     E.add_constraint(t_s) if target.TS else E.add_constraint(~(t_s))
  
#     E.add_constraint(t_e) if target.TE else E.add_constraint(~(t_e)) 

#     E.add_constraint(t_w) if target.TW else E.add_constraint(~(t_w))
      
#     return E



# def validate_move():

#     E.add_constraint(a >> (s_s & t_n))

#     E.add_constraint(b >> (s_n & t_s))

#     E.add_constraint(l >> (s_e & t_w))

#     E.add_constraint(r >> (s_w & t_e))

#     return 
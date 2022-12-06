from bauhaus import Encoding, proposition, constraint
from bauhaus.utils import count_solutions, likelihood
from validate_path import verus_theory
from create_path import create_path
from node import Node, map
from allMoves import PossiblePaths
from termcolor import colored
import time

# Function that prints the matrix Amn
list_of_nodes_in_path = []
def print_grid(grid, node):
    time.sleep(.5)
    for element in grid:
        for knot in element:
            if knot.name == node:
                value = colored(knot.name, "green")
                list_of_nodes_in_path.append(knot.name)
            elif knot.name in list_of_nodes_in_path:
                value = colored(knot.name, "green")
            else:
                value = knot.name
            print(value, end=" ")
        print()

# Function that prints the generated path
def path_grid(grid, start, end, path):
    time.sleep(.5)
    for element in grid:
        for knot in element:
            if knot.name == start:
                value = colored(knot.name, "magenta")
            elif knot.name == end:
                value = colored(knot.name, "yellow")
            elif knot.name in path:
                value = colored(knot.name, "green")
            else:
                value = knot.name
            print(value, end=" ")
        print()


# Generates a path and determines if it's valid
def check_path(beginning, end):
    # generate a path
    path = create_path(beginning, end)[0]


    # assume no moves are invalid
    violated = False


    # iterate over path 
    for i in range(len(path)-1): #we check element at i, then i+1, so if we go to i-1 incluscive we will go over the list
        # aesthetic stuff
        start_print = colored(path[i].name, "magenta")
        end_print = colored(path[i+1].name, "yellow")
        print(f"\nFrom {start_print} to {end_print}\n")

        # validate the move from i to i+1; verus is latin for verify
        T = verus_theory(path[i], path[i+1])
        T = T.compile()

        if not (T.satisfiable()):
            # if not valid, set violated to true and print out the error spot
            violated = True
            print(f"Cannot make the jump from {path[i].name} to {path[i+1].name}")
        print_grid(map, path[i].name)


    if not violated:
        # if path is all good, print the valid
        lista = [i.name for i in path]
        time.sleep(.5)

        print(f"\nThere is a valid path: {lista}\n")
        print(f"End node: {lista[len(lista)-1]}")
        print()
        start_print = colored(beginning.name, "magenta")
        end_print = colored(end.name, "yellow")
        print(f"\nPath available from {start_print} to {end_print}\n")
        path_grid(map, beginning.name, end.name, lista[1:-1])

    else:
        print("There is no valid path.\n")
        


if __name__ == "__main__":
    check_path(map[0][0], map[3][4])
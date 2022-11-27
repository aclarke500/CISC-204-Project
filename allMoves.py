# not sure what this was originally for, but I hijacked it and turned it into a list of paths
from node import map


# from AllMoves import PossiblePaths
#GRID
#   0 1 2
# 0 x x x
# 1 y y y
# 2 z z z

PossiblePaths = [
    [map[2][0], map[1][0], map[0][0], map[0][1], map[0][2]],
    [map[2][0], map[2][1], map[2][2], map[1][2], map[0][2]],  # These two will be the only valid ones

    [map[2][0], map[1][0], map[1][1], map[0][1], map[0][2]],
    [map[2][0], map[2][1], map[1][1], map[1][2], map[0][2]],
    [map[2][0], map[1][0], map[1][1], map[1][2], map[0][2]],
    [map[2][0], map[2][1], map[1][1], map[0][1], map[0][2]],
    [map[2][0], map[2][1], map[2][2], map[1][2], map[1][1], map[0][1], map[0][2]],
    [map[2][0], map[2][1], map[1][1], map[1][0], map[0][0], map[0][1], map[0][2]],
    [map[2][0], map[1][0], map[1][1], map[2][1], map[2][2], map[1][2], map[0][2]],
    [map[2][0], map[1][0], map[0][0], map[0][1], map[1][1], map[1][2], map[0][2]],
    [map[2][0], map[1][0], map[0][0], map[0][1], map[1][1], map[2][1], map[2][2], map[1][2], map[0][2]],
    [map[2][0], map[2][1], map[2][2], map[1][2], map[1][1], map[0][1], map[0][0], map[0][1], map[0][2]]
]

#map[2][0] prints the following
#TN: True
#TW: False
#TS: False
#TE: True

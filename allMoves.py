# This file is here to model the generation of possible (not legal) paths given the grid.

# The grid will be set, not randomized, just so it can be more easily troubleshooted

"""
[
['00', '01', '02'], 
['10', '11', '12'], 
['20', '21', '22']
]

Start = 20
End = 02

"""
CONST_GRID_SIZE = 3 # n x n Grid
grid = []
validPaths = []
def populate_matrix(n):
    for row in range(0,n):
        currRow =[]
        for col in range(0,n):
            currRow.append(str(row)+str(col))
        grid.append(currRow)

populate_matrix(CONST_GRID_SIZE)

for i in grid:
    print(str(i))

start = grid[2][0]
goal = grid[0][2]



    

#The values in this mock grid represent the name found in the Node object
            





        
        

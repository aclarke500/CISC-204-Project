# This file is here to model the generation of possible (not legal) paths given the grid.

# The grid will be set, not randomized, just so it can be more easily troubleshooted
grid = []

for i in range (0, 3):
    grid_a = []
    for j in range (0, 3):
        grid_a.append(str(i) + str(j))
    grid.append(grid_a)

#The values in this mock grid represent the name found in the Node object
print(grid)
"""
B = grid[2][0]
F = grid[1][2]

A = len(grid[0]+grid[1]+grid[2]) #9

D = abs(int(B[0])-int(F[0])) + abs(int(B[1])-int(F[1]))

P = [] # Possibly valid paths

for i in range (D, A, 2):    # Assuming intersections can be next to each other, otherwise i += 4

    bad_path_dict = {}
    for j in range(1, i):
        bad_path_dict[j] = []
    flag=0
    run = 1
    while run == 1:
        flag+=1
        if(flag>99):
            break
        current_path = [B]
        current_node = B
        for j in range(i):
            print("checkpoint A")
            n_bool = current_node[0] == "0"
            e_bool = current_node[1] == str(len(grid[0])-1)
            s_bool = current_node[0] == str(len(grid)-1)
            w_bool = current_node[1] == "0"

            move_made = 0

            # try heading north
            if not n_bool:
                temp_path = current_path
                try_node = grid[int(current_node[0])-1][int(current_node[1])]
                temp_path.append(try_node)
                if (try_node not in current_path) and (temp_path not in bad_path_dict[len(temp_path)]) and (temp_path not in P):
                    current_path.append(try_node)
                    current_node = try_node
                    move_made = 1
                    print("checkpoint B")
            
            # try heading east
            if (not e_bool) and move_made == 0:
                temp_path = current_path
                try_node = grid[int(current_node[0])][int(current_node[1])+1]
                temp_path.append(try_node)
                if (try_node not in current_path) and (temp_path not in bad_path_dict[len(temp_path)]) and (temp_path not in P):
                    current_path.append(try_node)
                    current_node = try_node
                    move_made = 1
                print("checkpoint C")
            # try heading south
            if not s_bool and move_made == 0:
                temp_path = current_path
                try_node = grid[int(current_node[0])+1][int(current_node[1])]
                temp_path.append(try_node)
                if (try_node not in current_path) and (temp_path not in bad_path_dict[len(temp_path)]) and (temp_path not in P):
                    current_path.append(try_node)
                    current_node = try_node
                    move_made = 1
                print("checkpoint E")
            print("checkpoint C")
            # try heading west
            if not w_bool and move_made == 0:
                temp_path = current_path
                try_node = grid[int(current_node[0])][int(current_node[1])-1]
                temp_path.append(try_node)
                if (try_node not in current_path) and (temp_path not in bad_path_dict[len(temp_path)]) and (temp_path not in P):
                    current_path.append(try_node)
                    current_node = try_node
                    move_made = 1
            print("checkpoint D")
            # no possible directions
            if move_made == 0:
                print("peanut butter")
                bad_path_dict[len(current_path)].append(current_path)
                break
            
            # made it to F
            if current_node == F:
                P.append(current_path)
                break

            # exhausted moves for this length of path
            if j == i:
                bad_path_dict[j].append(current_path)

        # No more paths to check
        print("LEN OF BAD_PATH_DICT[1]== \n\n"+ str(bad_path_dict[1]))
        if len(bad_path_dict[1]) == 1:
            run = 0
            print("CHECKPOINT Z")
            break

print(P)
            
"""
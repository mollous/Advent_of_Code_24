import numpy as np
import time

def take_step(i_direction, x, y, extra):

    direction = directions[i_direction%4]
    left_map = False

    next_x = x + direction[1]
    next_y = y + direction[0]

    
    if next_x >= n or next_x < 0 or next_y >= m or next_y < 0:
        return i_direction, x, y, True
    
    # Check if next one also #
    for _ in range(4):
        if data[next_x][next_y] == '#' or (next_x == extra[0] and next_y == extra[1]):
            i_direction += 1
            direction = directions[i_direction % 4]
            next_x = x + direction[1]
            next_y = y + direction[0]
        else:
            break
    else:
        # All 4 directions blocked
        return i_direction, x, y, True
    
    x = next_x
    y = next_y
    
    return i_direction, x, y, left_map

with open('input/day6.txt') as file:
    data = file.read().strip().split('\n')
    
n, m = len(data), len(data[0])

# places covered already
matrix_covered = np.zeros((n, m))

directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]

x_init, y_init = 0, 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "^":
            x_init, y_init = i, j

start_time = time.time()
count = 0
left_map = False


all_xy = set()
all_xy_neighbours = set()
all_xy.add((x_init, y_init))

# take a step
i_direction, x, y, left_map = take_step(0, x_init, y_init, [-1, -1])

all_xy.add((x, y))
while left_map == False:
    i_direction, x, y, left_map = take_step(i_direction, x, y, [-1, -1])
    all_xy.add((x, y))

print("--- %s seconds ---" % (time.time() - start_time))
print(f'Solution to part 1: {len(set(all_xy))}')

obstruction = 0
t = time.time()
for i in range(len(data)):
    print(i)
    for j in range(len(data[0])):
        if(data[i][j] == '#'): continue
        extra = [i, j]
        
        new_xyd = set()
        new_xyd.add((x_init, y_init, 0))

        i_direction, x, y, left_map = take_step(0, x_init, y_init, [i, j])
        new_xyd.add((x, y, i_direction % 4))
      
        while left_map == False:
            i_direction, x, y, left_map = take_step(i_direction, x, y, [i, j])
            
            # Check for obstructions
            state = (x, y, i_direction % 4)
            if state in new_xyd and (left_map == False):
                obstruction += 1
                left_map = True
            else:
                new_xyd.add(state)
            
            
print("--- %s seconds ---" % (time.time() - t))
print(f'Solution to part 2: {obstruction}')
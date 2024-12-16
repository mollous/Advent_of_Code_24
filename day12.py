import numpy as np
import time
import re

with open('input/day12.txt') as file:
    data = file.read().strip().split('\n')

num_rows, num_cols = len(data), len(data[0])

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] 

def calculate_unique_sides(locations):
    locs = set(locations)
    unique_sides = 0

    for x, y in locations:
        # start with 4 sides for each location
        doube_sides = 0
        
        # check all neighbors
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if neighbor in locs:
                double_sides += 1
        
        # each shared side is counted twice, so subtract it from 4
        unique_sides += (4 - double_sides)
    
    return unshared_sides

def get_neighbours(loc):
    x, y = loc
    c = data[x][y]
    
    # keep track of visited locations
    visited = []
    stack = [loc]
    
    while stack:
        cur_x, cur_y = stack.pop()
        if (cur_x, cur_y) in visited:
            continue
        visited.append((cur_x, cur_y))
        
        for dr, dc in directions:
            nr, nc = cur_x + dr, cur_y + dc
            if 0 <= nr < num_rows and 0 <= nc < num_cols and (nr, nc) not in visited:
                if data[nr][nc] == c and covered[nr][nc] == 0:
                    stack.append((nr, nc))
                    covered[nr][nc] = 1  # mark as covered
    
    return visited

def solve_puzzle():
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if covered[i][j] == 0:
                shape = get_neighbours([i, j])

                b = calculate_unique_sides(shape)
                count += len(a) * b
        
    return(count)

# places covered already
covered = np.zeros((num_rows, num_cols))
count = solve_puzzle()
print(f'Solution to part 1: {count}')
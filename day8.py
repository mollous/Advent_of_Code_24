import numpy as np
import re

relevant_char = set()
with open('input/day8.txt') as file:
    data = file.read().strip().split('\n')

for i in range(len(data)):
    for j in range(len(data[i])):
        relevant_char.add(data[i][j])
        
relevant_char.remove('.')
n, m = len(data), len(data[0])

def solve_puzzle(data, part_2):
    count = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if(data[i][j] != '.' and part_2):
                count += 1

            else:
                for c in relevant_char:
                    res = []
                    for key, val in enumerate(data):
                        temp = re.search(c, val)
                        if temp :
                            res.append((key, temp.start()))
                    if (i, j) in res:res.remove((i, j))
                    check = double_distance([i, j], res, part_2)
                    if(check):
                        count += 1
                        break
    return count

def double_distance(entenna, res, part_2):
    for i in range(len(res)):
        for j in range(i+1, len(res)):
            
            # Calculate relative distances
            d1 = entenna[0] - res[i][0], entenna[1] - res[i][1]
            d2 = entenna[0] - res[j][0], entenna[1] - res[j][1]
              
            if(part_2):
                try:
                    if (d1[0] / d2[0] == d1[1] / d2[1]):
                        return True
                except:
                    #division by zero
                    if (d2[0] == 0 and d1[0] == 0 and d1[1] / d2[1]):
                        return True
                    elif (d2[1] == 0 and d1[1] == 0 and d1[0] / d2[0]):
                        return True
                    else:
                        pass
            else:
                if (d1[0] == 2 * d2[0] and d1[1] == 2 * d2[1]) or ((d2[0] == 2 * d1[0] and d2[1] == 2 * d1[1])):
                    return True
    return False

count = solve_puzzle(data, False)
print(f'Solution to part 1: {count}')

count = solve_puzzle(data, True)
print(f'Solution to part 2: {count}')
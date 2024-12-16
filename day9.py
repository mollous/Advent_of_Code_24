import numpy as np
import time
import re

def create_data(input_array, part_2):
    relevant_indices = []
    relevant_dots = []
    data = []
    i = 0
    value = 0
    for c in input_array[0]:
        if(i%2 == 0):
            relevant_indices.append(len(data))
            if(part_2):
                data.append([str(value) for _ in range(int(c))])
            else:
                for _ in range(int(c)):
                    data.append(str(value))
            value += 1
            
        else:
            # add free spaces
            relevant_dots.append(len(data))
            if(part_2):
                data.append(['.' for _ in range(int(c))])
            else:
                for _ in range(int(c)):
                    data.append('.')

            
        i += 1
        
    return(data)

def solve_puzzle_one(data):
    a_copy = data.copy()

    # Initialize the count for moves performed
    count = 0
    
    while (a_copy[-1].isdigit() is False):
            a_copy.pop()
    

    # Process the array starting from the last index
    while '.' in ''.join(a_copy):
        dot_index = a_copy.index('.')
        
        if (a_copy[dot_index] == '.'):
            a_copy[dot_index] = a_copy[-1]
            a_copy.pop()
            
            
        while (a_copy[-1].isdigit() is False):
            a_copy.pop()
            
    # Calculate the weighted sum of remaining digits
    for i, value in enumerate(a_copy):
        if value.isdigit():
            count += int(value) * i

    return count

def solve_puzzle_two(data):

    for item in data[::-1]:
        if '.' in item:
            continue
        first_data = data.index(item)
        vacant = [b for b in data if '.' in b and b.count('.') >= len(item)]
        if vacant:
            first_vacant = data.index(vacant[0])
            if first_data < first_vacant:
                continue
            x = vacant[0].index('.')
            for i in range(len(item)):
                vacant[0][i+x] = item[i]
                item[i] = '.'
        
                
    count = 0
    index = 0 

    for item in data:
        for x in item:
            if x.isdigit():
                count += int(x) * index
            index += 1

    return(count)


with open('input/day9.txt') as file:
    data = file.read().strip().split('\n')

# a = create_data(data, False)
# count = solve_puzzle_one(a)
# print("Result Part 1: ", count)

a = create_data(data, True)
count = solve_puzzle_two(a)
print("Result Part 2: ", count)


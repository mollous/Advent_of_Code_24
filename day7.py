import numpy as np
import itertools
import math
import time

start_time = time.time()
outcome, factors = [], []

with open('input/day7.txt', 'r') as f:
    for line in f:
        left, right = line.strip().split(':')
        outcome.append(float(left))
        right = right.split( )
        factors.append([float(x) for x in right])


def check_formula(outcome, factors, a):
    operations = [j for j in itertools.product(a, repeat = len(factors)-1)]

    for operation in operations:
        solution = factors[0]
        for i in range(len(factors)-1):
            if (operation[i] == 0):
                solution += factors[i+1]
            elif (operation[i] == 1):
                solution = solution * factors[i+1]
            else:
                u = math.floor(math.log(factors[i+1], 10))
                solution = solution * 10**(u+1) + factors[i+1]
        if solution == outcome: return True
    return False

def solve_puzzle(outcome, factors, part_2):
    if(part_2):
        a = [0, 1, 2]
    else:
        a = [0, 1]

    count = 0
    for i in range(len(outcome)):
        b = check_formula(outcome[i], factors[i], a)
        if(b):
            count += outcome[i]

    return(count)

count = solve_puzzle(outcome, factors, False)
print(f'Solution to part 1: {int(count)}')

count = solve_puzzle(outcome, factors, True)
print(f'Solution to part 2: {int(count)}')

print(f'Computation time is {time.time() - start_time} seconds')
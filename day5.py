import numpy as np
import time
start_time = time.time()

def check_rules(job):
    for i in range(len(job)-1):
        for j in range(len(rules_new)):
            if job[i] == rules_new[j][1] and job[i+1] == rules_new[j][0]:
                return False
    return True

def order(job):
    ordered = False
    while (ordered == False):
        count_swaps = 0
        for i in range(len(job)-1):
            for j in range(len(rules_new)):
                if job[i] == rules_new[j][1] and job[i+1] == rules_new[j][0]:
                    # switch places
                    job[i], job[i+1] = job[i+1], job[i]
                    count_swaps += 1
        if (count_swaps == 0): ordered = True
    return(job)

with open('input/day5.txt') as file:
    data = file.read().strip().split('\n')

index = data.index('')
rules_new = [list(map(int, rule.split('|'))) for rule in data[0:index]]
jobs = [list(map(int, job.split(','))) for job in data[index+1:]]
    
def solve_puzzle(part_2):
    count = 0
    for job in jobs:
        a = check_rules(job)
        if(a and part_2 == False):
            count += job[int(0.5*len(job) - 0.5)]
        elif(a == False and part_2):
            #order job
            ordered_job = order(job)
            count += job[int(0.5*len(job) - 0.5)]  
            
    return(count)

count = solve_puzzle(False)
print(f'Solution to part 1: {count}')
#print("--- %s seconds ---" % (time.time() - start_time))

count = solve_puzzle(True)
print(f'Solution to part 2: {count}')
#print("--- %s seconds ---" % (time.time() - start_time))



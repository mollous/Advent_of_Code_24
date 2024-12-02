import numpy as np

with open('input/day2.txt', 'r') as f:
    data = f.readlines()
    
for i in range(len(data)):
    data[i] = data[i].strip('\n').split(' ')
    data[i] = [int(x) for x in data[i]]
    
def safety_one(array):
    diff = np.diff(array)
    
    # check if all increase
    if( all(n > 0 for n in diff)):
        return(True)
    # check if all decrease
    elif( all(n < 0 for n in diff)):
        return(True)
    else:
        return(False)
    
def safety_two(array):
    diff = abs(np.diff(array))
    
    # check if differences are between 1 and 3
    if( all(n in [1, 2, 3] for n in diff)):
        return(True)
    else:
        return(False)

def get_count(data, part_2):
    count = 0
    for i in range(len(data)):
        check1, check2 = safety_one(data[i]), safety_two(data[i])
        if(check1 and check2):
            count += 1
        elif (part_2):
            # part 2, check if removing one leads to both True
            for j in range(len(data[i])):
                new_array = data[i].copy()

                del new_array[j]
                # check for safety
                check1, check2 = safety_one(new_array), safety_two(new_array)
                if(check1 and check2):
                    count += 1
                    # stop checking this array
                    break
    return(count)

count = get_count(data, False)
print(f'Solution to part 1: {count}')

count = get_count(data, True)
print(f'Solution to part 2: {count}')
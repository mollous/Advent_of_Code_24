import re

with open('input/day3.txt', 'r') as f:
    data = f.readlines()
    
def solve_puzzle(data, part_2):
    count = 0
    enable = True
    for i in range(len(data)):
        split_data = split_input(data[i])

        if(len(split_data) == 1 and enable):
            count += find_enclosed(split_data[i])
        else:
            for j in range(len(split_data)):
                if (split_data[j] == "do()"):
                    enable = True
                elif (split_data[j] == "don't()"):
                    if(part_2):enable = False
                elif (enable):
                    count += find_enclosed(str(split_data[j]))
                else:
                    pass
                
    return(count)
    
    
def find_enclosed(s): 
    value = 0
    
    # find all matches
    matches = re.findall(r"mul\((\d*?),(\d*?)\)", s) 
    # if there are no matches return None
    if len(matches) == 0:
        return value
    if len(matches) == 1:
        value = int(matches[0][0]) *  int(matches[0][1])
        return value
    # if it is a valid number change its type to a number
    for i in range(len(matches)):
        value += int(matches[i][0]) *  int(matches[i][1])
    
    return value

def split_input(data):
    split_by = r"(do\(\)|don't\(\))"
    a = re.split(split_by, data)
    
    # Remove any empty strings from the result
    return (a)
    
count = solve_puzzle(data, False)
print(f"Solution to part 1: {count}")

count = solve_puzzle(data, True)
print(f"Solution to part 1: {count}")

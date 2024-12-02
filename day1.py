left_list, right_list = [], []

with open('input/day1.txt', 'r') as f:
    for line in f:
        left, right = line.strip().split('   ')
        left_list.append(left)
        right_list.append(right)
        
left = sorted([int(x) for x in left_list])
right = sorted([int(x) for x in right_list])

# Part 1
diff = 0
for i in range (len(left)):
    diff += abs(left[i] - right[i])
    
print(f'Solution to part 1: {diff}')

# Part 2
similarities = 0
for i in range (len(left)):
    #how many times is it in the second list?
    number = right.count(left[i])
    similarities += number * left[i]
    
print(f'Solution to part 2: {similarities}')

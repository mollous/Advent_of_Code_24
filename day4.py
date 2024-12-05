import numpy as np
import time
start_time = time.time()

# Read the input
with open('input/day4.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
    
for i in range(len(data)):
    data[i] = data[i].strip('\n')
    
n, m = len(data), len(data[0]) #for the diagonals
    
# Convert data to a numpy array for faster access
matrix = np.array([list(line) for line in data])

# Part 1

count = 0
# horizontal
for i in range(len(data)):
    a = data[i].count('XMAS')
    b = data[i].count('SAMX')
    count += (a+b)
    
# vertical
for i in range(len(data[0])):
    string = [data[x][i] for x in range(len(data[0]))]
    string = ''.join(string)
    a = string.count('XMAS')
    b = string.count('SAMX')
    count += (a+b)
    
# diagonal
diags = [matrix[::-1,:].diagonal(i) for i in range(-n,m)]
diags.extend(matrix.diagonal(i) for i in range(n,-m,-1))

for k in diags:
    string = ''.join(k)
    a = string.count('XMAS')
    b = string.count('SAMX')
    count += (a+b)
    
print(f'Solution to part 1: {count}')

# Part 2
count = 0
for i in range(1, len(matrix)-1):
    for j in range(1, len(matrix[0])-1):
        if(matrix[i][j] == 'A'):
            d1, d2 = False, False
            
            if(matrix[i-1][j-1] == 'M' and matrix[i+1][j+1] == 'S') or \
            (matrix[i+1][j+1] == 'M' and matrix[i-1][j-1] == 'S'):
                d1 = True
                
            if(matrix[i-1][j+1] == 'M' and matrix[i+1][j-1] == 'S') or \
            (matrix[i+1][j-1] == 'M' and matrix[i-1][j+1] == 'S'):
                d2 = True
            if(d1 and d2):
                count += 1
            
print(f'Solution to part 2: {count}')   
#print("--- %s seconds ---" % (time.time() - start_time))

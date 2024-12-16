from functools import lru_cache

@lru_cache(maxsize=None)
def process(stone, n):
    if n == 0:
        return 1
    if stone == 0:
        return process(1, n-1)

    if len(str(stone)) % 2: 
        return process(stone * 2024, n-1)
    
    half_len = int(len(str(stone)) / 2)

    return (process(int(str(stone)[:half_len]), n-1) + process(int(str(stone)[half_len:]), n-1))

with open('input/day11.txt') as file:
    data = file.read().strip().split('\n')

data = data[0].split(' ')
data = [int(x) for x in data]

def solve_puzzle(part_2):
    count = 0
    if(part_2):
        n = 75
    else:
        n = 25
    for item in data:
        a = process(int(item), n)
        count += a

    return(count)

count = solve_puzzle(False)
print(f'Solution to part 1 : {count}')

count = solve_puzzle(True)
print(f'Solution to part 2 : {count}')
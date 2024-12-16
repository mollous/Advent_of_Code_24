import numpy as np

with open('input/day10.txt') as file:
    data = file.read().strip().split('\n')

num_rows, num_cols = len(data), len(data[0])

class Hike:
    def __init__(self, start_place, value):
        self.start_place = start_place
        self.path = [start_place]
        self.value = value

    def add(self, new_position):
        self.path.append(new_position)
        self.value += 1


def find_hikes(data, start, part_2):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # down, right, up, left
    active_hikes = [Hike(start, 0)]

    for target_value in range(1, 10):
        new_hikes = []
        for hike in active_hikes:
            if hike.value + 1 != target_value:
                continue

            current_row, current_col = hike.path[-1]
            added = False

            for dr, dc in directions:
                nr, nc = current_row + dr, current_col + dc
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    if int(data[nr][nc]) == target_value:
                        if not added:
                            hike.add([nr, nc])
                            added = True
                        else:
                            new_hikes.append(Hike([nr, nc], target_value))

            if not added:
                hike.value = 100  # Mark hike as invalid

        active_hikes.extend(new_hikes)

    if part_2:
        return [hike.path[-1] for hike in active_hikes if hike.value == 9]
    else:
        return {(hike.path[-1][0], hike.path[-1][1]) for hike in active_hikes if hike.value == 9}


def solve_puzzle(data, part_2):
    total_count = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if data[row][col] == '0':
                total_count += len(find_hikes(data, [row, col], part_2))
    return total_count


# Solve both parts
part1_count = solve_puzzle(data, False)
print(f'Solution to part 1: {part1_count}')

part2_count = solve_puzzle(data, True)
print(f'Solution to part 2: {part2_count}')
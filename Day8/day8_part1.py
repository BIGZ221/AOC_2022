
with open("input.txt") as f:
    data = f.read().splitlines()

height_map = list(map(lambda line: list(map(int, list(line))), data))

visible = [[True for i in range(len(height_map[0]))] for j in range(len(height_map))]

def pretty_print(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def is_visible_horizontal(row, idx):
    global height_map
    height = height_map[row][idx]
    left = True
    for i in range(0, idx):
        if height_map[row][i] >= height:
            left = False
    right = True
    for i in range(len(height_map[row]) - 1, idx, -1):
        if height_map[row][i] >= height:
            right = False
    return left or right

def is_visible_vertical(col, idx):
    global height_map
    height = height_map[idx][col]
    down = True
    for i in range(0, idx):
        if height_map[i][col] >= height:
            down = False
    up = True
    for i in range(len(height_map) - 1, idx, -1):
        if height_map[i][col] >= height:
            up = False
    return up or down

def calc_visible():
    global height_map, visible
    for row in range(1, len(height_map) -1):
        for col in range(1, len(height_map[0]) - 1):
            visible[row][col] = is_visible_horizontal(row, col) or is_visible_vertical(col, row)    

def count_visible():
    global visible
    count = 0
    for row in visible:
        for col in row:
            if col:
                count += 1
    return count


calc_visible()
print(count_visible())
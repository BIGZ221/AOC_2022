
with open("input.txt") as f:
    data = f.read().splitlines()

height_map = list(map(lambda line: list(map(int, list(line))), data))

scenic_scores = [[0 for i in range(len(height_map[0]))] for j in range(len(height_map))]

def pretty_print(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def calc_scenic_horizontal(row, idx):
    global height_map
    height = height_map[row][idx]
    left_score = 0
    for i in range(idx - 1, -1, -1):
        left_score += 1
        if height_map[row][i] >= height:
            break
    right_score = 0
    for i in range(idx + 1, len(height_map[row])):
        right_score += 1
        if height_map[row][i] >= height:
            break
    return left_score * right_score

def calc_scenic_vertical(col, idx):
    global height_map
    height = height_map[idx][col]
    down_score = 0
    for i in range(idx - 1, -1, -1):
        down_score += 1
        if height_map[i][col] >= height:
            break
    up_score = 0
    for i in range(idx + 1, len(height_map)):
        up_score += 1
        if height_map[i][col] >= height:
            break
    return up_score * down_score

def calc_scenic_scores():
    global height_map, scenic_scores
    for row in range(1, len(height_map) -1):
        for col in range(1, len(height_map[0]) - 1):
            horizontal = calc_scenic_horizontal(row, col)
            vertical = calc_scenic_vertical(col, row)
            print(f"{row},{col} : {horizontal} {vertical}")
            scenic_scores[row][col] = horizontal * vertical

def get_max_scenic_score():
    global scenic_scores
    scenic_score = 0
    for row in scenic_scores:
        for col in row:
            scenic_score = max(scenic_score, col)
    return scenic_score


calc_scenic_scores()

print(get_max_scenic_score())
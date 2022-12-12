
import sys


def pretty_print(matrix):
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

height_map = list(map(lambda x: list(x), data))

def find(height_map, val):
    for i, row in enumerate(height_map):
        for j, col in enumerate(row):
            if col == val:
                return (i, j)

def get_adjacent(height_map, visited, pos):
    adj = []
    row, col = pos
    elevation = ord(height_map[row][col])
    if row > 0:
        newRow = row - 1
        if not visited[newRow][col] and elevation - ord(height_map[newRow][col]) >= -1:
            visited[newRow][col] = True
            adj.append((pos, (newRow, col)))
    if row < len(height_map) - 1:
        newRow = row + 1
        if not visited[newRow][col] and elevation - ord(height_map[newRow][col]) >= -1:
            visited[newRow][col] = True
            adj.append((pos, (newRow, col)))
    if col > 0:
        newCol = col - 1
        if not visited[row][newCol] and elevation - ord(height_map[row][newCol]) >= -1:
            visited[row][newCol] = True
            adj.append((pos, (row, newCol)))
    if col < len(height_map[row]) - 1:
        newCol = col + 1
        if not visited[row][newCol] and elevation - ord(height_map[row][newCol]) >= -1:
            visited[row][newCol] = True
            adj.append((pos, (row, newCol)))
    return adj

def path_to(height_map, start, target):
    visited = [[False for _ in row] for row in height_map]
    distances = [[0 for _ in row] for row in height_map]

    neighbors = get_adjacent(height_map, visited, start)

    while len(neighbors) > 0:
        prev, point = neighbors.pop(0)
        visited[point[0]][point[1]] = True
        neighbors.extend(get_adjacent(height_map, visited, point))
        distances[point[0]][point[1]] = distances[prev[0]][prev[1]] + 1
    return distances[target[0]][target[1]]
    
start = find(height_map, "S")
target = find(height_map, "E")

height_map[start[0]][start[1]] = "a"
height_map[target[0]][target[1]] = "z"

print(start)
print(target)

print(path_to(height_map, start, target))

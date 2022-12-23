
from copy import copy
import sys

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

data = list(map(lambda section: list(map(lambda vertex: list(map(int, vertex.split(","))), section.split(" -> "))), data))

data.append([[500, 0]])

def pretty_print(matrix):
    print('\n'.join([''.join([str(cell) for cell in row]) for row in matrix]))

def calc_dimensions(walls):
    minX = sys.maxsize
    minY = sys.maxsize
    maxX = 0
    maxY = 0
    for wall in walls:
        for vertex in wall:
            minX = min(minX, vertex[0])
            minY = min(minY, vertex[1])
            maxX = max(maxX, vertex[0])
            maxY = max(maxY, vertex[1])
    return minX, maxX, minY, maxY

def recalc_vertices(walls, minX, minY):
    for wall in walls:
        for vertex in wall:
            vertex[0] -= minX
            vertex[1] -= minY

def center_spawn(walls):
    _, _, _, maxY = calc_dimensions(walls)
    spawnX, _ = walls[-1][0]
    floorLevel = maxY + 2
    offset = floorLevel + 1 - spawnX
    for wall in walls:
        for vertex in wall:
            vertex[0] += offset

def init_area(walls):
    center_spawn(walls)
    _, _, minY, maxY = calc_dimensions(walls)
    floorLevel = maxY + 2
    width = 2 * floorLevel + 2
    height = floorLevel - minY + 1
    area = [[0 for _ in range(width)] for _ in range(height)]
    area[-1] = [1 for _ in range(width)]
    return area

def build_area(walls):
    area = init_area(walls)
    spawn = walls.pop()[0]
    area[spawn[1]][spawn[0]] = 2
    for wall in walls:
        prev = wall[0]
        for vertex in wall:
            x, y = vertex
            area[y][x] = 1
            startX, targetX = min(prev[0], x), max(prev[0], x)
            startY, targetY = min(prev[1], y), max(prev[1], y)
            for i in range(startX, targetX):
                area[y][i] = 1
            for i in range(startY, targetY):
                area[i][x] = 1
            prev = vertex
    return area, spawn

def fall(area, point):
    x, y = point
    if area[y + 1][x] == 0:
        point[1] += 1
    elif area[y + 1][x - 1] == 0:
        point[0] -= 1
        point[1] += 1
    elif area[y + 1][x + 1] == 0:
        point[0] += 1
        point[1] += 1
    else:
        area[y][x] = 3
        return False, point
    return True, point
    

minX, maxX, minY, maxY = calc_dimensions(data)
recalc_vertices(data, minX, minY)
area, spawn = build_area(data)
sand_count = 0
sand = copy(spawn)
while True:
    falling, sand = fall(area, sand)
    if sand[0] == spawn[0] and sand[1] == spawn[1]:
        sand_count += 1
        break
    if not falling:
        sand_count += 1
        sand = copy(spawn)
    
print(sand_count)    

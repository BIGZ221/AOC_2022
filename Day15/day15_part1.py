from functools import reduce
import re

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

TARGET_Y = 2_000_000
LOCATION_REGEX = re.compile(r"(?!x=)([+\-]?\d+).*?(?!y=)([+\-]?\d+)")

def extract_x_y(s):
    return list(map(lambda x: list(map(int, x)), LOCATION_REGEX.findall(s)))

def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])


sensors_beacons = map(extract_x_y, data)

sensor_beacon_distances = map(lambda pair: [pair[0], pair[1], manhattan(pair[0], pair[1])], sensors_beacons)

def in_range(args):
    global TARGET_Y
    sensor, _, distance = args
    return manhattan(sensor, [sensor[0], TARGET_Y]) < distance

sensors_in_range = list(filter(in_range, sensor_beacon_distances))
sensors_in_range.sort(key=lambda val: val[0][0])

furthest_left = sensors_in_range[0]
furthest_left_x = furthest_left[0][0] - furthest_left[2]
furthest_right = sensors_in_range[-1]
furthest_right_x = furthest_right[0][0] + furthest_right[2]

out_of_range = 0
for x in range(furthest_left_x, furthest_right_x + 1):
    pos = [x, TARGET_Y]
    is_in_range = False
    for sensor, beacon, dist in sensors_in_range:
        if beacon[0] == x and beacon[1] == TARGET_Y:
            # If pos is a beacon, we don't want to count it
            is_in_range = False
            break
        if manhattan(sensor, pos) <= dist:
            is_in_range = True
    if is_in_range:
        out_of_range += 1

print(out_of_range)

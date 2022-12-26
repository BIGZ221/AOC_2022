from functools import reduce
import re

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

MAX_COORD = 4_000_000
# MAX_COORD = 20
MIN_COORD = 0

LOCATION_REGEX = re.compile(r"(?!x=)([+\-]?\d+).*?(?!y=)([+\-]?\d+)")

def extract_x_y(s):
    return list(map(lambda x: list(map(int, x)), LOCATION_REGEX.findall(s)))

def manhattan(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

sensors_beacons = map(extract_x_y, data)

sensor_beacon_distances = list(map(lambda pair: [pair[0], pair[1], manhattan(pair[0], pair[1])], sensors_beacons))

def in_range(args, target):
    sensor, _, dist = args
    return manhattan(sensor, target) <= dist

answer = None
y = 0
while y < MAX_COORD and answer == None:
    x = 0
    while x < MAX_COORD and answer == None:
        pos = [x,y]
        sensors_in_range = list(filter(lambda s: in_range(s, pos), sensor_beacon_distances))
        if len(sensors_in_range) == 0:
            answer = pos
        else:
            sensors_in_range.sort(key=lambda s: s[0][0], reverse=True)
            sensor_beacon = sensors_in_range[0]
            sensor = sensor_beacon[0]
            sensor_dist = sensor_beacon[2]
            sensor_x = sensor[0]
            sensor_y = sensor[1]
            y_diff = abs(sensor_y - y)
            x_diff = x - sensor_x
            horizontal_dist = sensor_dist - y_diff - x_diff
            # print(sensor, sensor_dist)
            # print(x, y)
            # print(x_diff, y_diff)
            # print(horizontal_dist)
            # print()
            x += horizontal_dist
        x += 1
    y += 1

print(4000000 * answer[0] + answer[1])

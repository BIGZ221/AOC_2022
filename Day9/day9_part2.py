from math import copysign

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

class Vec2():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self) -> str:
        return str(self)

    def __str__(self):
        return f"{self.x},{self.y}"

    def __sub__(self, other):
        return Vec2(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

    def within_one(self, other):
        return abs(self.x - other.x) < 2 and abs(self.y - other.y) < 2
    
    def step_towards(self, target):
        offset = target - self
        x_off = abs(offset.x)
        y_off = abs(offset.y)
        if x_off > 0 and y_off > 0:
            self.x += int(copysign(1, offset.x))
            self.y += int(copysign(1, offset.y))
        elif x_off > 0:
            self.x += int(copysign(1, offset.x))
        elif y_off > 0:
            self.y += int(copysign(1, offset.y))

rope = [Vec2(0,0) for i in range(10)]

visited = { str(rope[-1]) }

def follow(ahead: Vec2, current: Vec2):
    if current.within_one(ahead):
        return
    current.step_towards(ahead)

def move(dir, amount):
    global visited, rope
    head = rope[0]
    for i in range(int(amount)):
        if dir == "U":
            head.y += 1
        elif dir == "R":
            head.x += 1
        elif dir == "D":
            head.y -= 1
        elif dir == "L":
            head.x -= 1
        for j in range(1, len(rope)):
            follow(rope[j - 1], rope[j])
        visited.add(str(rope[-1]))

for dir, amount in map(lambda x: x.split(), data):
    move(dir, amount)
    
print(len(visited))


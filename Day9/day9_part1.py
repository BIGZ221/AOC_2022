
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


head = Vec2(0,0)
tail = Vec2(0,0)

visited = { str(tail) }

def follow_head():
    global visited, head, tail
    if tail.within_one(head):
        return
    tail.step_towards(head)
    visited.add(str(tail))


def move(dir, amount):
    global visited, head, tail
    for i in range(int(amount)):
        if dir == "U":
            head.y += 1
        elif dir == "R":
            head.x += 1
        elif dir == "D":
            head.y -= 1
        elif dir == "L":
            head.x -= 1
        follow_head()



for dir, amount in map(lambda x: x.split(), data):
    move(dir, amount)
    
print(len(visited))


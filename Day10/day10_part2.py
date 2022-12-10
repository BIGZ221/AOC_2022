
with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

register = 1
cycle = 1
bound = 20
sum_signals = 0

crt = ""

def draw_pixel():
    global cycle, register, crt
    if abs((cycle - 1) % 40 - register) < 2:
        crt += "#"
    else:
        crt += "."
    if cycle % 40 == 0:
        crt += "\n"

for instruction in data:
    draw_pixel()
    cycle += 1
    if instruction.startswith("addx"):
        draw_pixel()
        register += int(instruction.split()[1])
        cycle += 1

print(crt)
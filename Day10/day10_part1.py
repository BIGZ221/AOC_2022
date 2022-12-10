
with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

register = 1
cycle = 1
bound = 20
sum_signals = 0

def calc_signal_strength():
    global register, bound, sum_signals
    if cycle >= bound and bound <= 220:
        sum_signals += (bound * register)
        print(bound, register, bound * register)
        bound += 40

for instruction in data:
    cycle += 1
    calc_signal_strength()
    if instruction.startswith("addx"):
        cycle += 1
        register += int(instruction.split()[1])
        calc_signal_strength()

print(sum_signals)

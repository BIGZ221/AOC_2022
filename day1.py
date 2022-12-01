
with open("input.txt") as f:
    data = f.read()

data = data.split("\n\n")

invs = {}

for i, elf in enumerate(data):
    inv = sum(list(map(int, elf.split())))
    invs[i] = inv

print(sum(sorted(invs.values(),reverse=True)[:3]))
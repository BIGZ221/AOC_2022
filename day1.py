max_inv = 0

with open("input.txt") as f:
    data = f.read()

data = data.split("\n\n")

for elf in data:
    inv = sum(list(map(int, elf.split())))
    max_inv = max(inv)

print(max_inv)

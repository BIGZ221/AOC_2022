
with open("input.txt") as f:
    data = f.read()

def is_contained(a, b):
    la, ra = list(map(int, a.split("-")))
    lb, rb = list(map(int, b.split("-")))
    return la <= lb and ra >= rb

total = 0
for pair in data.split():
    a, b = pair.split(",")
    if is_contained(a, b) == True or is_contained(b, a) == True:
        total += 1

print(total)
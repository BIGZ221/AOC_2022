
with open("input.txt") as f:
    data = f.read()

def is_contained(a, b):
    la, ra = list(map(int, a.split("-")))
    lb, rb = list(map(int, b.split("-")))
    return la <= lb and ra >= rb

def is_semi_contained(a, b):
    la, ra = list(map(int, a.split("-")))
    lb, rb = list(map(int, b.split("-")))
    if la >= lb and la <= rb:
        return True
    if ra >= lb and ra <= rb:
        return True
    
    return False


total = 0
for pair in data.split():
    a, b = pair.split(",")
    if is_contained(a, b) == True or is_contained(b, a) == True or is_semi_contained(a, b) == True:
        total += 1

print(total)
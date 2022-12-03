
with open("input.txt") as f:
    data = f.read()

rucksacks = data.split()

def get_common(a, b, c):
    return list(set(a).intersection(set(b)).intersection(set(c)))[0]

def get_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 26 + 1
    else:
        return ord(item) - ord('a') + 1

print(sum([get_priority(get_common(*rucksacks[i: i+3])) for i in range(0, len(rucksacks), 3)]))
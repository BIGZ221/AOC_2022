
with open("input.txt") as f:
    data = f.read()

rucksacks = data.split()

def get_common(rucksack):
    left, right = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    return set(left).intersection(set(right))

def get_priority(item: str):
    if item.isupper():
        return ord(item) - ord('A') + 26 + 1
    else:
        return ord(item) - ord('a') + 1

print(sum([list(map(get_priority, list(get_common(rucksack))[0]))[0] for rucksack in rucksacks]))


with open("input.txt") as f:
    data = f.read()

past_unique = []
for i, c in enumerate(data):
    try:
        c_index = past_unique.index(c)
        del past_unique[:c_index + 1]
    except:
        pass
    past_unique.append(c)
    if len(past_unique) == 14:
        print(i + 1)
        break

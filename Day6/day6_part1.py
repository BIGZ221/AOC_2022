
with open("input.txt") as f:
    data = f.read()

past_four = []
for i, c in enumerate(data):
    try:
        c_index = past_four.index(c)
        del past_four[:c_index + 1]
    except:
        pass
    past_four.append(c)
    if len(past_four) == 4:
        print(i + 1)
        break

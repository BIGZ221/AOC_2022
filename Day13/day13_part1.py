import ast

with open("input.txt") as f:
    data = f.read().split("\n\n")

data = list(map(lambda element: list(map(lambda el: ast.literal_eval(el), element.split())), data))

def in_order(left, right):
    if type(left) == type(right) and type(right) == int:
        return True if left < right else False if left > right else None
    if type(left) == type(right) and type(right) == list:
        for i in range(len(left)):
            if i >= len(right):
                return False
            ordered = in_order(left[i], right[i])
            if ordered != None:
                return ordered
        return True if len(left) < len(right) else None
    if type(left) == list:
        return in_order(left, [right])
    else:
        return in_order([left], right)

ordered = []

for i in range(len(data)):
    is_ordered = in_order(*data[i])
    if is_ordered != False:
        ordered.append(i + 1)

print(sum(ordered))

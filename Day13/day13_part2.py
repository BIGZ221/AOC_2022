import ast
from functools import cmp_to_key
from more_itertools import flatten

with open("input.txt") as f:
    data = f.read().split("\n\n")

data = list(map(lambda element: list(map(lambda el: ast.literal_eval(el), element.split())), data))

divider_packets = [[[2]], [[6]]]
data.append(divider_packets)

def in_order(left, right):
    if type(left) == type(right) and type(right) == int:
        return 1 if left < right else -1 if left > right else 0
    if type(left) == type(right) and type(right) == list:
        for i in range(len(left)):
            if i >= len(right):
                return -1
            ordered = in_order(left[i], right[i])
            if ordered != 0:
                return ordered
        return 1 if len(left) < len(right) else 0
    if type(left) == list:
        return in_order(left, [right])
    else:
        return in_order([left], right)

ordered = []

for i in range(len(data)):
    is_ordered = in_order(*data[i])
    if is_ordered != -1:
        ordered.append(i + 1)

sorted_data = sorted(flatten(data), key=cmp_to_key(in_order), reverse=True)



print((sorted_data.index(divider_packets[0]) + 1) * (sorted_data.index(divider_packets[1]) + 1))

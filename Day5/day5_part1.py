import re

stacks = ["T,V,J,W,N,R,M,S", "V,C,P,Q,J,D,W,B", "P,R,D,H,F,J,B", "D,N,M,B,P,R,F", "B,T,P,R,V,H", "T,P,B,C", "L,P,R,J,B", "W,B,Z,T,L,S,C,N", "G,S,L"]

stacks = list(map(lambda stack: stack.split(","), stacks))

with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

def make_move(count, from_index, to_index):
    for i in range(count):
        stacks[to_index].insert(0, stacks[from_index].pop(0))

moves = [list(map(int,re.findall("\d+", move))) for move in data]

for count, from_index, to_index in moves:
    make_move(count, from_index - 1, to_index -1)

print("".join([stack[0] for stack in stacks]))

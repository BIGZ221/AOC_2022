
with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

file_system = {}
total_sizes = {}

cd = []

def change_dir(dir):
    global cd
    if dir == "..":
        cd = cd[:-1]
    else:
        cd.append(dir)

def add_files():
    global file_system, cd, data
    path = "/".join(cd)
    dir_state = file_system.get(path, { "size": 0, "nested": [] })
    while len(data) > 0 and not data[0].startswith("$"):
        file = data.pop(0).split()
        if file[0] == "dir":
            dir_state["nested"].append(file[1])
        else:
            dir_state["size"] += int(file[0])
    file_system[path] = dir_state

def get_dir_size(dir):
    global file_system, total_sizes
    if dir in total_sizes:
        return total_sizes[dir]
    curr_dir = file_system[dir]
    visited = { dir }
    dirs: list = list(map(lambda nested: "/".join([dir, nested]), curr_dir["nested"]))
    sum = curr_dir["size"]
    while len(dirs) > 0:
        dir_name = dirs.pop()
        nested_dir = file_system[dir_name]
        sum += nested_dir["size"]
        visited.add(dir_name)
        for nested in nested_dir["nested"]:
            if nested not in visited:
                dirs.append("/".join([dir_name, nested]))
    return sum

# Solution would have worked if I didn't do weird path joining, see part 2 for better solution.
def calc_total_dir(dir):
    global file_system
    curr_dir = file_system[dir]
    return sum(calc_total_dir(nested) for nested in curr_dir["nested"]) + curr_dir["size"]

while len(data) > 0:
    line = data.pop(0)
    if line.startswith("$"):
        cmd = line.split()[1:]
        if cmd[0] == "cd":
            change_dir(cmd[1])
        elif cmd[0] == "ls":
            add_files()
    else:
        print("should never print")

items = sorted(file_system.items(), key=lambda item: len(item[1]["nested"]))

for dir, entry in items:
    total_sizes[dir] = get_dir_size(dir)

print(sum(filter(lambda size: size < 100_000, total_sizes.values())))

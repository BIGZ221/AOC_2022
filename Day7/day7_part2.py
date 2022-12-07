
with open("input.txt") as f:
    data = f.read().splitlines(keepends=False)

DISK_SPACE = 70_000_000
NEEDED_SPACE = 30_000_000

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
            dir_state["nested"].append(f"{path}/{file[1]}")
        else:
            dir_state["size"] += int(file[0])
    file_system[path] = dir_state
        
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

for path in file_system.keys():
    total_sizes[path] = calc_total_dir(path)

used_space = total_sizes["/"]
free_space = DISK_SPACE - used_space
viable_directories = filter(lambda size: free_space + size > NEEDED_SPACE, total_sizes.values())

print(sorted(viable_directories)[0])


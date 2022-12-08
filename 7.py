import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/7.txt")]

class Node:
    def __init__(self, dir_name, parent):
        self.dir_name = dir_name
        self.parent = parent
        self.files = {}
        self.dirs = {}

    def get_size(self):
        size = 0
        for key, value in self.files.items():
            size += value
        for dir_name, node in self.dirs.items():
            size += node.get_size()
        return size


home = Node('/', None)
current_node = home
skip = 1 # skip the first line
for index, line in enumerate(lines):
    if skip > 0:
        skip -= 1
        continue
    if line == '$ cd ..':
        current_node = current_node.parent
    elif line[:4] == '$ cd':
        # assume that the node already exists because we can't have cd'ed before we ls'd
        dir = line[5:]
        current_node = current_node.dirs[dir]
    elif line == '$ ls':
        i = index + 1
        next_line = lines[i]
        while next_line[:4] not in ['$ cd', '$ ls']:
            if next_line[0] == 'd':
                dir = next_line[4:]
                current_node.dirs[dir] = Node(dir, current_node)
            else:
                size, name = next_line.split(" ")
                current_node.files[name] = int(size)
            i += 1
            if i == len(lines):
                break
            next_line = lines[i]
            skip += 1

# dfs/ any graph traversal from home to find all nodes with size less than 100k

stack = [home]

size_less_100k = 0
while len(stack) > 0:
    node = stack.pop()
    size = node.get_size()
    if size < 100000:
        size_less_100k += size
    for dir_name, node in node.dirs.items():
        stack.append(node)
print(size_less_100k)

# part 2

total_space = 70000000
free_space = total_space - home.get_size()
threshold = 30000000 - free_space  # we need to delete at least this much

# another dfs to find the node with the smallest size that is greater than the threshold

stack = [home]
size_of_smallest_dir_larger_than_threshold = float('inf')  # lol
while len(stack) > 0:
    node = stack.pop()
    size = node.get_size()
    if threshold < size < size_of_smallest_dir_larger_than_threshold:
        size_of_smallest_dir_larger_than_threshold = size
    for dir_name, node in node.dirs.items():
        stack.append(node)

print(size_of_smallest_dir_larger_than_threshold)

import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/7.txt")]
from functools import lru_cache

# strategy: just make objects and then maybe do some recursion
# problem: i assumed that no two directories would have the same name, which was wrong

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.size} {self.name}"

class Directory:
    def __init__(self, name, files, dirs):
        self.name = name
        self.dirs = dirs
        self.files = files

    def __str__(self):
        output = ""
        for file in self.files:
            output += f"{file.size} {file.name}\n"
        for directory in self.dirs:
            output += f"dir {directory}\n"
        return output

    def get_size(self):
        size = 0
        for file in self.files:
            size += file.size
        for dir in self.dirs:
            size += all_dirs[dir].get_size()
        return size

i = 1
# ok, detect ls' and get the cds from above them.
all_dirs = {}
while i < (len(lines)):
    # at the start of each loop, we should be at a line with $ cd
    line = lines[i]
    if line == '$ ls':
        dir = lines[i-1][5:]
        files = []
        dirs = []
        i += 1
        line = lines[i]
        while line[:4] not in ['$ cd', '$ ls']:
            if line[0] == 'd':  # directory
                dirs.append(line[4:])
            else:
                size, name = line.split(" ")
                files.append(File(name, int(size)))
            i += 1
            if i == len(lines):
                break
            line = lines[i]
        all_dirs[dir] = Directory(dir, files, dirs)
        i -= 1
    i += 1


sizes = {}

for key, value in all_dirs.items():
    print("Directory " + key)
    print(str(value))
    print("")
    sizes[key] = value.get_size()

print(sizes)

total_size_less_than_100k = 0
for key, value in sizes.items():
    print(f"Directory {key} has size {value}")
    if value <= 100000:
        total_size_less_than_100k += value
        print(key)

print(total_size_less_than_100k)





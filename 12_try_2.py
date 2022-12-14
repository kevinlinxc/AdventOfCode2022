# trainwreck part 2
import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/12.txt")]

width = len(lines[0])
height = len(lines)

start_point = None
end_point = None
for y, line in enumerate(lines):
    for x, char in enumerate(line):
       if char == "S":
           start_point = (x, y)
       elif char == "E":
           end_point = (x, y)


def get_neighbours(x, y):
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if x < width - 1:
        neighbours.append((x + 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if y < height - 1:
        neighbours.append((x, y + 1))
    return neighbours


visited = set()


def bfs(start, end):
    queue = []
    queue.append((start, 1))
    visited.add(start)
    while len(queue) > 0:
        node, count = queue.pop(0)
        letter = lines[node[1]][node[0]]
        neighbours = get_neighbours(node[0], node[1])
        for neighbour in neighbours:
            if lines[neighbour[1]][neighbour[0]] == end and letter  in ["z", "y"]:
                return count
        for adjacent in neighbours:
            their_letter = lines[adjacent[1]][adjacent[0]]
            if (ord(their_letter) - ord(letter) <= 1 and adjacent not in visited) or letter == "S":
                visited.add(adjacent)
                queue.append((adjacent, count + 1))

count = bfs(start_point, "E")
print(count)


def bfs2(start, end):
    queue = []
    visited = set()
    queue.append((start, 1))
    visited.add(start)
    while len(queue) > 0:
        node, count = queue.pop(0)
        letter = lines[node[1]][node[0]]
        neighbours = get_neighbours(node[0], node[1])
        for neighbour in neighbours:
            if lines[neighbour[1]][neighbour[0]] == end and letter in ["b"]:
                return count
        for adjacent in neighbours:
            their_letter = lines[adjacent[1]][adjacent[0]]
            if letter == "E":
                if their_letter in ["y", "z"] and adjacent not in visited:
                    visited.add(adjacent)
                    queue.append((adjacent, count + 1))
            else:
                if ord(letter) - ord(their_letter) <= 1 and adjacent not in visited:
                    visited.add(adjacent)
                    queue.append((adjacent, count + 1))

count = bfs2(end_point, "a")
print(count)


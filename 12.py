# trainwreck part 1
import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/12.txt")]

start_point = None
end_point = None
for y, line in enumerate(lines):
    for x, char in enumerate(line):
       if char == "S":
           start_point = (x, y)
       elif char == "E":
           end_point = (x, y)


def get_height(pt):
    return ord(lines[pt[1]][pt[0]])

def get_valid_neighbours(x,y):
    current_letter = lines[y][x]
    if lines[y][x] == "S":
        return [(x, y - 1), (x, y + 1), (x + 1, y)]  # all but left, kind of hardcoded
    current_elevation = get_height((x,y))
    neighbours = []
    if y > 0:
        top = lines[y - 1][x]

        if ord(top) - current_elevation <= 1:
            if (top == "E" and current_letter in ["y", "z"]) or top != "E":
                neighbours.append((x, y - 1))
    if y < len(lines) - 1:
        bottom = lines[y + 1][x]
        if ord(bottom) - current_elevation <= 1:
            if (bottom == "E" and current_letter in ["y", "z"]) or bottom != "E":
                neighbours.append((x, y + 1))
    if x > 0:
        left = lines[y][x - 1]
        if ord(left) - current_elevation <= 1:
            if (left == "E" and current_letter in ["y", "z"]) or left != "E":
                neighbours.append((x - 1, y))
    if x < len(lines[0]) - 1:
        right = lines[y][x + 1]
        if ord(right) - current_elevation <= 1:
            if (right == "E" and current_letter in ["y", "z"]) or right != "E":
                neighbours.append((x + 1, y))

    return neighbours


def get_valid_neighbours2(x,y):
    current_letter = lines[y][x]
    if lines[y][x] == "E":
        return [(x, y - 1), (x + 1, y)]  #right and down fuck it
    current_elevation = get_height((x,y))
    neighbours = []
    if y > 0:
        top = lines[y - 1][x]

        if current_elevation - ord(top) <= 1:
            if (top == "a" and current_letter == "b") or top != "a":
                neighbours.append((x, y - 1))
    if y < len(lines) - 1:
        bottom = lines[y + 1][x]
        if current_elevation - ord(bottom) <= 1:
            if (bottom == "a" and current_letter == "b") or bottom != "a":
                neighbours.append((x, y - 1))
    if x > 0:
        left = lines[y][x - 1]
        if current_elevation - ord(left) <= 1:
            if (left == "a" and current_letter == "b") or left != "a":
                neighbours.append((x - 1, y))
    if x < len(lines[0]) - 1:
        right = lines[y][x + 1]
        if current_elevation - ord(right) <= 1:
            if (right == "a" and current_letter == "b") or right != "a":
                neighbours.append((x + 1, y))

    return neighbours

#
from dijkstar import Graph, find_path
#
#
def build_graph():
    graph = Graph()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            neighbours = get_valid_neighbours(x, y)
            for neighbour in neighbours:
                graph.add_edge((x, y), neighbour, 1)
    return graph

def build_graph2():
    graph = Graph()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            neighbours = get_valid_neighbours2(x, y)
            for neighbour in neighbours:
                graph.add_edge((x, y), neighbour, 1)
    return graph

graph = build_graph()

path = find_path(graph, start_point, end_point)
print(path.nodes)
print(len(path.nodes)-1)

graph2 = build_graph2()
path2 = find_path(graph2, end_point, start_point)
print(path2.nodes)
print(len(path2.nodes)-1)

# def print_path(lines, path):
#     # use < > v ^ to print path, with . for unvisited spots
#     for y, line in enumerate(lines):
#         for x, char in enumerate(line):
#             if (x, y) in path:
#                 if (x, y) == start_point:
#                     print("S", end="")
#                 elif (x, y) == end_point:
#                     print("E", end="")
#                 else:
#                     next = path[path.index((x, y)) + 1]
#                     if next[0] == x:
#                         if next[1] > y:
#                             print("v", end="")
#                         else:
#                             print("^", end="")
#                     else:
#                         if next[0] > x:
#                             print(">", end="")
#                         else:
#                             print("<", end="")
#             else:
#                 print(".", end="")
#         print()
#
# print_path(lines, path.nodes)
# for node in path.nodes:
#     print(lines[node[1]][node[0]], end="")

# from matplotlib import pyplot as plt
#
# x = [x[0] for x in path.nodes]
# y = [-y[1] for y in path.nodes]
#
#
# plt.scatter(x, y)
# plt.show()


# recursive max depth reached
# make breadth first search to find shortest path
# def bfs_helper(start, end):
#     bfs(start, end, [])
#
# def bfs(start, end, path):
#     start_x, start_y = start
#     if lines[start_y][start_x] == end:
#         # shortest path thanks to bfs
#         print(path)
#         print(len(path))
#         return
#     visited.add(start)
#     neighbours = get_valid_neighbours(start_x, start_y)
#     for neighbour in neighbours:
#         if neighbour not in visited:
#             bfs(neighbour, end, path + [neighbour])


# iterative too slow
# heights_reached = set()
# visited = set()
# def bfs(start, end):
#     # maintain a queue of paths
#     queue = []
#     # push the first path into the queue
#     queue.append([start])
#     visited.add(start)
#     while queue:
#         # get the first path from the queue
#         path = queue.pop(0)
#         # get the last node from the path
#         node = path[-1]
#         letter = lines[node[1]][node[0]]
#         # path found
#         if letter == end:
#             return path
#         # enumerate all adjacent nodes, construct a
#         # new path and push it into the queue
#         for adjacent in get_valid_neighbours(*node):
#             if adjacent not in visited:
#                 new_path = list(path)
#
#                 new_path.append(adjacent)
#                 queue.append(new_path)
#                 visited.add(adjacent)
#
# path = bfs(start_point, "E")
# print(path)
# print(len(path)-1)

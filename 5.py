import fileinput
import re

lines = [line.strip() for line in fileinput.input(files="inputs/5.txt")]

#     [V] [G]             [H]
# [Z] [H] [Z]         [T] [S]
# [P] [D] [F]         [B] [V] [Q]
# [B] [M] [V] [N]     [F] [D] [N]
# [Q] [Q] [D] [F]     [Z] [Z] [P] [M]
# [M] [Z] [R] [D] [Q] [V] [T] [F] [R]
# [D] [L] [H] [G] [F] [Q] [M] [G] [W]
# [N] [C] [Q] [H] [N] [D] [Q] [M] [B]
#  1   2   3   4   5   6   7   8   9

stack = {
    1: list("NDMQBPZ"),
    2: list("CLZQMDHV"),
    3: list("QHRDVFZG"),
    4: list("HGDFN"),
    5: list("NFQ"),
    6: list("DQVZFBT"),
    7: list("QMTZDVSH"),
    8: list("MGFPNQ"),
    9: list("BWRM"),
}

stack_2 = {
    1: list("NDMQBPZ"),
    2: list("CLZQMDHV"),
    3: list("QHRDVFZG"),
    4: list("HGDFN"),
    5: list("NFQ"),
    6: list("DQVZFBT"),
    7: list("QMTZDVSH"),
    8: list("MGFPNQ"),
    9: list("BWRM"),
}


def pretty_print(stack):
    for key, value in stack.items():
        print(f"{key}: {''.join(value)}")


def move(stack, from_: int, to_: int):
    stack[to_].append(stack[from_].pop())


def move2(stack_, quantity, from_: int, to_: int):
    removed = []
    for i in range(quantity):
        removed.append(stack_[from_].pop())
    removed = reversed(removed)
    for item in removed:
        stack_[to_].append(item)


for line in lines:
    # pretty_print(stack)
    # print(line)
    regex = r"move ([0-9]+) from ([0-9]+) to ([0-9])"
    match = re.match(regex, line)
    quantity, from_, to_ = [int(x) for x in match.groups()]
    for _ in range(quantity):
        move(stack, from_, to_)

end_str = ""
for key, value in stack.items():
    end_str += value[-1]

print(end_str)
# QGTHFZBHV
print("part 2")

# part 2
for line in lines:
    pretty_print(stack_2)
    print(line)
    regex = r"move ([0-9]+) from ([0-9]+) to ([0-9])"
    match = re.match(regex, line)
    quantity, from_, to_ = [int(x) for x in match.groups()]
    move2(stack_2, quantity, from_, to_)

end_str2 = ""
for key, value in stack_2.items():
    end_str2 += value[-1]

print(end_str2)
# MGDMPSZTM

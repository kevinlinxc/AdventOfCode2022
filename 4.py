import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/4.txt")]


def contains(ll, lr, rl, rr):
    if rl >= ll and rr <= lr:
        return 1
    elif rl <= ll and rr >= lr:
        return 1
    return 0


def overlaps(ll, lr, rl, rr):
    if rl >= ll and rl <= lr:
        return 1
    elif rr >= ll and rr <= lr:
        return 1
    elif contains(ll, lr, rl, rr):
        return 1
    return 0


count = 0

for line in lines:
    left_range, right_range = line.split(",")
    ll, lr = left_range.split("-")
    rl, rr = right_range.split("-")
    count += contains(int(ll), int(lr), int(rl), int(rr))

print(count)
# 475

count2 = 0
for line in lines:
    left_range, right_range = line.split(",")
    ll, lr = left_range.split("-")
    rl, rr = right_range.split("-")
    count2 += overlaps(int(ll), int(lr), int(rl), int(rr))

print(count2)
# 825

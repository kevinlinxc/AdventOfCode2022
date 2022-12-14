import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/13.txt")]

# left side should have fewer items, or lower number first, or

def is_correct_order(left, right, depth=0):
    for i in range(depth):
        print("\t", end="")
    print(f"- {left} vs {right}")
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        return left < right
    elif type(left) == int and type(right) == list:
        return is_correct_order([left], right, depth + 1)
    elif type(left) == list and type(right) == int:
        return is_correct_order(left, [right], depth + 1)
    # both are lists
    for i in range(max(len(left), len(right))):  # go for the longest, see if theres any out of bounds errors
        try:
            left_item = left[i]
        except IndexError:
            return True
        try:
            right_item = right[i]
        except IndexError:
            return False
        result = is_correct_order(left_item, right_item, depth + 1)
        if result is None:
            continue
        else:
            return result

def is_correct_order_comparator(left, right, depth=0):
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        return -1 if left < right else 1
    elif type(left) == int and type(right) == list:
        return is_correct_order_comparator([left], right, depth + 1)
    elif type(left) == list and type(right) == int:
        return is_correct_order_comparator(left, [right], depth + 1)
    # both are lists
    for i in range(max(len(left), len(right))):  # go for the longest, see if theres any out of bounds errors
        try:
            left_item = left[i]
        except IndexError:
            return -1
        try:
            right_item = right[i]
        except IndexError:
            return 1
        result = is_correct_order_comparator(left_item, right_item, depth + 1)
        if result is None:
            continue
        else:
            return result
def part1():


    indices = 0
    packet_count = 0
    for i in range(0, len(lines), 3):
        packet_count += 1
        first_line = eval(lines[i])
        second_line = eval(lines[i+1])
        if is_correct_order(first_line, second_line):
            indices += packet_count
            print(f"correct order for index {packet_count}")
    print(indices)

part1()
# 6395

def part2():
    packets = []
    import functools
    for i in range(0, len(lines), 3):
        packets.append((eval(lines[i])))
        packets.append((eval(lines[i+1])))
    packets.append([[2]])
    packets.append([[6]])
    print(f"before sorting: {packets}")
    sorted_packets = sorted(packets, key=functools.cmp_to_key(is_correct_order_comparator))
    print(f"after sorting: {sorted_packets}")
    first_index = sorted_packets.index([[2]]) + 1
    second_index = sorted_packets.index([[6]]) + 1
    print(first_index, second_index)
    print(first_index * second_index)

part2()
# 24921
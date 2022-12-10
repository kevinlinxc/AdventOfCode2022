import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/9.txt")]


def move(old_position, direction):
    x, y = old_position
    if direction == 'U':
        return x, y + 1
    elif direction == 'D':
        return x, y - 1
    elif direction == 'R':
        return x + 1, y
    elif direction == 'L':
        return x - 1, y


def part1():
    # part 1

    head_pos = (0, 0)
    tail_pos = (0, 0)

    visited = set()

    for line in lines:

        direc, amt = line.split(' ')
        amt = int(amt)
        for i in range(amt):
            # print(f"head: {head_pos}, tail: {tail_pos}, moving {direc}")
            visited.add(tail_pos)
            x_dist = head_pos[0] - tail_pos[0]
            y_dist = head_pos[1] - tail_pos[1]
            # detect diagonals, if the direction is in pull direction, then tail takes head position
            pull = set()
            if (x_dist, y_dist) == (1, 1):
                pull = {'U', 'R'}
            elif (x_dist, y_dist) == (1, -1):
                pull = {'D', 'R'}
            elif (x_dist, y_dist) == (-1, 1):
                pull = {'U', 'L'}
            elif (x_dist, y_dist) == (-1, -1):
                pull = {'D', 'L'}

            if direc in pull:
                tail_pos = head_pos
                head_pos = move(head_pos, direc)
                continue
            # not a diagonal pull, so head moves and we check if tail needs to move
            head_pos = move(head_pos, direc)
            if head_pos[0] - tail_pos[0] > 1:
                tail_pos = (tail_pos[0] + 1, tail_pos[1])
            elif head_pos[0] - tail_pos[0] < -1:
                tail_pos = (tail_pos[0] - 1, tail_pos[1])
            elif head_pos[1] - tail_pos[1] > 1:
                tail_pos = (tail_pos[0], tail_pos[1] + 1)
            elif head_pos[1] - tail_pos[1] < -1:
                tail_pos = (tail_pos[0], tail_pos[1] - 1)
    print(len(visited))


part1()
# 6098


def part2():
    move_diffs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    next_to_diffs = move_diffs[:4]

    def where_to_move(parent_pos, child_pos):
        # uses set union to figure out where child should move to be next to parent. Prioritizes
        # moving directly next to parent, but will do diagonal if it can't
        # if the parent is still in the 9 blocks near to the child, return None to signify that nothing else moves
        if parent_pos == child_pos:
            return None
        child_close_zone = set()
        for move_diff in move_diffs:
            child_close_zone.add((child_pos[0] + move_diff[0], child_pos[1] + move_diff[1]))
        if parent_pos in child_close_zone:
            return None
        # since were not close to child, we know the child will move to be near the parent
        # check if we can move directly next to parent
        next_to_parent = set()
        for move_diff in next_to_diffs:
            next_to_parent.add((parent_pos[0] + move_diff[0], parent_pos[1] + move_diff[1]))
        try:
            new_position = next_to_parent.intersection(child_close_zone).pop()
        except KeyError:
            # if we can't, then the parent was diagonal, and now it moved diagonally, find intersection of diagonals to
            # find where child should move
            parent_diagonals = set()
            for move_diff in move_diffs[4:]:
                parent_diagonals.add((parent_pos[0] + move_diff[0], parent_pos[1] + move_diff[1]))
            new_position = parent_diagonals.intersection(child_close_zone).pop()
        return new_position

    positions = {0: (0, 0), 1: (0, 0), 2: (0, 0), 3: (0, 0), 4: (0, 0), 5: (0, 0), 6: (0, 0), 7: (0, 0), 8: (0, 0),
                 9: (0, 0)}
    visited = set()

    for line in lines:
        direc, amt = line.split(' ')
        amt = int(amt)
        for i in range(amt):
            # print(positions)
            # print(direc)
            # print("\n")
            visited.add(positions[9])
            positions[0] = move(positions[0], direc)
            parent_location = positions[0]
            for i in range(1, 10):
                child_location = positions[i]
                new_child_location = where_to_move(parent_location, child_location)
                if new_child_location is None:
                    break
                else:
                    positions[i] = new_child_location
                    parent_location = new_child_location

    print(len(visited))


part2()
# 2597
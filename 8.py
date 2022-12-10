# looking at trees in a forest, seeing how many are visible form each side
import fileinput

from collections import defaultdict
lines = [line.strip() for line in fileinput.input(files="inputs/8.txt")]

# part 1
width = len(lines[0])
height = len(lines)
print(width, height)

visible = defaultdict(list)
# maybe an O(n) solution?

for y, line in enumerate(lines):
    # look from the left, any max is visible, add to set
    max_in_line = float('-inf')
    for x, char in enumerate(line):
        if int(char) > max_in_line:
            max_in_line = int(char)
            visible[(x, y)].append('left')

    # look from the right, any max is visible, add to set
    max_in_line = float('-inf')
    for x, char in enumerate(line[::-1]):
        if int(char) > max_in_line:
            max_in_line = int(char)
            visible[(width - x - 1, y)].append('right')

for x in range(width):
    # look from the top, any max is visible, add to set
    max_in_line = float('-inf')
    for y, line in enumerate(lines):
        if int(line[x]) > max_in_line:
            max_in_line = int(line[x])
            visible[(x, y)].append('top')

    # look from the bottom, any max is visible, add to set
    max_in_line = float('-inf')
    for y, line in enumerate(lines[::-1]):
        if int(line[x]) > max_in_line:
            max_in_line = int(line[x])
            visible[(x, height - y - 1)].append('bottom')

print(len(visible.items()))
# 1779
# part 2

max_scenic_score = float('-inf')
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        cur_height = int(char)
        visible_left = 0
        visible_right = 0
        visible_top = 0
        visible_bottom = 0
        left = x
        while left > 0:
            left -= 1
            if int(lines[y][left]) < cur_height:
                visible_left += 1
            else:
                visible_left += 1
                break

        right = x
        while right < width - 1:
            right += 1
            if int(lines[y][right]) < cur_height:
                visible_right += 1
            else:
                visible_right += 1
                break
        top = y
        while top > 0:
            top -= 1
            if int(lines[top][x]) < cur_height:
                visible_top += 1
            else:
                visible_top += 1
                break
        bottom = y
        while bottom < height - 1:
            bottom += 1
            if int(lines[bottom][x]) < cur_height:
                visible_bottom += 1
            else:
                visible_bottom += 1
                break
        scenic_score = visible_left * visible_right * visible_top * visible_bottom
        max_scenic_score = max(max_scenic_score, scenic_score)
print(max_scenic_score)
# 172224

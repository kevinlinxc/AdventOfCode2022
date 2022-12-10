# real easy, just a sliding window with a deque
import fileinput
lines = [line.strip() for line in fileinput.input(files="inputs/6.txt")]
from collections import deque


line = lines[0]
contained = []
my_d = deque()
i = 0
for i in range(3):
    my_d.append(line[i])

for index, char in enumerate(line[3:]):
    print(f"Looking at {char}")
    my_d.append(char)
    if len(set(list(my_d))) == 4:
        print("good: " + "".join(list(my_d)))
        print(index + 3 + 1)
        break
    else:
        print("bad: " + "".join(list(my_d)))
        my_d.popleft()
# 1855

# part 2, no optimization needed, just do the same thing
my_d2 = deque()

for i in range(13):
    my_d2.append(line[i])

for index, char in enumerate(line[14:]):
    print(f"Looking at {char}")
    my_d2.append(char)
    if len(set(list(my_d2))) == 14:
        print("good: " + "".join(list(my_d2)))
        print(index + 14 + 1)
        break
    else:
        print("bad: " + "".join(list(my_d2)))
        my_d2.popleft()

# 3256

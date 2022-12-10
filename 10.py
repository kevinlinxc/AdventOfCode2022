import fileinput

import matplotlib.pyplot as plt
lines = [line.strip() for line in fileinput.input(files="inputs/10.txt")]


def part1():
    register = 1
    cycle = 0
    signal_strength = 0
    for line in lines:
        # print("cycle: " + str(cycle), "register: " + str(register))
        if line == "noop":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += cycle * register
        else:
            _, amt = line.split(" ")
            amt = int(amt)
            for i in range(2):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    signal_strength += cycle * register
            register += amt

    print(signal_strength)


part1()


# 12980


# part 2

def part2():
    screen_lit_up = []

    def draw(cycle, register):
        return cycle in [register - 1, register, register + 1]

    register = 1
    line_num = 5
    cycle = 0
    for line in lines:

        # print("cycle: " + str(cycle), "register: " + str(register))
        if line == "noop":
            if draw(cycle, register):
                screen_lit_up.append((cycle, line_num))
            cycle += 1
            if cycle == 40:
                cycle = 0
                line_num -= 1
        else:
            _, amt = line.split(" ")
            amt = int(amt)
            for i in range(2):
                if draw(cycle, register):
                    screen_lit_up.append((cycle, line_num))
                cycle += 1
                if cycle == 40:
                    cycle = 0
                    line_num -= 1
            register += amt
    return screen_lit_up


screen = part2()

print(screen)
x = [x[0] for x in screen]
y = [y[1] for y in screen]


plt.scatter(x, y)
plt.show()
# expand matplotlib show window horizontally
# BRJLFULP

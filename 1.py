import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/1.txt")]

# part 1
max_cal = 0
current = 0
for index, line in enumerate(lines):
    if line == '' or index == len(lines)-1:
        max_cal = max(current, max_cal)
        current = 0
    else:
        current += int(line)

print(max_cal)


# part 2
counts = []
current = 0
for index, line in enumerate(lines):
    if line == '' or index == len(lines)-1:
        counts.append(current)
        current = 0
    else:
        current += int(line)
counts.append(current)

print(sum(sorted(counts, reverse=True)[0:3]))

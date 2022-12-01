import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/1.txt")]
print(lines)

max_cal = 0
current = 0

for line in lines:
    # todo don't ignore last line
    if line == '':
        max_cal = max(current, max_cal)
        current = 0
    else:
        current += int(line)


print(max_cal)

counts = []
current = 0
for line in lines:
    if line == '':
        counts.append(current)
        current = 0
    else:
        current += int(line)
counts.append(current)

print(sorted(counts, reverse=True))
print(sum(sorted(counts, reverse=True)[0:3]))
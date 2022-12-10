import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/3.txt")]


def letter_in_common(str1, str2):
    for letter in str1:
        if letter in str2:
            return letter


# part 1
prio = 0


def priority(letter):
    # a-z = 1-26, A=Z = 27-52
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


for line in lines:
    length = len(line)
    first_half, second_half = line[:length // 2], line[length // 2:]
    prio += priority(letter_in_common(first_half, second_half))
print(prio)
# 7795

# part 2
prio2 = 0
for index in range(0, len(lines), 3):
    first = lines[index]
    second = lines[index + 1]
    third = lines[index + 2]
    for letter in first:
        if letter in second and letter in third:
            prio2 += priority(letter)
            break

print(prio2)
# 2703

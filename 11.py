import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/11.txt")]


class Monkey:
    def __init__(self, items, operation, divisible, if_true, if_false):
        self.items = items
        self.operation = operation
        self.test = lambda x: if_true if x % divisible == 0 else if_false
        self.inspected_count = 0


def part1():
    Monkey0 = Monkey([97, 81, 57, 57, 91, 61], lambda x: x * 7, 11, 5, 6)
    Monkey1 = Monkey([88, 62, 68, 90], lambda x: x * 17, 19, 4, 2)
    Monkey2 = Monkey([74, 87], lambda x: x + 2, 5, 7, 4)
    Monkey3 = Monkey([53, 81, 60, 87, 90, 99, 75], lambda x: x + 1, 2, 2, 1)
    Monkey4 = Monkey([57], lambda x: x + 6, 13, 7, 0)
    Monkey5 = Monkey([54, 84, 91, 55, 59, 72, 75, 70], lambda x: x * x, 7, 6, 3)
    Monkey6 = Monkey([95, 79, 79, 68, 78], lambda x: x + 3, 3, 1, 3)
    Monkey7 = Monkey([61, 97, 67], lambda x: x + 4, 17, 0, 5)

    monkeys = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]

    # part 1

    for i in range(20):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                worry = monkey.items.pop(0)
                worry = monkey.operation(worry)
                worry = worry // 3
                monkeys[monkey.test(worry)].items.append(worry)
                monkey.inspected_count += 1

    activity = [monkey.inspected_count for monkey in monkeys]
    sorted_activity = list(reversed(sorted(activity)))
    print(sorted_activity[0] * sorted_activity[1])

# part1()


def part2():
    Monkey0 = Monkey([97, 81, 57, 57, 91, 61], lambda x: x * 7, 11, 5, 6)
    Monkey1 = Monkey([88, 62, 68, 90], lambda x: x * 17, 19, 4, 2)
    Monkey2 = Monkey([74, 87], lambda x: x + 2, 5, 7, 4)
    Monkey3 = Monkey([53, 81, 60, 87, 90, 99, 75], lambda x: x + 1, 2, 2, 1)
    Monkey4 = Monkey([57], lambda x: x + 6, 13, 7, 0)
    Monkey5 = Monkey([54, 84, 91, 55, 59, 72, 75, 70], lambda x: x * x, 7, 6, 3)
    Monkey6 = Monkey([95, 79, 79, 68, 78], lambda x: x + 3, 3, 1, 3)
    Monkey7 = Monkey([61, 97, 67], lambda x: x + 4, 17, 0, 5)

    monkeys = [Monkey0, Monkey1, Monkey2, Monkey3, Monkey4, Monkey5, Monkey6, Monkey7]

    # part 1

    for i in range(10000):
        if i % 100 == 0:
            print(i, flush=True)
        for monkey in monkeys:
            while len(monkey.items) > 0:
                worry = monkey.items.pop(0)
                worry = monkey.operation(worry)
                worry = worry % 9699690
                monkeys[monkey.test(worry)].items.append(worry)
                monkey.inspected_count += 1

    activity = [monkey.inspected_count for monkey in monkeys]
    sorted_activity = list(reversed(sorted(activity)))
    print(sorted_activity[0] * sorted_activity[1])


part2()

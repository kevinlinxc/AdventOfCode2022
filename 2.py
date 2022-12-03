import fileinput

lines = [line.strip() for line in fileinput.input(files="inputs/2.txt")]

abc_dict = {
    "A": "Rock",
    "B": "Paper",
    "C": "Scissors",
}

xyz_dict = {
    "X": "Rock",
    "Y": "Paper",
    "Z": "Scissors",
}

beats_dict = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper",
}

loses_dict = {
    "Rock": "Paper",
    "Paper": "Scissors",
    "Scissors": "Rock",
}

score_dict = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3,
}


def score_for_round(them, me):
    score = score_dict[me]
    if me == them:
        return 3 + score
    elif beats_dict[me] == them:
        return 6 + score
    else:
        return score


def score_for_round_p2(them, xyz):
    if xyz == "X":
        me = beats_dict[them]
    elif xyz == "Y":
        me = them
    else:
        me = loses_dict[them]
    return score_for_round(them, me)


if __name__ == "__main__":
    # part 1
    total_score = 0
    for line in lines:
        abc, xyz = line.split()
        them = abc_dict[abc]
        me = xyz_dict[xyz]
        total_score += score_for_round(them, me)

    print(total_score)

    total_score = 0
    for line in lines:
        abc, xyz = line.split()
        them = abc_dict[abc]
        total_score += score_for_round_p2(them, xyz)
    print(total_score)

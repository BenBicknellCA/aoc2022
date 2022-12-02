with open("input.txt") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))


def get_score():
    score = 0
    opp_rock = "A"
    opp_paper = "B"
    rock = "X"
    paper = "Y"
    win = 6
    tie = 3
    lose = 0
    for i in lines:
        pair = i.split(" ")
        opp = pair[0]
        you = pair[1]
        if you == rock:
            score += 1
            if opp == opp_rock:
                score += tie
            elif opp == opp_paper:
                score += lose
            else:
                score += win
        elif you == paper:
            score += 2
            if opp == opp_rock:
                score += win
            elif opp == opp_paper:
                score += tie
            else:
                score += lose
        else:
            score += 3
            if opp == opp_rock:
                score += lose
            elif opp == opp_paper:
                score += win
            else:
                score += tie
    return score


print(get_score())

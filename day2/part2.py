from part1 import get_pairs


def part_2():
    lines = get_pairs()
    score = 0
    opp_rock = "A"
    opp_paper = "B"
    win_score = 6
    tie_score = 3
    lose_score = 0
    for i in lines:
        pair = i.split(" ")
        opp = pair[0]
        you = pair[1]
        if you == "X":
            if opp == opp_rock:
                score += +3 + lose_score
            elif opp == opp_paper:
                score += +1 + lose_score
            else:
                score += +2 + lose_score
        elif you == "Y":
            if opp == opp_rock:
                score += +1 + tie_score
            elif opp == opp_paper:
                score += +2 + tie_score
            else:
                score += +3 + tie_score
        else:
            if you == "Z":
                if opp == opp_rock:
                    score += +2 + win_score
                elif opp == opp_paper:
                    score += +3 + win_score
                else:
                    score += +1 + win_score
    return score

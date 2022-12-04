from part1 import get_pairs


def get_groups():
    data = get_pairs()
    temp = []
    group = []
    for r, sack in enumerate(data, 1):
        temp.append(sack)
        if r % 3 == 0:
            group.append(temp)
            temp = []
    return group


def main():
    groups = get_groups()
    total_value = 0
    lower_dict = {chr(n): n - 96 for n in range(ord("a"), ord("z") + 1)}
    upper_dict = {chr(n): n - 38 for n in range(ord("A"), ord("Z") + 1)}
    lower_upper = upper_dict | lower_dict
    for group in groups:
        for key, value in lower_upper.items():
            if key in group[0] and key in group[1] and key in group[2]:
                total_value += value
    return value

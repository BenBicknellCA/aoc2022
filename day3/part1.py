def get_pairs():
    with open("input.txt") as f:
        lines = list(map(lambda x: x.strip(), f.readlines()))
        return lines


def get_comparts():
    input = get_pairs()
    total_value = 0
    lower_dict = {chr(n): n - 96 for n in range(ord("a"), ord("z") + 1)}
    upper_dict = {chr(n): n - 38 for n in range(ord("A"), ord("Z") + 1)}
    lower_upper = upper_dict | lower_dict
    for i in input:
        compart_1, compart_2 = i[: len(i) // 2], i[len(i) // 2 :]
        print(compart_1, compart_2)

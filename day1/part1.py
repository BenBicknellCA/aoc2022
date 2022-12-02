with open("input.txt") as f:
    lines = f.readlines()


def get_most_cals():
    lines_no_newline = list(map(lambda x: x.strip(), lines))
    temp = []
    array_group = []
    max_group = []
    for i in lines_no_newline:
        if not i == "":
            num = int(i)
            temp.append(num)
        else:
            array_group.append(temp)
            temp = []
    for array in array_group:
        max_group.append(sum(array))
        max_group.sort()
    return max_group

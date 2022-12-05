def get_input():
    with open("input.txt") as f:
        lines = [list(map(lambda x: x.strip().split(","), f.readlines()))]

        return lines


def main():
    total = 0
    data = get_input()
    for n in data:
        for pair in n:
            for str1, str2 in zip(pair[1::], pair[::1]):
                elf_str = str1.split("-") + str2.split("-")
            for elf1, elf2, elf3, elf4 in zip(
                (elf_str[::4]),
                (elf_str[1::4]),
                (elf_str[2::4]),
                (elf_str[3::4]),
            ):
                group1 = set(range(int(elf1), int(elf2) + 1))
                group2 = set(range(int(elf3), int(elf4) + 1))

            if group1.issubset(group2) or group2.issubset(group1):
                total += 1

    # if group1 in group2 or group2 in group1:
    #     total += 1
    print(total)

    # if group[0] > group[2] and group[1] > group[3]:
    #     total += 1
    # elif group[2] > group[0] and group[3] > group[1]:
    #     total += 1
    # print(group)
    # print(total)


main()

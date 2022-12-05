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
                if int(elf2) >= int(elf3) and int(elf4) >= int(elf1):
                    total += 1
        print(total)


main()

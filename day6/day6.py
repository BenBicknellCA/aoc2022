input_data = open("input.txt", "r")
line = input_data.readline().strip("\n")
input_data.close()


def func(seq, n):
    signal = ["".join(char) for char in zip(*[seq[n:] for n in range(n)])]
    for count, i in enumerate(signal, 4):
        if len(set(i)) == 4:
            return count, i


print(func(line, 4))

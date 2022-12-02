from part1 import get_most_cals


def top_three_cals():
    array_of_sums = get_most_cals()
    top_three_sum = sum(array_of_sums[-3:])
    print(top_three_sum)
    return


top_three_cals()

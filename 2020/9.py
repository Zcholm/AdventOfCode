#!/usr/bin/python3

def get_data(s):
    with open(s) as f:
        return [int(line.strip()) for line in f.readlines()]


def is_sum_of_two(values, val):
    for i in range(len(values) - 1):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == val:
                return True
    return False


def get_weakness(data, preamble):
    for i in range (preamble, len(data)):
        if not is_sum_of_two(data[i - preamble : i], data[i]):
            return [i, data[i]]


def find_contigous_set(data, preamble):
    [idx, val] = get_weakness(data, preamble)

    for i in range(get_weakness(data, preamble)[0]):
        j = i + 1
        while sum(data[i : j]) < val and j <= len(data):
            j += 1
        if (sum(data[i : j]) == val):
            return (min(data[i : j]) + max(data[i : j]))


def main():
    print("Answer to example 1: {0}".format(get_weakness(get_data("9_test_data.txt"), 5)[1]))
    print("Answer to part 1: {0}".format(get_weakness(get_data("9_data.txt"), 25)[1]))
    print("Answer to example 2: {0}".format(find_contigous_set(get_data("9_test_data.txt"), 5)))
    print("Answer to part 2: {0}".format(find_contigous_set(get_data("9_data.txt"), 25)))


if __name__ == "__main__":
    main()

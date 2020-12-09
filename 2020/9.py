#!/usr/bin/python3

def get_data(s):
    data = []
    with open(s) as f:
       for line in f.readlines():
           data.append(int(line.strip()))
    return data


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
        j = i
        cumsum = data[i]
        tested = [cumsum]
        while cumsum < val and j < len(data):
            j += 1
            cumsum += data[j]
            tested.append(data[j])
        if cumsum == data[idx]:
            return (min(tested) + max(tested))


def main():
    print("Answer to example 1: {0}".format(get_weakness(get_data("9_test_data.txt"), 5)[1]))
    print("Answer to part 1: {0}".format(get_weakness(get_data("9_data.txt"), 25)[1]))
    print("Answer to example 2: {0}".format(find_contigous_set(get_data("9_test_data.txt"), 5)))
    print("Answer to part 2: {0}".format(find_contigous_set(get_data("9_data.txt"), 25)))


if __name__ == "__main__":
    main()

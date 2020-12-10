#!/usr/bin/python3

def get_data(s):
    with open(s) as f:
        return [int(line.strip()) for line in f.readlines()]


def get_differences(data):
    data.append(0)
    data.append(max(data) + 3)
    data.sort()
    differences = []
    for i in range(len(data) - 1):
        differences.append(data[i+1] - data[i])

    return (differences)


def get_number_of_differences(data):
    diff_1 = diff_3 = 0
    for diff in get_differences(data):
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1
        else:
            print("Get your data straight")
            exit()
    return diff_1 * diff_3


def get_combinations(data):
    diffs = get_differences(data)
    combinations = 1
    cons = 0
    for diff in diffs:
        if diff == 3:
            # When we find a three, the previous consecutive run of ones is over.
            # Multibly all combinations of previous set of ones, see comment at bottom:
            if cons == 0 or cons == 1:
                pass
            elif cons == 2:
                combinations *= 2
            elif cons == 3:
                combinations *= 4
            elif cons == 4:
                combinations *= 7
            elif cons == 5:
                combinations *= 13
            elif cons == 6:
                combinations *= 24
            else:
                print("You need to get a life")
                exit()

            cons = 0

        elif diff == 1:
            cons += 1
        else:
            print("Get your data straight")
            exit()

    return combinations



def main():
    print("Answer to example 1: {0}".format(get_number_of_differences(get_data("10_test_data_1.txt"))))
    print("Answer to example 2: {0}".format(get_number_of_differences(get_data("10_test_data_2.txt"))))
    print("Answer to example 3: {0}".format(get_combinations(get_data("10_test_data_1.txt"))))
    print("Answer to example 4: {0}".format(get_combinations(get_data("10_test_data_2.txt"))))
    print()
    print("Answer to part 1: {0}".format(get_number_of_differences(get_data("10_data.txt"))))
    print("Answer to part 2: {0}".format(get_combinations(get_data("10_data.txt"))))


if __name__ == "__main__":
    main()

# Yes, I am leaving this in here:

# From example data:   ..., 45, 46, 47, 48, 49, 52
# Differences to previous:  3 , 1 , 1 , 1 , 1 , 3

# From this rules for "ones" can be made:
# "ones" are 46, 47, 48, 49. The first one can be removed, but the last cannot.
# So we have 3 ones that can be removed.
# You cannot remove more than two consecutive ones.

# A series of four "ones" have the following valid configurations, which is 7.
# 1, 1, 1, 1
# x, 1, 1, 1
# 1, x, 1, 1
# 1, 1, x, 1
# x, x, 1, 1
# x, 1, x, 1
# 1, x, x, 1

# A series of three ones have four valid configs:
# 1, 1, 1
# x, 1, 1
# 1, x, 1
# x, x, 1

# A series of two ones have two valid configs:
# 1, 1
# x, 1

# A series of five ones:
# 1, 1, 1, 1, 1
# 1, x, 1, 1, 1
# 1, 1, x, 1, 1
# 1, 1, 1, x, 1
# 1, x, x, 1, 1
# 1, x, 1, x, 1
# 1, 1, x, x, 1
# x, 1, 1, 1, 1
# x, x, 1, 1, 1
# x, 1, x, 1, 1
# x, 1, 1, x, 1
# x, x, 1, x, 1
# x, 1, x, x, 1

# So a five has 7 + 6 = 13 valid configs.


# A series of 6: = 13 + 11 = 24
# 1, 1, 1, 1, 1, 1
# 1, 1, x, 1, 1, 1
# 1, 1, 1, x, 1, 1
# 1, 1, 1, 1, x, 1
# 1, 1, x, x, 1, 1
# 1, 1, x, 1, x, 1
# 1, 1, 1, x, x, 1
# 1, x, 1, 1, 1, 1
# 1, x, x, 1, 1, 1
# 1, x, 1, x, 1, 1
# 1, x, 1, 1, x, 1
# 1, x, x, 1, x, 1
# 1, x, 1, x, x, 1
# x, 1, 1, 1, 1, 1
# x, 1, x, 1, 1, 1
# x, 1, 1, x, 1, 1
# x, 1, 1, 1, x, 1
# x, 1, x, x, 1, 1
# x, 1, x, 1, x, 1
# x, 1, 1, x, x, 1
# x, x, 1, 1, 1, 1
# x, x, 1, x, 1, 1
# x, x, 1, 1, x, 1
# x, x, 1, x, x, 1


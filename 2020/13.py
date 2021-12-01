#!/usr/bin/python3
from time import sleep

def get_data(s):
    d = []
    with open(s) as f:
        lines = f.readlines()
        return [int(lines[0]), [line for line in lines[1].split(",")]]

def part_1(data):
    [t, buses] = data

    while True:
        for bus in buses:
            try:
                if t % int(bus) == 0:
                    return (t - data[0]) * int(bus)
            except:
                pass
        t += 1


def part_2(data):
    print(data)
    return 0


def main():
    print("Answer to ex 1:   {0}".format(part_1(get_data("13_test_data.txt"))))
    print("Answer to ex 2:   {0}".format(part_2(get_data("13_test_data.txt"))))

    print("Answer to part 1: {0}".format(part_1(get_data("13_data.txt"))))
    print("Answer to part 2: {0}".format(part_2(get_data("13_data.txt"))))


if __name__ == "__main__":
    main()


#!/usr/bin/python3
import re
#2: >6269, <10000

def get_data():
    data = []
    with open("7_data.txt") as f:
       i = 0
       for line in f.readlines():
           data.append(line.strip())
    return data


def get_line(color, data):
    for line in data:
        if line.startswith(color):
            return line
    print("No line starts with " + color)
    exit()


def get_colors_and_number(line):
    words = line.split(' ')
    n = int((len(words) / 4) - 1)
    colors = []
    for i in range(n):
        colors.append([int(words[4 + 4 * i]), words[5 + 4 * i] + ' ' + words[6 + 4 * i]])
    return colors


def can_contain_gold(line, data):
    if re.match(".*no other bags.*", line):
        return False

    colors = get_colors_and_number(line)

    for num, c in colors:
        if c == "shiny gold":
            return True
        else:
            if can_contain_gold(get_line(c, data), data):
                return True
    return False


def number_of_children(color, data):
    line = get_line(color, data)

    if re.match(".*no other bags.*", line):
        return 0

    total = 0

    colors = get_colors_and_number(line)
    for num, c in colors:
        total += num * (1 + number_of_children(c, data))

    return total


def main():
    data = get_data()

    count = 0
    for line in data:
        if can_contain_gold(line, data):
            count += 1

    print(count)
    print(number_of_children("shiny gold", data))


if __name__ == "__main__":
    main()


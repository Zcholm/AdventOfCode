#!/usr/bin/python3

def get_data(s):
    with open(s) as f:
        return [line.strip() for line in f.readlines()]


def get_adjacent_occ (data, x, y):
    x_range = range(max(0, x - 1), min(len(data[0]), x + 2))
    y_range = range(max(0, y - 1), min(len(data), y + 2))
    occ = 0

    for i in x_range:
        for j in y_range:
            if i == x and j == y:
                continue
            elif data[j][i] == '#':
                occ += 1
    return occ

def is_chair(c):
    return c == "#" or c == "L"

def is_occupied(c):
    return c == "#"


def find_chair(data, x, y, dx, dy):
    x += dx
    y += dy
    while x >= 0 and x < len(data[0]) and y >= 0 and y < len(data):
        if is_chair(data[y][x]):
            if is_occupied(data[y][x]):
                return 1
            else:
                return 0
        x += dx
        y += dy
    return 0


def get_seen_occ(data, x, y):
    seen_occ = 0

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            seen_occ += find_chair(data, x, y, dx, dy)
    return seen_occ


def number_of_occ(data):
    occ = 0
    for line in data:
        for seat in line:
            if seat == "#":
                occ += 1
    return occ


def fill_seats (data, part):
    changed = True
    while changed:
        changed = False
        new_data = data.copy()
        for y, line in enumerate(new_data):
            for x, seat in enumerate(line):
                if part == 1:
                    adj = get_adjacent_occ(data, x, y)
                    limit = 4
                if part == 2:
                    adj = get_seen_occ(data, x, y)
                    limit = 5

                if adj >= limit and data[y][x] == "#":
                    new_data[y] = new_data[y][0:x] + "L" + new_data[y][x+1:]
                    changed = True
                elif adj == 0 and data[y][x] == "L":
                    new_data[y] = new_data[y][0:x] + "#" + new_data[y][x+1:]
                    changed = True
        data = new_data.copy()
    return number_of_occ(new_data)



def main():
    print("Answer to ex 1:   {0}".format(fill_seats(get_data("11_test_data.txt"), 1)))
    print("Answer to part 1: {0}".format(fill_seats(get_data("11_data.txt"), 1)))
    print("Answer to ex 2:   {0}".format(fill_seats(get_data("11_test_data.txt"), 2)))
    print("Answer to part 2: {0}".format(fill_seats(get_data("11_data.txt"), 2)))


if __name__ == "__main__":
    main()


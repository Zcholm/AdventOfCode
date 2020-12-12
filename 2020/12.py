#!/usr/bin/python3
import numpy as np

def get_data(s):
    with open(s) as f:
        return [line.strip() for line in f.readlines()]

def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])


def move_ship(nav_data, cmd):
    dir_from_angle = {0:"E", 90:"N", 180:"W", 270:"S"}
    c = cmd[0]
    val = int(cmd[1:])

    if c == "W":
        nav_data[0][0] -= val
    elif c == "E":
        nav_data[0][0] += val
    elif c == "N":
        nav_data[0][1] += val
    elif c == "S":
        nav_data[0][1] -= val

    elif c == "R":
        nav_data[1] = (nav_data[1] - val) % 360
    elif c == "L":
        nav_data[1] = (nav_data[1] + val) % 360

    elif c == "F":
        move_ship(nav_data, dir_from_angle[nav_data[1]] + cmd[1:])


def rotate_wp(wp, degrees): #Recursively rotate 90 degrees until we are done:
    return wp if degrees == 0 else rotate_wp(np.array([-wp[1], wp[0]]), degrees - 90)


def move_ship_wp(ship, wp, cmd):
    c = cmd[0]
    val = int(cmd[1:])

    if c == "W":
        wp[0] -= val
    elif c == "E":
        wp[0] += val
    elif c == "N":
        wp[1] += val
    elif c == "S":
        wp[1] -= val

    elif c == "R":
        wp = rotate_wp(wp, (-val) % 360)
    elif c == "L":
        wp = rotate_wp(wp, val)

    elif c == "F":
        for times in range(val):
            ship = ship + wp

    return [ship, wp]


def part_1(data):
    nav_data = [[0, 0], 0] # [ship_pos = [0, 0], direction = 0 degrees]
    for line in data:
        move_ship(nav_data, line)
    return manhattan(nav_data[0])


def part_2(data):
    wp = np.array([10, 1])
    ship = np.array([0, 0])
    for line in data:
        [ship, wp] = move_ship_wp(ship, wp, line)
    return manhattan(ship)


def main():
    print("Answer to ex 1:   {0}".format(part_1(get_data("12_test_data.txt"))))
    print("Answer to ex 2:   {0}".format(part_2(get_data("12_test_data.txt"))))

    print("Answer to part 1: {0}".format(part_1(get_data("12_data.txt"))))
    print("Answer to part 2: {0}".format(part_2(get_data("12_data.txt"))))


if __name__ == "__main__":
    main()


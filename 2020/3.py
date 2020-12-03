#!/usr/bin/python3
# 272
# 3898725600

data = []
width = 0
height = 0

with open("3_data.txt") as f:
   for line in f.readlines():
      data.append((line.strip()))
      height += 1
width = len(data[0])


def go_right (x, dx):
    new = x + dx
    if new >= width:
        new = new - width
    return new


def go_down (y, dy):
    return y + dy


def trees (dx, dy):
    trees = 0
    y = 0
    x = 0

    while (True):
        if data[y][x] == '#':
            trees = trees + 1

        x = go_right(x, dx)
        y = go_down(y, dy)
        if y >= height:
            return trees

print(trees(3,1))
print(trees(1,1) * trees(3,1) * trees(5,1) * trees(7,1) * trees(1,2))


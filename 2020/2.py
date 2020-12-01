#!/usr/bin/python3

data = []
with open("2_data.txt") as f:
   for line in f.readlines():
      data.append(int(line))

n = len(data)


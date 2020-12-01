#!/usr/bin/python3

data = []
with open("1_data.txt") as f:
   for line in f.readlines():
      data.append(int(line))

n = len(data)

for i in range(n - 1):
    for j in range(i + i, n):
            if data[i] + data[j] == 2020:
                print("Answer 1: {0}".format (data[i] * data[j]))

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range (j + 1, n):
            if data[i] + data[j] + data[k] == 2020:
                print("Answer 2: {0}".format (data[i] * data[j] * data[k]))


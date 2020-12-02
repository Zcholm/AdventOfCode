#!/usr/bin/python3

data = []
with open("2_data.txt") as f:
   for line in f.readlines():
      data.append((line))


def is_valid1(password):
    rng = password.split(' ')[0].split('-')

    mn = int(rng[0])
    mx = int(rng[1])

    lt = password.split(' ')[1][0]

    pw = password.split(' ')[2]

    if pw.count(lt) >= mn and pw.count(lt) <= mx:
        return 1
    return 0


def is_valid2(password):
    rng = password.split(' ')[0].split('-')

    mn = int(rng[0])
    mx = int(rng[1])

    lt = password.split(' ')[1][0]

    pw = password.split(' ')[2]

    if pw[mn - 1] == lt or pw[mx - 1] == lt:
        if pw[mn - 1] == lt and pw[mx - 1] == lt:
            return 0
        return 1
    return 0


valid1 = 0
valid2 = 0

for d in data:
     valid1 += is_valid1(d)
     valid2 += is_valid2(d)

print(valid1)
print(valid2)

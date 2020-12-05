#!/usr/bin/python3

def get_data():
    bpss = []
    with open("5_data.txt") as f:
       i = 0
       for line in f.readlines():
           bpss.append(line.strip())
    return bpss

def get_pos (n, data):
    mn = 0
    rng = 2 ** n
    mx = rng - 1

    for i in range(n):
        rng = int(rng / 2)
        if data [i] == "B" or data[i] == "R":
            mn += rng
        if data[i] == "F" or data[i] == "L":
            mx -= rng

    if mn != mx:
        exit()
    else:
        return mn

def main():
    bpss = get_data()
    ids = []
    for bps in bpss:
        ids.append(get_pos(7, bps[:7]) * 8 + get_pos(3, bps[7:]))

    print(max(ids))

    # Got to have me some nice O(n**3) complexity:
    for i in ids:
        if i + 1 not in ids and i + 2 in ids:
            print(i + 1)

if __name__ == "__main__":
    main()


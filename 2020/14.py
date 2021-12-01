#!/usr/bin/python3
import re

def get_data(s):
    d = []
    with open(s) as f:
        return [line.strip() for line in f.readlines()]


def get_mask(mask):
    if len(mask) != 36:
        raise RuntimeError

    zero_mask = 0
    one_mask = 0
    for i, c in enumerate(mask):
        if c == "1":
            one_mask |= (1 << (35 - i))
        elif c == "0":
            zero_mask |= (1 << (35 - i))
    return [zero_mask, one_mask]

def part_1(data):
    mem = {}
    mask = []
    for line in data:
        if line.startswith("mask"):
            mask = get_mask(line.split()[2])
        elif line.startswith("mem"):
            [idx, num] = [int(reg) for reg in re.findall("\d+", line)]
            num |= mask[1]
            num &= ~mask[0]
            mem[idx] = num
    return sum(mem.values())


def replace_index(string, index, new_char):
    return string[:index] + new_char + string[index + 1:]

def addr_to_int(addr):
    val = 0
    for i, c in enumerate(addr):
        if c == "1":
            val |= 1 << (len(addr) - i - 1)
    return val

def get_possible_addresses(mask, addr):
    addr |= (get_mask(mask)[1])

    idxs = [i for i, ltr in enumerate(mask) if ltr == "X"]
    addrs = []

    for num in range(2 ** len(idxs)):
        for bit, idx in enumerate(idxs):
            bit_value = (num & (1 << bit)) >> bit
            mask = replace_index(mask, idx, str(bit_value))
        addrs.append(mask)
        print([mask, addr_to_int(mask)])
    print()
    return addrs

def part_2(data):
    mem = {}
    mask = None
    for line in data:
        if line.startswith("mask"):
            mask = line.split()[2]
        elif line.startswith("mem"):
            [idx, num] = [int(reg) for reg in re.findall("\d+", line)]
            for addr in get_possible_addresses(mask, idx):
                mem[addr] = num

    return sum(mem.values())

def main():
    #print("Answer to ex 1:   {0}".format(part_1(get_data("14_test_data.txt"))))
    print("Answer to ex 2:   {0}".format(part_2(get_data("14_test_data_2.txt"))))

    print("Answer to part 1: {0}".format(part_1(get_data("14_data.txt"))))
    #print("Answer to part 2: {0}".format(part_2(get_data("14_data.txt"))))


if __name__ == "__main__":
    main()


#!/usr/bin/python3
import re
#2: >6269, <10000

def get_data():
    data = []
    with open("8_data.txt") as f:
       i = 0
       for line in f.readlines():
           data.append(line.strip())
    return data

pc = 0
acc = 0
visited = []
data = None

def execute(data, verbose = False):
    global pc, acc, visited, last_jmp

    if pc >= len(data):
        return 2

    [op, arg] = data[pc].split(' ')

    if op == "nop":
        pc += 1
    elif op == "acc":
        acc += int(arg)
        pc += 1
    elif op == "jmp":
        pc += int(arg)

    if pc in visited:
        if verbose:
            print("Infinite loop detected! ACC = {0}".format(acc))
        return 0
    else:
        visited.append(pc)
        return 1

def main():
    data = get_data()

    executes = 0
    while (execute(data, verbose = True) == 1):
        executes += 1

    for i in range(len(data)):
        global pc, acc, visited
        pc = 0
        acc = 0
        visited = []

        if data[i].startswith("jmp"):
            new_data = data.copy()
            new_data[i] = new_data[i].replace("jmp", "nop", 1)

        elif data[i].startswith("nop"):
            new_data = data.copy()
            new_data[i] = new_data[i].replace("nop", "jmp", 1)

        else:
            continue

        result = 1
        while (result == 1):
            result = execute(new_data)

        if result == 2:
            print("Finished executing, ACC = {0}, line {1} changed".format(acc, i + 1))
            print("Old: \'" + data[i] + "\'")
            print("New: \'" + new_data[i] + "\'")



if __name__ == "__main__":
    main()


#!/usr/bin/python3

def get_data():
    data = []
    with open("8_data.txt") as f:
       i = 0
       for line in f.readlines():
           data.append(line.strip())
    return data

pc = acc = 0
visited = []

def execute(data, verbose = False):
    global pc, acc, visited, last_jmp

    if pc >= len(data):
        return 2

    [op, arg] = data[pc].split(' ')

    pc += 1 if (op == "nop" or op == "acc") else int(arg)
    acc += int(arg) if op == "acc" else 0

    if pc in visited:
        print("Infinite loop detected! ACC = {0}".format(acc)) if verbose else 0
        return 0
    else:
        visited.append(pc)
        return 1

def main():
    data = get_data()

    while (execute(data, verbose = True) == 1): pass

    for i in range(len(data)):
        global pc, acc, visited
        pc = acc = 0
        visited = []

        new_data = data.copy()

        if data[i].startswith("jmp"):
            new_data[i] = new_data[i].replace("jmp", "nop", 1)

        elif data[i].startswith("nop"):
            new_data[i] = new_data[i].replace("nop", "jmp", 1)

        else: continue

        result = 1
        while (result == 1):
            result = execute(new_data)

        if result == 2:
            print("Finished executing, ACC = {0}, line {1} changed".format(acc, i + 1))
            print("Old: \'" + data[i] + "\'")
            print("New: \'" + new_data[i] + "\'")


if __name__ == "__main__":
    main()


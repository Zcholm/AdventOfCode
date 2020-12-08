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

def execute(data, part = 0):
    global pc, acc, visited

    if pc >= len(data):
        print("Finished executing, ACC = {0}".format(acc)) if part == 2 else 0
        return 2

    [op, arg] = data[pc].split(' ')

    pc += 1 if (op == "nop" or op == "acc") else int(arg)
    acc += int(arg) if op == "acc" else 0

    if pc in visited:
        print("Infinite loop detected! ACC = {0}".format(acc)) if part == 1 else 0
        return 0
    else:
        visited.append(pc)
        return 1

def main():
    data = get_data()

    while (execute(data, part = 1) == 1): pass

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

        while (execute(new_data, part = 2) == 1): pass


if __name__ == "__main__":
    main()


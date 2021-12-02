def get_input (filename):
    with open(filename) as f:
        return f.readlines()

def intify (lines):
    ints = []
    for line in lines:
        ints.append(int(line))
    return ints

def number_of_changes (indata):
    increase = -1 #first one will trigger a false increase
    decrease = 0
    same = 0
    prev = -9999999999999999999999999999999

    for point in intify(indata):
        if point == prev:
            same += 1
        elif point > prev:
            increase += 1
        else:
            decrease += 1
        prev = point

    return [decrease, increase, same]

def three_slide_sums (indata):
    indata = intify (indata)
    three_sums = []
    for idx in range (len(indata)-2):
        three_sums.append (indata[idx] + indata[idx+1] + indata[idx+2])
    return three_sums

def move_xy (instruction, pos):
    [command, dist] = instruction.split()
    if command == "forward":
        pos[0] += int (dist)
    elif command == "back":
        pos[0] -= int (dist)
    elif command == "down":
        pos[1] += int (dist)
    elif command == "up":
        pos[1] -= int (dist)

    if pos [0] < 0 or pos [1] < 0:
        raise Exception ("check your data/algorithm")
    return pos

def move_x_phi (instruction, pos):
    [command, dist] = instruction.split()
    if command == "forward":
        pos[0] += int (dist)
        pos[1] += pos[2] * int (dist)
    elif command == "back":
        pos[0] -= int (dist)
        pos[1] -= pos[2] * int (dist)
    elif command == "down":
        pos[2] += int (dist)
    elif command == "up":
        pos[2] -= int (dist)


def example_1a ():
    return number_of_changes (get_input ("01_input_example.txt"))[1]

def solution_1a ():
    return number_of_changes (get_input ("01_input.txt"))[1]

def example_1b ():
    return number_of_changes (three_slide_sums(get_input ("01_input_example.txt")))[1]

def solution_1b ():
    return number_of_changes (three_slide_sums(get_input ("01_input.txt")))[1]

def example_2a ():
    pos = [0, 0]
    for line in get_input ("02_input_example.txt"):
        move_xy (line, pos)
    return pos[0] * pos [1]

def solution_2a ():
    pos = [0, 0]
    for line in get_input ("02_input.txt"):
        move_xy (line, pos)
    return pos[0] * pos [1]

def example_2b ():
    pos = [0, 0, 0]
    for line in get_input ("02_input_example.txt"):
        move_x_phi (line, pos)
    return pos[0] * pos [1]

def solution_2b ():
    pos = [0, 0, 0]
    for line in get_input ("02_input.txt"):
        move_x_phi (line, pos)
    return pos[0] * pos [1]

def example_3a ():
    return "Hold your horses"

def solution_3a ():
    return "Hold your horses"

def example_3b ():
    return "Hold your horses"

def solution_3b ():
    return "Hold your horses"

def example_4a ():
    return "Hold your horses"

def solution_4a ():
    return "Hold your horses"

def example_4b ():
    return "Hold your horses"

def solution_4b ():
    return "Hold your horses"

def example_5a ():
    return "Hold your horses"

def solution_5a ():
    return "Hold your horses"

def example_5b ():
    return "Hold your horses"

def solution_5b ():
    return "Hold your horses"

def example_6a ():
    return "Hold your horses"

def solution_6a ():
    return "Hold your horses"

def example_6b ():
    return "Hold your horses"

def solution_6b ():
    return "Hold your horses"

def example_7a ():
    return "Hold your horses"

def solution_7a ():
    return "Hold your horses"

def example_7b ():
    return "Hold your horses"

def solution_7b ():
    return "Hold your horses"

def example_8a ():
    return "Hold your horses"

def solution_8a ():
    return "Hold your horses"

def example_8b ():
    return "Hold your horses"

def solution_8b ():
    return "Hold your horses"

def example_9a ():
    return "Hold your horses"

def solution_9a ():
    return "Hold your horses"

def example_9b ():
    return "Hold your horses"

def solution_9b ():
    return "Hold your horses"

def example_10a ():
    return "Hold your horses"

def solution_10a ():
    return "Hold your horses"

def example_10b ():
    return "Hold your horses"

def solution_10b ():
    return "Hold your horses"

def example_11a ():
    return "Hold your horses"

def solution_11a ():
    return "Hold your horses"

def example_11b ():
    return "Hold your horses"

def solution_11b ():
    return "Hold your horses"

def example_12a ():
    return "Hold your horses"

def solution_12a ():
    return "Hold your horses"

def example_12b ():
    return "Hold your horses"

def solution_12b ():
    return "Hold your horses"

def example_13a ():
    return "Hold your horses"

def solution_13a ():
    return "Hold your horses"

def example_13b ():
    return "Hold your horses"

def solution_13b ():
    return "Hold your horses"

def example_14a ():
    return "Hold your horses"

def solution_14a ():
    return "Hold your horses"

def example_14b ():
    return "Hold your horses"

def solution_14b ():
    return "Hold your horses"

def example_15a ():
    return "Hold your horses"

def solution_15a ():
    return "Hold your horses"

def example_15b ():
    return "Hold your horses"

def solution_15b ():
    return "Hold your horses"

def example_16a ():
    return "Hold your horses"

def solution_16a ():
    return "Hold your horses"

def example_16b ():
    return "Hold your horses"

def solution_16b ():
    return "Hold your horses"

def example_17a ():
    return "Hold your horses"

def solution_17a ():
    return "Hold your horses"

def example_17b ():
    return "Hold your horses"

def solution_17b ():
    return "Hold your horses"

def example_18a ():
    return "Hold your horses"

def solution_18a ():
    return "Hold your horses"

def example_18b ():
    return "Hold your horses"

def solution_18b ():
    return "Hold your horses"

def example_19a ():
    return "Hold your horses"

def solution_19a ():
    return "Hold your horses"

def example_19b ():
    return "Hold your horses"

def solution_19b ():
    return "Hold your horses"

def example_20a ():
    return "Hold your horses"

def solution_20a ():
    return "Hold your horses"

def example_20b ():
    return "Hold your horses"

def solution_20b ():
    return "Hold your horses"

def example_21a ():
    return "Hold your horses"

def solution_21a ():
    return "Hold your horses"

def example_21b ():
    return "Hold your horses"

def solution_21b ():
    return "Hold your horses"

def example_22a ():
    return "Hold your horses"

def solution_22a ():
    return "Hold your horses"

def example_22b ():
    return "Hold your horses"

def solution_22b ():
    return "Hold your horses"

def example_23a ():
    return "Hold your horses"

def solution_23a ():
    return "Hold your horses"

def example_23b ():
    return "Hold your horses"

def solution_23b ():
    return "Hold your horses"

def example_24a ():
    return "Hold your horses"

def solution_24a ():
    return "Hold your horses"

def example_24b ():
    return "Hold your horses"

def solution_24b ():
    return "Hold your horses"


def main ():
    print ("====== 1a =======")
    print (example_1a ())
    print (solution_1a ())
    print ("====== 1b =======")
    print (example_1b ())
    print (solution_1b ())

    print ("====== 2a =======")
    print (example_2a ())
    print (solution_2a ())
    print ("====== 2b =======")
    print (example_2b ())
    print (solution_2b ())

    print ("====== 3a =======")
    print (example_3a ())
    print (solution_3a ())
    print ("====== 3b =======")
    print (example_3b ())
    print (solution_3b ())

    print ("====== 4a =======")
    print (example_4a ())
    print (solution_4a ())
    print ("====== 4b =======")
    print (example_4b ())
    print (solution_4b ())

    print ("====== 5a =======")
    print (example_5a ())
    print (solution_5a ())
    print ("====== 5b =======")
    print (example_5b ())
    print (solution_5b ())

    print ("====== 6a =======")
    print (example_6a ())
    print (solution_6a ())
    print ("====== 6b =======")
    print (example_6b ())
    print (solution_6b ())

    print ("====== 7a =======")
    print (example_7a ())
    print (solution_7a ())
    print ("====== 7b =======")
    print (example_7b ())
    print (solution_7b ())

    print ("====== 8a =======")
    print (example_8a ())
    print (solution_8a ())
    print ("====== 8b =======")
    print (example_8b ())
    print (solution_8b ())

    print ("====== 9a =======")
    print (example_9a ())
    print (solution_9a ())
    print ("====== 9b =======")
    print (example_9b ())
    print (solution_9b ())

    print ("====== 10a =======")
    print (example_10a ())
    print (solution_10a ())
    print ("====== 10b =======")
    print (example_10b ())
    print (solution_10b ())

    print ("====== 11a =======")
    print (example_11a ())
    print (solution_11a ())
    print ("====== 11b =======")
    print (example_11b ())
    print (solution_11b ())

    print ("====== 12a =======")
    print (example_12a ())
    print (solution_12a ())
    print ("====== 12b =======")
    print (example_12b ())
    print (solution_12b ())

    print ("====== 13a =======")
    print (example_13a ())
    print (solution_13a ())
    print ("====== 13b =======")
    print (example_13b ())
    print (solution_13b ())

    print ("====== 14a =======")
    print (example_14a ())
    print (solution_14a ())
    print ("====== 14b =======")
    print (example_14b ())
    print (solution_14b ())

    print ("====== 15a =======")
    print (example_15a ())
    print (solution_15a ())
    print ("====== 15b =======")
    print (example_15b ())
    print (solution_15b ())

    print ("====== 16a =======")
    print (example_16a ())
    print (solution_16a ())
    print ("====== 16b =======")
    print (example_16b ())
    print (solution_16b ())

    print ("====== 17a =======")
    print (example_17a ())
    print (solution_17a ())
    print ("====== 17b =======")
    print (example_17b ())
    print (solution_17b ())

    print ("====== 18a =======")
    print (example_18a ())
    print (solution_18a ())
    print ("====== 18b =======")
    print (example_18b ())
    print (solution_18b ())

    print ("====== 19a =======")
    print (example_19a ())
    print (solution_19a ())
    print ("====== 19b =======")
    print (example_19b ())
    print (solution_19b ())

    print ("====== 20a =======")
    print (example_20a ())
    print (solution_20a ())
    print ("====== 20b =======")
    print (example_20b ())
    print (solution_20b ())

    print ("====== 21a =======")
    print (example_21a ())
    print (solution_21a ())
    print ("====== 21b =======")
    print (example_21b ())
    print (solution_21b ())

    print ("====== 22a =======")
    print (example_22a ())
    print (solution_22a ())
    print ("====== 22b =======")
    print (example_22b ())
    print (solution_22b ())

    print ("====== 23a =======")
    print (example_23a ())
    print (solution_23a ())
    print ("====== 23b =======")
    print (example_23b ())
    print (solution_23b ())

    print ("====== 24a =======")
    print (example_24a ())
    print (solution_24a ())
    print ("====== 24b =======")
    print (example_24b ())
    print (solution_24b ())

if __name__ == "__main__":
    main ()


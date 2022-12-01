import math

def get_input (filename):
    with open(filename) as f:
        return f.readlines()

def get_elves_calories (lines):
    elves = []
    current_elf = 0

    for line in lines:
        if line == "\n":
            elves.append (current_elf)
            current_elf = 0
        else:
            current_elf += int(line)
    elves.append (current_elf)
    return elves


def solution_1a (filename):
    elves = get_elves_calories (get_input (filename))
    return max(elves)

def solution_1b (filename):
    elves = get_elves_calories (get_input (filename))
    return sum (sorted (elves)[-3:])

#not 106111


def solution_2a (filename):
    return "Hold your horses"

def solution_2b (filename):
    return "Hold your horses"

def solution_3a (filename):
    return "Hold your horses"

def solution_3b (filename):
    return "Hold your horses"

def solution_4a (filename):
    return "Hold your horses"

def solution_4b (filename):
    return "Hold your horses"

def solution_5a (filename):
    return "Hold your horses"

def solution_5b (filename):
    return "Hold your horses"

def solution_6a (filename):
    return "Hold your horses"

def solution_6b (filename):
    return "Hold your horses"

def solution_7a (filename):
    return "Hold your horses"

def solution_7b (filename):
    return "Hold your horses"

def solution_8a (filename):
    return "Hold your horses"

def solution_8b (filename):
    return "Hold your horses"

def solution_9a (filename):
    return "Hold your horses"

def solution_9b (filename):
    return "Hold your horses"

def solution_10a (filename):
    return "Hold your horses"

def solution_10b (filename):
    return "Hold your horses"

def solution_11a (filename):
    return "Hold your horses"

def solution_11b (filename):
    return "Hold your horses"

def solution_12a (filename):
    return "Hold your horses"

def solution_12b (filename):
    return "Hold your horses"

def solution_13a (filename):
    return "Hold your horses"

def solution_13b (filename):
    return "Hold your horses"

def solution_14a (filename):
    return "Hold your horses"

def solution_14b (filename):
    return "Hold your horses"

def solution_15a (filename):
    return "Hold your horses"

def solution_15b (filename):
    return "Hold your horses"

def solution_16a (filename):
    return "Hold your horses"

def solution_16b (filename):
    return "Hold your horses"

def solution_17a (filename):
    return "Hold your horses"

def solution_17b (filename):
    return "Hold your horses"

def solution_18a (filename):
    return "Hold your horses"

def solution_18b (filename):
    return "Hold your horses"

def solution_19a (filename):
    return "Hold your horses"

def solution_19b (filename):
    return "Hold your horses"

def solution_20a (filename):
    return "Hold your horses"

def solution_20b (filename):
    return "Hold your horses"

def solution_21a (filename):
    return "Hold your horses"

def solution_21b (filename):
    return "Hold your horses"

def solution_22a (filename):
    return "Hold your horses"

def solution_22b (filename):
    return "Hold your horses"

def solution_23a (filename):
    return "Hold your horses"

def solution_23b (filename):
    return "Hold your horses"

def solution_24a (filename):
    return "Hold your horses"

def solution_24b (filename):
    return "Hold your horses"


def main ():
    print ("====== 1a =======")
    print (solution_1a ("01_input_example.txt"))
    print (solution_1a ("01_input.txt"))
    print ("====== 1b =======")
    print (solution_1b ("01_input_example.txt"))
    print (solution_1b ("01_input.txt"))

#    print ("====== 2a =======")
#    print (solution_2a ("02_input_example.txt"))
#    print (solution_2a ("02_input.txt"))
#    print ("====== 2b =======")
#    print (solution_2b ("02_input_example.txt"))
#    print (solution_2b ("02_input.txt"))
#
#    print ("====== 3a =======")
#    print (solution_3a ("03_input_example.txt"))
#    print (solution_3a ("03_input.txt"))
#    print ("====== 3b =======")
#    print (solution_3b ("03_input_example.txt"))
#    print (solution_3b ("03_input.txt"))
#
#    print ("====== 4a =======")
#    print (solution_4a ("04_input_example.txt"))
#    print (solution_4a ("04_input.txt"))
#    print ("====== 4b =======")
#    print (solution_4b ("04_input_example.txt"))
#    print (solution_4b ("04_input.txt"))
#
#    print ("====== 5a =======")
#    print (solution_5a ("05_input_example.txt"))
#    print (solution_5a ("05_input.txt"))
#    print ("====== 5b =======")
#    print (solution_5b ("05_input_example.txt"))
#    print (solution_5b ("05_input.txt"))
#
#    print ("====== 6a =======")
#    print (solution_6a ("06_input_example.txt"))
#    print (solution_6a ("06_input.txt"))
#    print ("====== 6b =======")
#    print (solution_6b ("06_input_example.txt"))
#    print (solution_6b ("06_input.txt"))
#
#    print ("====== 7a =======")
#    print (solution_7a ("07_input_example.txt"))
#    print (solution_7a ("07_input.txt"))
#    print ("====== 7b =======")
#    print (solution_7b ("07_input_example.txt"))
#    print (solution_7b ("07_input.txt"))
#
#    print ("====== 8a =======")
#    print (solution_8a ("08_input_example.txt"))
#    print (solution_8a ("08_input.txt"))
#    print ("====== 8b =======")
#    print (solution_8b ("08_input_example.txt"))
#    print (solution_8b ("08_input.txt"))
#
#    print ("====== 9a =======")
#    print (solution_9a ("09_input_example.txt"))
#    print (solution_9a ("09_input.txt"))
#    print ("====== 9b =======")
#    print (solution_9b ("09_input_example.txt"))
#    print (solution_9b ("09_input.txt"))
#
#    print ("====== 10a =======")
#    print (solution_10a ("10_input_example.txt"))
#    print (solution_10a ("10_input.txt"))
#    print ("====== 10b =======")
#    print (solution_10b ("10_input_example.txt"))
#    print (solution_10b ("10_input.txt"))
#
#    print ("====== 11a =======")
#    print (solution_11a ("11_input_example.txt"))
#    print (solution_11a ("11_input.txt"))
#    print ("====== 11b =======")
#    print (solution_11b ("11_input_example.txt"))
#    print (solution_11b ("11_input.txt"))
#
#    print ("====== 12a =======")
#    print (solution_12a ("12_input_example.txt"))
#    print (solution_12a ("12_input.txt"))
#    print ("====== 12b =======")
#    print (solution_12b ("12_input_example.txt"))
#    print (solution_12b ("12_input.txt"))
#
#    print ("====== 13a =======")
#    print (solution_13a ("13_input_example.txt"))
#    print (solution_13a ("13_input.txt"))
#    print ("====== 13b =======")
#    print (solution_13b ("13_input_example.txt"))
#    print (solution_13b ("13_input.txt"))
#
#    print ("====== 14a =======")
#    print (solution_14a ("14_input_example.txt"))
#    print (solution_14a ("14_input.txt"))
#    print ("====== 14b =======")
#    print (solution_14b ("14_input_example.txt"))
#    print (solution_14b ("14_input.txt"))
#
#    print ("====== 15a =======")
#    print (solution_15a ("15_input_example.txt"))
#    print (solution_15a ("15_input.txt"))
#    print ("====== 15b =======")
#    print (solution_15b ("15_input_example.txt"))
#    print (solution_15b ("15_input.txt"))
#
#    print ("====== 16a =======")
#    print (solution_16a ("16_input_example.txt"))
#    print (solution_16a ("16_input.txt"))
#    print ("====== 16b =======")
#    print (solution_16b ("16_input_example.txt"))
#    print (solution_16b ("16_input.txt"))
#
#    print ("====== 17a =======")
#    print (solution_17a ("17_input_example.txt"))
#    print (solution_17a ("17_input.txt"))
#    print ("====== 17b =======")
#    print (solution_17b ("17_input_example.txt"))
#    print (solution_17b ("17_input.txt"))
#
#    print ("====== 18a =======")
#    print (solution_18a ("18_input_example.txt"))
#    print (solution_18a ("18_input.txt"))
#    print ("====== 18b =======")
#    print (solution_18b ("18_input_example.txt"))
#    print (solution_18b ("18_input.txt"))
#
#    print ("====== 19a =======")
#    print (solution_19a ("19_input_example.txt"))
#    print (solution_19a ("19_input.txt"))
#    print ("====== 19b =======")
#    print (solution_19b ("19_input_example.txt"))
#    print (solution_19b ("19_input.txt"))
#
#    print ("====== 20a =======")
#    print (solution_20a ("20_input_example.txt"))
#    print (solution_20a ("20_input.txt"))
#    print ("====== 20b =======")
#    print (solution_20b ("20_input_example.txt"))
#    print (solution_20b ("20_input.txt"))
#
#    print ("====== 21a =======")
#    print (solution_21a ("21_input_example.txt"))
#    print (solution_21a ("21_input.txt"))
#    print ("====== 21b =======")
#    print (solution_21b ("21_input_example.txt"))
#    print (solution_21b ("21_input.txt"))
#
#    print ("====== 22a =======")
#    print (solution_22a ("22_input_example.txt"))
#    print (solution_22a ("22_input.txt"))
#    print ("====== 22b =======")
#    print (solution_22b ("22_input_example.txt"))
#    print (solution_22b ("22_input.txt"))
#
#    print ("====== 23a =======")
#    print (solution_23a ("23_input_example.txt"))
#    print (solution_23a ("23_input.txt"))
#    print ("====== 23b =======")
#    print (solution_23b ("23_input_example.txt"))
#    print (solution_23b ("23_input.txt"))
#
#    print ("====== 24a =======")
#    print (solution_24a ("24_input_example.txt"))
#    print (solution_24a ("24_input.txt"))
#    print ("====== 24b =======")
#    print (solution_24b ("24_input_example.txt"))
#    print (solution_24b ("24_input.txt"))

if __name__ == "__main__":
    main ()


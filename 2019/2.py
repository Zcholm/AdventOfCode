# Challenge: https://adventofcode.com/2019/day/2
def add(code, p):
    code[code[p + 3]] = code[code[p + 2]] + code[code[p + 1]]


def mult(code, p):
    code[code[p + 3]] = code[code[p + 2]] * code[code[p + 1]]


def run(code, p, n, v):
    code[1] = n
    code[2] = v
    while code[p] != 99:
        if code[p] == 1:
            add(code, p)
        elif code[p] == 2:
            mult(code, p)
        p += 4


# Read and convert input file to ints:
int_code = open("2_data.txt").read().split(",")
for idx, char in enumerate(int_code):
    int_code[idx] = int(int_code[idx])

# Create a copy so we don´t need to read the file each time:
test_code = int_code.copy()

# Run the program for part 1:
run(test_code, 0, 12, 2)
print("Answer 1: {}".format(test_code[0]))

# Part 2:
wanted_out = 19690720

size = len(int_code)

for noun in range(size):
    for verb in range(size):
        test_code = int_code.copy()
        run(test_code, 0, noun, verb)
        if test_code[0] == wanted_out:
            print("Answer 2: {}".format(100 * noun + verb))
            break

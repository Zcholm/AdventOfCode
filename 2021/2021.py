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

def main ():
    print ("====== 1a =======")
    print (number_of_changes (get_input ("01a_input_example.txt"))[1])
    print (number_of_changes (get_input ("01a_input.txt"))[1])
    print ("====== 1b =======")
    print (number_of_changes (three_slide_sums(get_input ("01a_input_example.txt")))[1])
    print (number_of_changes (three_slide_sums(get_input ("01a_input.txt")))[1])

if __name__ == "__main__":
    main ()


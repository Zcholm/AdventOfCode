#!/usr/bin/python3

alphabet = ['a', 'b', 'c', 'd', 'e',\
            'f', 'g', 'h', 'i', 'j',\
            'k', 'l', 'm', 'n', 'o',\
            'p', 'q', 'r', 's', 't',\
            'u', 'v', 'w', 'x', 'y',\
            'z']


def get_data():
    groups = [[]]
    with open("6_data.txt") as f:
       i = 0
       for line in f.readlines():
           if line.strip() == "":
              i += 1
              groups.append([])
           else:
               groups[i].append(line.strip())
    return groups


def get_number_1 (groups):
    num = 0
    for group in groups:
        answered = []
        for form in group:
            for c in alphabet:
                if c in form and c not in answered:
                    answered.append(c)
                    num += 1
    print(num)


def get_number_2 (groups):
    num = 0
    for group in groups:
        answered = alphabet.copy()
        for c in alphabet:
            c_in_all = True
            for form in group:
                if c not in form:
                    c_in_all = False
            if c_in_all:
                num += 1
    print(num)


def main():
    get_number_1(get_data())
    get_number_2(get_data())


if __name__ == "__main__":
    main()


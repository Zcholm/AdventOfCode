def add(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    code[code[p + 3]] = code[adr2] + code[adr1]
    return p + 4


def mult(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    code[code[p + 3]] = code[adr2] * code[adr1]
    return p + 4


def store(code, p, inp):
    code[code[p + 1]] = inp
    return p + 2


def output(code, p, m1):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    print("Ouput: {}".format(code[adr1]))
    return p + 2


def jit(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    if code[adr1] != 0:
        return code[adr2]
    else:
        return p + 3


def jif(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    if code[adr1] == 0:
        return code[adr2]
    else:
        return p + 3


def lt(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    if code[adr1] < code[adr2]:
        code[code[p + 3]] = 1
    else:
        code[code[p + 3]] = 0
    return p + 4


def eq(code, p, m1, m2):
    if m1 == 0:
        adr1 = code[p + 1]
    else:
        adr1 = p + 1
    if m2 == 0:
        adr2 = code[p + 2]
    else:
        adr2 = p + 2
    if code[adr1] == code[adr2]:
        code[code[p + 3]] = 1
    else:
        code[code[p + 3]] = 0
    return p + 4


def run(code, inp):
    p = 0
    while code[p] != 99:
        op = code[p] % 100
        m1 = int(("0000" + str(code[p]))[-3])
        m2 = int(("0000" + str(code[p]))[-4])
        if op == 1:
            p = add(code, p, m1, m2)
        elif op == 2:
            p = mult(code, p, m1, m2)
        elif op == 3:
            p = store(code, p, inp)
        elif op == 4:
            p = output(code, p, m1)
        elif op == 5:
            p = jit(code, p, m1, m2)
        elif op == 6:
            p = jif(code, p, m1, m2)
        elif op == 7:
            p = lt(code, p, m1, m2)
        elif op == 8:
            p = eq(code, p, m1, m2)


with open("7_data.txt", "r") as file:
    strdata = file.read().split(",")
    dat = []

    for val in strdata:
        dat.append(int(val))


def permute(a, l, r):
    if l == r:
        global perms
        perms.append(a.copy())
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]  # backtrack


perms = []

settings = [0, 1, 2, 3, 4]
n = len(settings)
permute(settings, 0, n - 1)

run(dat, 0)

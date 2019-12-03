file = open("3_data.txt")
lines = file.readlines()

cableTurns =[[0,0]]

lines[0] = lines[0].split(",")
lines[1] = lines[1].split(",")

cable= []
crossings = []

for line_idx, line in enumerate(lines):
    x = 0
    y = 0
    length = 0
    for turn_idx, turn in enumerate(lines[line_idx]):
        dir = turn[:1]
        dist = int(turn[1:])

        for i in range(dist):
            if dir == "R":
                x += 1
            elif dir == "L":
                x -= 1
            elif dir == "U":
                y += 1
            elif dir == "D":
                y -= 1

            length += 1
            if line_idx == 0:           # This little if statement will hog your cpu the coming 5-15 minutes, enjoy!
                cable.append([x, y])
            elif [x,y] in cable:
                crossings.append([x,y])

closest = abs(crossings[0][0]) + abs(crossings[0][1])

for crossing in crossings:
    closest = min(closest, abs(crossing[0]) + abs(crossing[1]))

#print(crossings)
print("The shortest Manhattan distance to a crossing is {}.".format(closest))

# Part 2:
noOfCrossings = len(crossings)
lengths = [[0] * noOfCrossings, [0]*noOfCrossings]

for line_idx, line in enumerate(lines):
    x = 0
    y = 0
    length = 0
    for turn_idx, turn in enumerate(lines[line_idx]):
        dir = turn[:1]
        dist = int(turn[1:])

        for i in range(dist):
            if dir == "R":
                x += 1
            elif dir == "L":
                x -= 1
            elif dir == "U":
                y += 1
            elif dir == "D":
                y -= 1
            length += 1
            for cross_idx, crossing in enumerate(crossings):
                if crossing == [x, y]:
                    lengths[line_idx][cross_idx] = length

totalLengths = []
for idx, length in enumerate(lengths[0]):
    totalLengths.append(lengths[0][idx] + lengths[1][idx])

print("The shortest total cable length to a line crossing is {}.".format(min(totalLengths)))

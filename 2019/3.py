def isCrossing(x, y, ):


file = open("3_data.txt")

lines = file.readlines()

# Start by asserting the size of the grid:
xmin = 0
xmax = 0
ymin = 0
ymax = 0

cableTurns =[[0,0]]

line1 = lines[0]
line2 = lines[1]

line1 = line1.split(",")
line2 = line2.split(",")

print(line1)
print(line2)

x = 0
y = 0

horizontalLines = []
verticalLines = []

for turn in line1:
    dir = turn[:1]
    dist = int(turn[1:])
    if dir == "R":
        x += dist
        xmax = max(xmax, x)
        horizontalLines.append(y)
    elif dir == "L":
        x -= dist
        xmin = min(xmin, x)
        horizontalLines.append(y)
    elif dir == "U":
        y += dist
        ymax = max(ymax, y)
        verticalLines.append(x)
    elif dir == "D":
        y -= dist
        ymin = min(ymin, y)
        verticalLines.append(x)
    cableTurns.append([x, y])


print(verticalLines)
print(horizontalLines)















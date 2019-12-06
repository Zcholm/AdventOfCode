def no_orbits(lines, obj):
    # Recursively find the number of objects visited on the path towards COM,
    # and save the path for later comparison:
    global path_object
    path_object.append(obj)
    for line in lines:
        obj_a = line[:3]
        obj_b = line[-4:-1]
        if obj == obj_b:
            return 1 + no_orbits(lines, obj_a)
    return 0


# Open input file:
with open("6_data.txt", "r") as file:
    lines = file.readlines()

# Get a list of all individual objects:
objects = []
for line in lines:
    obj_a = line[:3]
    obj_b = line[-4:-1]
    if obj_a not in objects:
        objects.append(obj_a)
    if obj_b not in objects:
        objects.append(obj_b)

# An array to store the path taken to COM, used in part 2:
path_object = []

# Solve part 1:
total = 0
for obj in objects:
    total += no_orbits(lines, obj)
print("There are {} orbits.".format(total))

# Get path to COM for you and Santa.
# Arrays must be copied to be saved when their reference is cleared:
path_object = []
no_orbits(lines, "YOU")
path_you = path_object.copy()
path_object = []
no_orbits(lines, "SAN")
path_santa = path_object.copy()

# Loop from the back (from COM) to find the outermost common object both you and santa orbits:
i = 1
while path_santa[-i] == path_you[-i]:
    i += 1

path_len = len(path_santa) + len(path_you) - 2 * i
print("You must do {} orbital transfers to reach Santa.".format(path_len))

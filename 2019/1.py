file = open("1_data.txt").readlines()

def fuel_req(weight):
    sum = 0

    while weight > 0:
        weight = max(0, weight // 3 - 2)
        sum += weight

    return sum


module_fuel_sum = 0
fuel_fuel_sum = 0

for line in file:
    module_fuel = (int(line) // 3 ) - 2
    fuel_fuel = fuel_req(module_fuel)
    module_fuel_sum += module_fuel
    fuel_fuel_sum += fuel_fuel

fuel_sum = module_fuel_sum + fuel_fuel_sum

print("Answer 1: {}\nAnswer 2: {} ".format(module_fuel_sum, fuel_sum))

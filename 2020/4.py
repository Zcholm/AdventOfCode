#!/usr/bin/python3
import re

passports = [""]
width = 0
height = 0

with open("4_data.txt") as f:
   i = 0
   for line in f.readlines():
       if line.strip() == "":
          i += 1
          passports.append("")
       passports[i] += line.strip() + " "

def byr_valid(byr):
    try:
        year = int(re.search("\d{4}", byr).group(0))
    except:
        return False
    if year >= 1920 and year <= 2002:
        return True
    return False

def iyr_valid(iyr):
    try:
        year = int(re.search("\d{4}", iyr).group(0))
    except:
        return False
    if year >= 2010 and year <= 2020:
        return True
    return False

def eyr_valid(eyr):
    try:
        year = int(re.search("\d{4}", eyr).group(0))
    except:
        return False
    if year >= 2020 and year <= 2030:
        return True
    return False

def hgt_valid(hgt):
    h = int(re.search("\d+", hgt).group(0))
    if re.search("cm", hgt):
        return (h >= 150 and h <= 193)
    if re.search("in", hgt):
        return (h >= 59 and h <= 76)

def is_valid_1(passport):
    req_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in req_fields:
        if field not in passport:
            return False
    return True

def is_valid_2(passport):
    if not is_valid_1(passport):
        return False
    try:
        byr = re.search("byr:\d{4}", passport).group(0)
    except:
        return False
    try:
        iyr = re.search("iyr:\d{4}", passport).group(0)
    except:
        return False
    try:
        eyr = re.search("eyr:\d{4}", passport).group(0)
    except:
        return False
    try:
        hgt = re.search("hgt:\d+(cm|in)", passport).group(0)
    except:
        return False
    try:
        hcl = re.search("hcl:#[0-9a-f]{6}[ ]", passport).group(0)
    except:
        return False
    try:
        ecl = re.search("ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport).group(0)
    except:
        return False
    try:
        pid = re.search("pid:[0-9]{9}[ ]", passport).group(0)
    except:
        return False

    if not byr_valid(byr):
        return False
    if not iyr_valid(iyr):
        return False
    if not eyr_valid(eyr):
        return False
    if not hgt_valid(hgt):
        return False
    # The rest are deemed valid by regex alone:
    return True

count_1 = 0
count_2 = 0
for passport in passports:
    if is_valid_1(passport):
        count_1 += 1
    if is_valid_2(passport):
        count_2 += 1
print(count_1)
print(count_2)

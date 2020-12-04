
from typing import Callable

# For part 1, a passport is valid if all the keys are present
# For part 2, the key needs to be present and the validtor function needs to return True

# The keys on a passport line
passport_keys = [
    "byr:", # (Birth Year)
    "iyr:", # (Issue Year)
    "eyr:", # (Expiration Year)
    "hgt:", # (Height)
    "hcl:", # (Hair Color)
    "ecl:", # (Eye Color)
    "pid:", # (Passport ID)
    # "cid:", # (Country ID) (optional and ignored)
]

## Used by the height validator function to make sure the height is in the proper range
height_max = {
    'cm': 193,
    'in': 76,
}

height_min = {
    'cm': 150,
    'in': 59,
}

# Validator functions for part 2
###  byr (Birth Year) - four digits; at least 1920 and at most 2002.
###  iyr (Issue Year) - four digits; at least 2010 and at most 2020.
###  eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
###  hgt (Height) - a number followed by either cm or in:
###      If cm, the number must be at least 150 and at most 193.
###      If in, the number must be at least 59 and at most 76.
###  hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
###  ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
###  pid (Passport ID) - a nine-digit number, including leading zeroes.
###  cid (Country ID) - ignored, missing or not.

validators = {
    "byr:": lambda x: int(x) >= 1920 and int(x) <= 2002,
    "iyr:": lambda x: int(x) >= 2010 and int(x) <= 2020,
    "eyr:": lambda x: int(x) >= 2020 and int(x) <= 2030,
    "hgt:": lambda x: x[:-2].isdigit() and int(x[:-2]) >= height_min[x[-2:]] and int(x[:-2]) <= height_max[x[-2:]],
    "hcl:": lambda x: len(x) == 7 and x[0] == '#' and all(c in "0123456789abcdef" for c in x[1:]),
    "ecl:": lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    "pid:": lambda x: len(x) == 9 and x.isdigit(),
}

## Given a passport string and a key, returns the value associate with that key as a string with 
## no following whitespace.
## Expects that passport key:value pairs will be separated by whitespace
def get_value(passport: str, key: str) -> str:
    pos = passport.find(key)
    if pos < 0:
        return None
    end = start = pos + len(key)
    while end < len(passport) and not passport[end].isspace():
        end += 1
    return passport[start:end]

## The main validation function for part 2
## Given a passport string, checks that every key is present and that the associated value is valid
def part2_is_valid(passport: str) -> bool:
    for key in passport_keys:
        value = get_value(passport, key)
        if not value or not validators[key](value):
            return False

    return True

## The main validation function for part 1
## Just checks that all of the necessary keys are present
def part1_is_valid(passport: str) -> bool:
    for key in passport_keys:
        if passport.find(key) < 0:
            return False
    return True


# Goes through the whole file, and tallies how many passports are valid
# multi-line passport entries are compacted to a single line before being passed to the validator
# function
def solve(validator: Callable[[str], bool], filename: str) -> int:
    num_valid = 0
    current_passport = ""

    with open(filename) as f:
        for line in f:
            # at a blank line process the current passport
            if line.isspace():
                if validator(current_passport):
                    num_valid += 1
                current_passport = ""
            else:
                # concatenate multiple line passports to a single string
                current_passport += line

    return num_valid

def main():
    print(solve(part1_is_valid, 'input4.txt'))
    print(solve(part2_is_valid, 'input4.txt'))

main()
import re

def part1(filename):
    def is_valid(min, max, letter, pw):
        cnt = pw.count(letter)
        return cnt >= int(min) and cnt <= int(max)

    num_valid = 0

    with open(filename) as f:
        for line in f:
            m = re.match('\A(\d+)-(\d+)\s+(\w+):\s+(\w+)', line)
            if is_valid(min=m.group(1), max=m.group(2), letter=m.group(3), pw=m.group(4)):
                num_valid += 1

    return num_valid

def part2(filename):
    def is_valid(min, max, letter, pw):
        return (pw[int(min)-1] == letter) != (pw[int(max)-1] == letter)

    num_valid = 0

    with open(filename) as f:
        for line in f:
            m = re.match('\A(\d+)-(\d+)\s+(\w+):\s+(\w+)', line)
            if is_valid(min=m.group(1), max=m.group(2), letter=m.group(3), pw=m.group(4)):
                num_valid += 1

    return num_valid

print(part1('input2.txt'))
print(part2('input2.txt'))
import re

def parse(line):
    m = re.match('\A(\d+)-(\d+)\s+(\w+):\s+(\w+)', line)
    return [m.group(1), m.group(2), m.group(3), m.group(4)]

def test1(min, max, letter, pw):
    cnt = pw.count(letter)
    return cnt >= int(min) and cnt <= int(max)

def test2(min, max, letter, pw):
    return (pw[int(min)-1] == letter) != (pw[int(max)-1] == letter)

def main(filename, test):
    num_valid = 0

    with open(filename) as f:
        for line in f:
            if test(*parse(line)):
                num_valid += 1

    return num_valid

print(main('input2.txt', test1))
print(main('input2.txt', test2))
import re

def parse(line):
    m = re.match('\A(\d+)-(\d+)\s+(\w+):\s+(\w+)', line)
    return [m.group(1), m.group(2), m.group(3), m.group(4)]

def test1(min, max, letter, pw):
    cnt = pw.count(letter)
    return cnt >= int(min) and cnt <= int(max)

def test2(min, max, letter, pw):
    return (pw[int(min)-1] == letter) != (pw[int(max)-1] == letter)

lines = [parse(line) for line in open("input/input2.txt").readlines()]

# Part 1
print(len([line for line in lines if test1(*line)]))

# Part 2
print(len([line for line in lines if test2(*line)]))
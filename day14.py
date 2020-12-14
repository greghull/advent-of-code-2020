# Program requirements are at: https://adventofcode.com/2020/day/14
import re

# Parses a line into an array of tokens
# Lines come in 2 forms:
# mask = X0100001101000X1100X0110XX11111X1000
# mem[44272] = 88008
def parse(line):
    tokens = re.sub(r"\s+", "", line).split('=')
    m = re.match('\Amem\[(\d+)\]', tokens[0])
    if m:
        tokens[0] = int(m.group(1))
        tokens[1] = int(tokens[1])
    return tokens

# Reads a file and parses each line
# Returns an array of parsed lines
def read(filename):
    with open(filename) as f: 
        return [parse(line) for line in f]

# Evaluates the code according to the rules of Part 1
def eval(code):
    mem = {}
    and_mask = 0xFFFFFFFF
    or_mask = 0

    for cmd in code:
        op, arg = cmd[0], cmd[1]
        if op == "mask":
            or_mask = int(arg.replace('X', '0'), 2)
            and_mask = int(arg.replace('X', '1'), 2)
        else:
            mem[op] = (arg | or_mask) & and_mask

    return sum(mem.values())

# Given a mask, and a memory address, return the write mask which indicates which
# memory addresses should be written to
def write_mask(mask, address):
    wmask = []
    for i, b in enumerate(mask):
        if b == '0':
            wmask.append(address[i])
        else:
            wmask.append(b)
    return "".join(wmask)

# utility function
def write_locations_recur(mask): 
    loc = mask.find('X')
    if loc < 0:
        return mask
    else:
        return " ".join([write_locations_recur(mask.replace('X', '1', 1)), write_locations_recur(mask.replace('X', '0', 1))])

# Given a mask and a memory address, return a list of all the memory address that should be 
# written to
def write_locations(mask, addr):
    wmask = write_mask(mask, "{0:36b}".format(addr).replace(' ', '0'))
    return write_locations_recur(wmask).split(' ')

# Evaluates the code according to the rules of Part 2
def eval2(code):
    mem = {}
    mask = '0' * 36

    for cmd in code:
        if  cmd[0] == "mask":
            mask = cmd[1]
        else:
            for loc in write_locations(mask, cmd[0]):
                mem[int(loc, 2)] = cmd[1]

    return sum(mem.values())


print(eval(read("input/input14.txt")))
print(eval2(read("input/input14.txt")))
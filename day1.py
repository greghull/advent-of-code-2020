from itertools import product

data = [int(line) for line in open("input/input1.txt").readlines()]


def part1(d):
    pair = next((x for x in product(d, d) if x[0] + x[1] == 2020))
    return pair[0] * pair[1]


def part2(d):
    s = [x for x in product(d, d) if x[0] + x[1] < 2020]
    triplet = next((x for x in product(s, d) if x[0][0]+x[0][1]+x[1] == 2020))
    return triplet[0][0] * triplet[0][1] * triplet[1]


print(part1(data))
print(part2(data))

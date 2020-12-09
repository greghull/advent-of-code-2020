import re, strutils

type
    Password = tuple
        min: int
        max: int
        ch: char
        pw: string

proc parse(line: string): Password =
    var matches: array[4, string]
    if re.match(line, re"\A(\d+)-(\d+)\s+(\w+):\s+(\w+)", matches):
        return (strutils.parseInt(matches[0]), strutils.parseInt(matches[1]), 
                matches[2][0], matches[3])

proc test1(p: Password): bool =
    let cnt = strutils.count(p.pw, p.ch)
    return cnt >= p.min and cnt <= p.max

proc test2(p: Password): bool =
    return (p.pw[p.min-1] == p.ch) != (p.pw[p.max-1] == p.ch)

proc solve(filename: string, test: proc(pw: Password): bool): int =
    for line in lines filename:
        if test(parse(line)):
            result += 1


echo solve("../input/input2.txt", test1)
echo solve("../input/input2.txt", test2) 
import re, strutils, sequtils

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

proc test1(p: Password): int =
    let cnt = p.pw.count(p.ch)
    if cnt >= p.min and cnt <= p.max: return 1

proc test2(p: Password): int =
    if (p.pw[p.min-1] == p.ch) != (p.pw[p.max-1] == p.ch):
        return 1

proc solve(filename: string, test: proc(pw: Password): int): int =
    return toSeq(lines filename).mapIt((test(parse(it)))).foldl(a+b)

echo solve("../input/input2.txt", test1)
echo solve("../input/input2.txt", test2) 
import strutils, algorithm, sequtils

proc solve_part1(s: seq[int]): int =
    let reversed = s.reversed()
    for i in s:
        for j in reversed:
            if i+j == 2020:
                return i*j
            elif i+j < 2020:
                break

    return 0

proc solve_part2(s: seq[int]): int = 
    for i in 0 ..< s.len:
        for j in i+1 ..< s.len:
            if s[i] + s[j] >= 2020:
                break
            for k in 0 ..< s.len:
                let val = s[i]+s[j]+s[k]
                if val > 2020:
                    break
                elif val == 2020:
                    return s[i]*s[j]*s[k]
    return 0

#let data = load_data("../input/input1.txt")
var data = toSeq(lines "../input/input1.txt").mapIt(it.parseInt()).sorted()

echo solve_part1(data)
echo solve_part2(data)
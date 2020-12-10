import sets, tables, sequtils

# For a group, count the number of questions to which anyone answered "yes".
proc eval1(group: seq[string]): int = 
    # yes is the set of questions that anyone answered 'yes' to
    var yes = initHashSet[char]()

    for line in group:
        for ch in line:
            yes.incl(ch)

    # return the number of questions that anyone answered yes to
    return yes.len

# For each group, count the number of questions to which everyone answered "yes".
proc eval2(group: seq[string]): int = 
    # yes is a map from the letter representing each question to how many people within the 
    # group answered yes to that question
    var yes = initCountTable[char]()

    for line in group:
        for ch in line:
            yes.inc(ch)

    # return the number of questions that everyone said yes to
    return toSeq(yes.values).mapIt(it div group.len).foldl(a+b)
    
    
# Solve part1 of the day's problem
proc solve(filename: string, eval: proc(g: seq[string]): int): int =
    var 
        # Each group is an array of lines, where each line represents the answers given by a person in that group
        group: seq[string]
        # a running some of who answered yes according to each problem's requirements
        sum = 0

    for line in lines filename:
        if line == "":
            # at an empty line, eval the previous group and reset the current group
            sum += eval(group)
            group.setLen(0)
        else:
            # add the current line to the current group
            group.add(line)

    return sum

echo solve("../input/input6.txt", eval1)
echo solve("../input/input6.txt", eval2)

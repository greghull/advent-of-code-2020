# For a group, count the number of questions to which anyone answered "yes".
def eval1(group: str) -> int:
    # yes is the set of questions that anyone answered 'yes' to
    yes = set()
    for line in group:
        for ch in line:
            yes.add(ch)

    # return the number of questions that anyone answered yes to
    return len(yes)

# For each group, count the number of questions to which everyone answered "yes".
def eval2(group: str) -> int:
    # yes is a map from the letter representing each question to how many people within the 
    # group answered yes to that question
    yes = {}
    for line in group:
        for ch in line:
            yes[ch] = yes.get(ch, 0) + 1

    # return the number of questions that everyone said yes to
    return sum(map(lambda x: x // len(group), yes.values()))
    
# Solve part1 of the day's problem
def solve(filename: str, eval) -> int:
    # Each group is an array of lines, where each line represents the answers given by a person in that group
    group = []            
    # a running some of who answered yes according to each problem's requirements
    sum = 0                             
    with open(filename) as f:
        for line in f:
            if line.isspace():           
                # at an empty line, eval the previous group and reset the current group
                sum += eval(group)
                group = []
            else:
                # otherwise add the current line to the current group
                group.append(line.rstrip('\n')) 
                
    return sum


def main():
    print(solve('input/input6.txt', eval1))
    print(solve('input/input6.txt', eval2))

main()
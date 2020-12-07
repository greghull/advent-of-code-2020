## in the code below
## -- bag is a string of the form "adjective color"
## -- contents is an array of bag strings
## -- BAGS is a dictionary where the keys are each a bag, and the values are contents

BAGS = {}

## This class is used to memoize functions that count bags
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def contains(source, target):
    num = 0
    contents = BAGS[source]
    for c in contents:
        if c == target:
            num += 1
        else:
            num += contains(c, target)

    return num

@Memoize
def contents_count(source):
    contents = BAGS[source]
    num = len(contents)

    for c in contents:
        num += contents_count(c)

    return num


def expect_alpha(tokens):
    word = next(tokens)
    if not word.isalpha():
        raise Exception('Expected an alphabetic word')
    return word

def expect_bag(tokens):
    bag = ' '.join([expect_alpha(tokens), expect_alpha(tokens)])
    if not bag in BAGS:
        BAGS[bag] = []    
    return bag

def expect_literal(tokens, literal):
    err = f"Expected '{literal}'"

    if next(tokens) != literal:
        raise Exception(err)

def expect_number(tokens):
    num = next(tokens)

    if num == 'no':
        return None

    return int(num)

def parse(line):
    tokens = iter(line.split(' '))

    bag = expect_bag(tokens)
    contents = BAGS[bag]

    expect_literal(tokens, 'bags')
    expect_literal(tokens, 'contain')

    while True:
        num = expect_number(tokens)

        if not num:
            break

        inner_bag = expect_bag(tokens)
        for i in range(num):
            contents.append(inner_bag)

        if '.' in next(tokens):
            break

    return bag

# Solve part1 of the day's problem
def solve1() -> int:  
    answer = 0
    for bag in BAGS.keys():
        if contains(bag, 'shiny gold') > 0:
            answer += 1

    return answer

# Solve part2 of the day's problem
def solve2() -> int:  
    return contents_count('shiny gold')

with open('input/input7.txt') as f:
    for line in (line.rstrip('\n') for line in f):
        parse(line)

print(solve1())
print(solve2())
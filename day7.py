## Definitions
## A bag is a string of the form "adjective color".
## A contents is an array of bag strings.
## The global variable BAGS is a dictionary, where the keys are each a bag, 
## and the values are contents.

BAGS = {}

## This class is used to memoize functions that count bags
## Taken directly from https://www.python-course.eu/python3_memoization.php
class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]

## Given a source bag and a target bag, this function returns true if source bag
## will eventually contain the target bag
@Memoize
def contains(source, target):
    contents = BAGS[source]
    for c in contents:
        if c == target or contains(c, target):
            return True

    return False

# Given a source bag, this function returns the number of bags it will contain, including all nested bags.
def contents_count(source):
    contents = BAGS[source]
    return len(contents) + sum([contents_count(c) for c in contents])


## PARSER FUNCTIONS

# Given an iteration of tokens, expects the next token to be all alphabetic characters and returns it
def expect_alpha(tokens):
    word = next(tokens)
    if not word.isalpha():
        raise Exception('Expected an alphabetic word')
    return word

# Given an iteration of tokens, expects the next token to be the name of a bag and returns it
# If that name doesn't already exists in the global dictionary of BAGS, then the name is added
def expect_bag(tokens):
    bag = ' '.join([expect_alpha(tokens), expect_alpha(tokens)])
    if not bag in BAGS:
        BAGS[bag] = []    
    return bag

# Given an iteration of tokens, expects the next token to the specified literal
def expect_literal(tokens, literal):
    err = f"Expected '{literal}'"

    if next(tokens) != literal:
        raise Exception(err)

# Given an iteration of tokens, expects the next token to be a decimal number or the word 'no'
# returns the number or 0
def expect_number(tokens) -> int:
    num = next(tokens)

    if num == 'no':
        return 0

    return int(num)

# parses a line describing a bag
def parse(line):
    # We'll iterate through the line, token by token
    tokens = iter(line.split(' '))

    # First get the bag that is being described
    bag = expect_bag(tokens)
    # then retrieve the array that describes the bags contents
    contents = BAGS[bag]

    # make sure that he grammar is sane, then ignore these tokens
    expect_literal(tokens, 'bags')
    expect_literal(tokens, 'contain')

    # what follows next is a list of bags that are contained in the bag defined at the beginning
    # of the line
    while True:
        num = expect_number(tokens)
        if not num:
            break

        inner_bag = expect_bag(tokens)
        for i in range(num):
            contents.append(inner_bag)

        # next(tokens) will be one of ['bag,', 'bags,', 'bag.', 'bags.']
        # if it contains a period, then the line is ended
        if '.' in next(tokens):
            break

    return bag

# Solve part1 of the day's problem
def solve1() -> int:  
    return sum(map(lambda x: 1 if contains(x, 'shiny gold') else 0, BAGS.keys()))

# Solve part2 of the day's problem
def solve2() -> int:  
    return contents_count('shiny gold')


def main():
    with open('input/input7.txt') as f:
        for line in (line.rstrip('\n') for line in f):
            parse(line)

    print(solve1())
    print(solve2())


main()
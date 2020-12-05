# Solve for how many trees we'll encounter when taking the path
# specified by down and right.
# The solver works by moving down, then to the right.
# The default path is move down 1, then move right 1.
def solve(filename, down=1, right=1):
    trees = 0   # the number of trees we have encountered
    width = 0   # the width of the map before it repeats
    x = 0       # our current x position
    y = 0       # our current y position

    with open(filename) as f:
        for line in f:
            # if width is not yet defined, we're on the first line of the file
            # don't check for trees here.. just figure out the line width
            # subtract 1 from line width to ignore the newline
            if not width:
                width = len(line)-1

            # everytime we move down the appropriate number of lines, then we will move to the right
            # and check to see if we hit a tree
            elif y % down == 0:
                # Since the map repeats to the right infinitely, increment the x counter modulo the width
                x = (x + right) % width

                if line[x] == '#':
                    trees += 1

            # move down a line
            y += 1

    return trees


def main():
    routes = [
        {'down': 1, 'right': 1}, {'down': 1, 'right': 3}, {'down': 1, 'right': 5},
        {'down': 1, 'right': 7}, {'down': 2, 'right': 1},
    ]

    product = 1
    for route in routes: product *= solve('input/input3.txt', **route)
    print(product)

main()
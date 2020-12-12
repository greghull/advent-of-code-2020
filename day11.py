from functools import lru_cache

# Directions for searching for occupied seats
# directions = ne, n, nw, e, w, se, s, sw
DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# A rule consists of:
# - the maximum distance that we should look for empty seats
#       - None means no maximum distance  (part 2)
#       - 1 means only look at adjacent seats  (part 1)
# - the maximum number of seen seats that can be occupied
RULES = [
    { 'max_distance': 1,      # part 1 of today's problem
      'max_occupancy': 4 },
      
    { 'max_distance': None,   # part 2 if today's problem
      'max_occupancy': 5 }
]

# Given a grid, a starting location, and a direction returns 1 if an occupied seat can be seen in the
# specified direction.. otherwise returns 0
# If max_dist is given, it specifies that we only look up to that many seats away
# i.e. a max_dist of 1 means adjacent seats only
def can_see_occupied(grid, y, x, direction, max_dist=None):
    y += direction[0]
    x += direction[1]
    dist = 1

    while y >= 0 and y<len(grid) and x >= 0 and x < len(grid[y]):
        if  max_dist and dist > max_dist:
            return 0
        if grid[y][x] == '#':
            return 1
        elif grid[y][x] == 'L':
            return 0
        y += direction[0]
        x += direction[1]
        dist += 1

    return 0

# Given a grid, transforms the specified seat according to the supplied rules
def transform_seat(grid, y, x, rule):
    # shortcut for refering to the current seat
    seat = grid[y][x]
    # a lambda that determines how many nearby seats are occupied
    nearby = lambda: sum([can_see_occupied(grid, y, x, d, rule['max_distance']) for d in DIRECTIONS])
    
    if seat == '.':
        return '.'
    elif seat == 'L' and nearby() == 0:
        return '#'
    elif seat == '#' and nearby() < rule['max_occupancy']:
        return '#' 

    return 'L'

# Given a grid, transforms the row at index (y) based on the provided rules
def transform_row(grid, y, rule):
    return [transform_seat(grid,y,x,rule) for x in range(len(grid[y]))]

# Given a starting grid, and a rule, returns the new grid
def transform(grid, rule):
    return [transform_row(grid, y, rule) for y in range(len(grid))]

# Given a grid, returns the number of occupied seats
def num_occupied(grid):
    return sum([row.count('#') for row in grid])

# Pretty prints a grid
def p(grid):
    for line in grid:
        print(line)
    print()

# Given a starting grid and a rule, solves the puzzle
def solve(input, rule):
    output = transform(input, rule)

    while output != input:
        input = output
        output = transform(input, rule)

    return num_occupied(output)
        
with open("input/input11.txt") as f:
    grid = [line.rstrip('\n') for line in f]

for rule in RULES:
    print(solve(grid, rule))
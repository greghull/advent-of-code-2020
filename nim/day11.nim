import sequtils, sugar

# Directions for searching for occupied seats
# directions = ne, n, nw, e, w, se, s, sw
type
    Grid = seq[string]

    Rule = tuple
        max_distance: int
        max_occupancy: int

    Direction = tuple
        north: int
        east: int

const 
    DIRECTIONS = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

# A rule consists of:
# - the maximum distance that we should look for empty seats
#       - None means no maximum distance  (part 2)
#       - 1 means only look at adjacent seats  (part 1)
# - the maximum number of seen seats that can be occupied
    RULES = [(max_distance: 1, max_occupancy: 4), 
             (max_distance: 0, max_occupancy: 5)]

# Given a grid, a starting location, and a direction returns 1 if an occupied seat can be seen in the
# specified direction.. otherwise returns 0
# If max_dist is given, it specifies that we only look up to that many seats away
# i.e. a max_dist of 1 means adjacent seats only
proc can_see_occupied(grid: Grid, y: int, x: int, dir: Direction, max_dist=0): int = 
    var 
        y1 = y + dir[0]
        x1 = x + dir[1]
        dist = 1

    while y1 >= 0 and y1<grid.len and x1 >= 0 and x1 < len(grid[y1]):
        if  max_dist > 0 and dist > max_dist:
            return 0
        if grid[y1][x1] == '#':
            return 1
        elif grid[y1][x1] == 'L':
            return 0
        y1 += dir[0]
        x1 += dir[1]
        dist += 1

    return 0

proc nearby(grid: Grid, y: int, x: int, max_dist: int): int = 
    let n = collect(newSeq):
        for dir in DIRECTIONS:
            can_see_occupied(grid, y, x, dir, max_dist)
    return foldl(n, a+b)
  

# Given a grid, transforms the specified seat according to the supplied rules
proc transform_seat(grid: Grid, y: int, x: int, rule: Rule): char =
    # shortcut for refering to the current seat
    let seat = grid[y][x]

    if seat == '.':
        return '.'
    elif seat == 'L' and nearby(grid, y, x, rule.max_distance) == 0:
        return '#'
    elif seat == '#' and nearby(grid, y, x, rule.max_distance) < rule.max_occupancy:
        return '#' 

    return 'L'

# Given a grid, transforms the row at index (y) based on the provided rules
proc transform_row(grid: Grid, y: int, rule: Rule): string = 
    result = ""
    for x in 0 ..< grid[y].len:
        result &= transform_seat(grid, y, x, rule)

# Given a starting grid, and a rule, returns the new grid
proc transform(grid: Grid, rule: Rule): Grid =
    collect(newSeq):
        for y in 0..<grid.len:
            transform_row(grid, y, rule)

# Returns true if two grids are equal
proc grid_equals(g1, g2: Grid): bool =
    all(toSeq 0 ..< g1.len, proc (y: int): bool = g1[y] == g2[y])

# Given a grid, returns the number of occupied seats
proc num_occupied(grid: Grid): int = 
    let num = collect(newSeq):
        for row in grid:
            row.count('#')
    return num.foldl(a+b)


# Pretty prints a grid
proc p(grid: Grid) = 
    for line in grid:
        echo line
    echo ""

# Given a starting grid and a rule, solves the puzzle
proc solve(input: Grid, rule: Rule): int = 
    var 
        input = input
        output = transform(input, rule)

    while output != input:
        input = output
        output = transform(input, rule)

    return num_occupied(output)

let grid = toSeq(lines "../input/input11.txt")

for rule in RULES:
    echo solve(grid, rule)
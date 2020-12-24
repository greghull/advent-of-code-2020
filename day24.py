
DIRECTIONS = ["se", "ne", "sw", "nw", "e", "w"]

# Directions indicate how far to move along the (x,y) axis
MOVEMENT = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (0, 1),
    'sw': (0, -1),
    'nw': (-1, 1),
    'se': (1, -1),
}


def move(tile, dir):
    return (tile[0]+MOVEMENT[dir][0], tile[1]+MOVEMENT[dir][1])

def parse(line, tile=(0,0)):
    if not line:
        return tile
    for dir in DIRECTIONS:
        if line.startswith(dir):
            return parse(line[len(dir):], move(tile, dir))
    raise f"Unknown direction in: {line}"

def flip(map, tile):
    if tile in map:
        map.remove(tile)
    else:
        map.add(tile)

def neighbors(map, tile):
    return set([move(tile, dir) for dir in DIRECTIONS])


# Only record the black tiles on the map
map = set()

with open("input/input24.txt") as f:
    for line in [line.rstrip('\n') for line in f]:
        flip(map, parse(line))

print("-- Part 1 --")
print(len(map), "black tiles\n")

# Part 2
print("-- Part 2 --")
for i in range(100):
    need_flipped = set()
    for tile in map:
        n = neighbors(map, tile)        # n is all neighbors of this tile
        black_n = map & n               # black_n is only the black neighbors
        n.difference_update(black_n)    # n is now only the white neighbors

        if len(black_n) == 0 or len(black_n) > 2:
            need_flipped.add(tile)

        for white_tile in n:
            hood = neighbors(map, white_tile)
            if len(hood & map) == 2:
                need_flipped.add(white_tile)

    for tile in need_flipped:
        flip(map, tile)

print(len(map), "black tiles")


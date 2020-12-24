
DIRECTIONS = ["se", "ne", "sw", "nw", "e", "w"]


move = {
    "e": lambda t: (t[0]+1, t[1]),
    "w": lambda t: (t[0]-1, t[1]),
    "ne": lambda t: (t[0], t[1]+1),
    "sw": lambda t: (t[0], t[1]-1),
    "nw": lambda t: (t[0]-1, t[1]+1),
    "se": lambda t: (t[0]+1, t[1]-1)
}

def parse(line, tile=(0,0)):
    if not line:
        return tile
    for dir in DIRECTIONS:
        if line.startswith(dir):
            return parse(line[len(dir):], move[dir](tile))
    raise f"Unknown direction in: {line}"

# Given a tile, returns a set of all it's neighbors
def neighbors(map, tile):
    return set([move[dir](tile) for dir in DIRECTIONS])


# Only record the black tiles on the map
map = set()

with open("input/input24.txt") as f:
    for line in [line.rstrip('\n') for line in f]:
        map.symmetric_difference_update({parse(line)})

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

    map.symmetric_difference_update(need_flipped)

print(len(map), "black tiles")


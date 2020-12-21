import math

class Tile:
    def __init__(self, chunk):
        lines = chunk.split('\n')
        self.id = int(lines[0].split(' ')[1].replace(':', ''))
        self.image = lines[1:]
        if len(self.image[len(self.image)-1]) == 0:
            self.image = self.image[:-1]

    def flip(self):
        self.image.reverse()

    @property
    def width(self):
        return len(self.image[0])

    @property
    def height(self):
        return len(self.image)

    def rotate(self):
        image = []
        for i in range(len(self.image)):
            image.append("".join([self.image[j][i] for j in range(len(self.image))])[::-1])
        self.image = image

    def remove_borders(self):
        self.image = self.image[1:-1]

        for i,row in enumerate(self.image):
            self.image[i] = row[1:-1]

    @property
    def edges(self):
        s =  set([self.image[0], self.image[-1]])
        s.add("".join([line[0] for line in self.image]))
        s.add("".join([line[-1] for line in self.image]))
        return s

    @property
    def possible_edges(self):
        s = self.edges
        s.add(self.image[0][::-1])
        s.add(self.image[-1][::-1])
        s.add("".join([line[0] for line in self.image])[::-1])
        s.add("".join([line[-1] for line in self.image])[::-1])
        return s

    def edge(self, side):
        if side == 'n':
            return self.image[0]
        if side == 's':
            return self.image[-1]
        if side == 'e':
            return "".join([line[-1] for line in self.image])
        if side == 'w':
            return "".join([line[0] for line in self.image])

    def possible_corner_edges(self, tiles):
        edges = self.possible_edges.copy()
        for tile in tiles:
            if tile != self:
                edges = edges.difference(tile.possible_edges)
        return edges

    def is_corner(self, tiles):
        # A Corner piece has 2 unique edges
        # this set will hold each edge and it's refelection
        return len(self.possible_corner_edges(tiles)) == 4     

    def __str__(self):
        return "\n".join(self.image)

    def find_monster(self, x, y):
        sea_monster = [
            [18],
            [0,5,6,11,12,17,18,19],
            [1,4,7,10,13,16]
        ]

        for i, row in enumerate(sea_monster):
            for j in row:
                if y+i >= self.height or x+j >= self.width:
                    return False
                if self.image[y+i][x+j] != '#':
                    return False
        return True

    def total_monsters(self):
        cnt = 0
        for i in range(self.width):
            for j in range(self.height):
                if self.find_monster(i,j):
                    cnt += 1
        return cnt

    def find_total_monsters(self):
        for i in range(4):
            cnt = self.total_monsters()
            if cnt > 0:
                return cnt
            self.rotate()
        
        self.flip()

        for i in range(4):
            cnt = self.total_monsters()
            if cnt > 0:
                return cnt
            self.rotate()

        return 0

    def rough_water(self):
        return sum(line.count("#") for line in self.image)
 

class Grid:
    def __init__(self, tiles):
        self.tiles = tiles
        self.tile_width = len(self.tiles[0].image[0])
        self.tile_height = len(self.tiles[0].image)
        self.corners = list(filter(lambda x: x.is_corner(self.tiles), self.tiles))
        self.dim = math.floor(math.sqrt(len(tiles)))
        self.display = [[None for x in range(self.dim)] for x in range(self.dim)] 
        self.display[0][0] = self.corners[0]
        self.vert_gap = "\n"
        self.horiz_gap = " "

    def row_string(self, row):
        s = ""
        for i in range(self.tile_height):
            for tile in row:
                if tile == None:
                    s += "-" * self.tile_width
                else:
                    s += tile.image[i]
                s += self.horiz_gap
            s += "\n"
        return s

    def __str__(self):
        return "Grid 1:\n" + self.vert_gap.join([self.row_string(row) for row in self.display])

    def find_neighbor(self, piece, side):
        target = {"s": "n", "w": "e", "e": "w", "n": "s"}

        for tile in self.tiles:
            if piece == tile:
                continue

            for i in range(4):
                if piece.edge(side) == tile.edge(target[side]):
                    return tile
                tile.rotate()

            tile.flip()

            for i in range(4):
                if piece.edge(side) == tile.edge(target[side]):
                    return tile
                tile.rotate()

            tile.flip()  # mark sure tile is left in it's starting state

        return None

    def remove_borders(self):
        self.tile_width -= 2
        self.tile_height -= 2
        for tile in self.tiles:
            tile.remove_borders()

    def fill_display(self):
        corner = self.display[0][0]
        possible = corner.possible_corner_edges(self.tiles)

        if corner.edge('n') not in possible:
            corner.flip()

        # Find the top row...
        for i in range(1, self.dim):
            self.display[0][i] = self.find_neighbor(self.display[0][i-1], "e")

        #Find the rest of the rows
        for i in range(1, self.dim):
            for j in range(self.dim):
                self.display[i][j] = self.find_neighbor(self.display[i-1][j], "s")


with open('input/input20.txt') as f:
    tiles = [Tile(chunk) for chunk in f.read().split('\n\n')]


## Part 1
grid = Grid(tiles)
product = 1
print("Corners")
for tile in grid.corners:
    product *= tile.id
    print(tile)
print("Product", product, "\n")




## Part 2
grid.fill_display()
print(grid)

grid.horiz_gap = ""
grid.vert_gap = ""
grid.remove_borders()

whole = Tile(grid.__str__())


whole.rotate()
whole.rotate()
whole.rotate()
whole.flip()


print(whole)

cnt = whole.find_total_monsters()

print(cnt)
print(whole.rough_water() - cnt*15)


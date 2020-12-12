# A command for the navigation computer is an ordered pair.  
# The operand is the first value and the argument is the second value
OP = 0
ARG = 1

# A direction is an ordered pair
# y is the first value, x is the second value
Y = 0
X = 1

DIRECTIONS = {
    0: (1,0),
    90: (0,1),
    180: (-1, 0),
    270: (0, -1),
    "N": (1,0),
    "E": (0,1),
    "S": (-1, 0),
    "W": (0, -1),
}

# Navigation computer Mark 1 -- for solving problem 1
class Mark1:
    def __init__(self, bearing=0):
        self.x = 0
        self.y = 0
        self.bearing = bearing

    @property
    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)

    # Moves the ship n units in the specified direction
    def move(self, dir, n):
        self.y = self.y + n*dir[Y]
        self.x = self.x + n*dir[X]

    def eval(self, code):
        for cmd in code:
            op = cmd[OP]
            arg = cmd[ARG]

            if op in "NSEW":
                self.move(DIRECTIONS[op], arg)
            elif op == 'R':
                self.bearing = (self.bearing + arg) % 360
            elif op == 'L':
                self.bearing = (self.bearing - arg) % 360
            elif op == 'F':
                self.move(DIRECTIONS[self.bearing], arg)
                

# Navigation computer Mark 2 -- for solving problem 2
class Mark2(Mark1):
    def __init__(self, way_x=0, way_y=0):
        super().__init__()
        self.way_x = way_x
        self.way_y = way_y

    # Moves the waypoint n units in the specified direction
    def move_way(self, dir, n):
        self.way_y = self.way_y + n*dir[Y]
        self.way_x = self.way_x + n*dir[X]

    def rotate_waypoint(self, bearing):
        if bearing != 0:
            self.way_x, self.way_y = self.way_y, -1 * self.way_x
            self.rotate_waypoint(bearing-90)

    def eval(self, code):
        for cmd in code:
            op = cmd[OP]
            arg = cmd[ARG]

            if op in "NSEW":
                self.move_way(DIRECTIONS[op], arg)
            elif op == 'R':
                self.rotate_waypoint(arg % 360)
            elif op == 'L':
                self.rotate_waypoint((-1 * arg) % 360)
            elif op == 'F':
                self.move([self.way_y, self.way_x], arg)

def parse(line):
    return (line[:1], int(line[1:]))

with open("input/input12.txt") as f:    
    code = [parse(line.rstrip('\n')) for line in f]

mark1 = Mark1(bearing=90)
mark1.eval(code)
print(f"p1 manhattan distance: {mark1.manhattan_distance}")

mark2 = Mark2(way_x=10, way_y=1)
mark2.eval(code)
print(f"p2 manhattan distance: {mark2.manhattan_distance}")
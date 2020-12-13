# A command for the navigation computer is an ordered pair.  
# The operand is the first value and the argument is the second value
OP = 0
ARG = 1

# A 4-pt compass direction is an ordered pair
COMPASS = {
    "N": (1,0),
    "E": (0,1),
    "S": (-1, 0),
    "W": (0, -1),
    0: (1,0),
    90: (0,1),
    180: (-1, 0),
    270: (0, -1),
}

TURN = {
    "L": -1,    # Turn to the left is negative degrees
    "R": 1      # Rotate to the right is positive degrees
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
        self.y += n*dir[0]
        self.x += n*dir[1]

    def eval(self, code):
        for cmd in code:
            op = cmd[OP]
            arg = cmd[ARG]

            if op in "NSEW":
                self.move(COMPASS[op], arg)
            elif op in "RL":
                self.bearing = (self.bearing + TURN[op]*arg) % 360
            elif op == 'F':
                self.move(COMPASS[self.bearing], arg)
                

# Navigation computer Mark 2 -- for solving problem 2
class Mark2(Mark1):
    def __init__(self, way_x=0, way_y=0):
        super().__init__()
        self.way_x = way_x
        self.way_y = way_y

    # Moves the waypoint n units in the specified direction
    def move_way(self, dir, n):
        self.way_y += n*dir[0]
        self.way_x += n*dir[1]

    def rotate_waypoint(self, bearing):
        if bearing != 0:
            self.way_x, self.way_y = self.way_y, -1 * self.way_x
            self.rotate_waypoint(bearing-90)

    def eval(self, code):
        for cmd in code:
            op = cmd[OP]
            arg = cmd[ARG]

            if op in "NSEW":
                self.move_way(COMPASS[op], arg)
            elif op in 'RL':
                self.rotate_waypoint((TURN[op]*arg) % 360)
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

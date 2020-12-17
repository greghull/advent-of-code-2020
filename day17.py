from array import array

# Returns a new space of dimension t * z * y * x with each point populated by a '0'
def new_4space(t, z, y, x):
    return [[[array('I', [0] * x) for j in range(y)] for i in range(z)] for d in range(t)]

# A "Space" is a 4-dimensional array indexed by t, z, y, x
# For loops the indices d,i,j,k are often used to reference t,z,y,x
# The t dimension will be ignored if time_travel is set to False
class Space:
    def __init__(self, plane, time_travel=False):
        self.points = [[plane]]

        if time_travel:
            self.time_delta = 2
        else:
            self.time_delta = 0

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, p):
        self._points = p
        self.age = len(p)
        self.depth = len(p[0])
        self.height = len(p[0][0])
        self.width = len(p[0][0][0])

    def cycle(self):
        new_points = new_4space(self.age+self.time_delta, self.depth+2, self.height+2, self.width+2)

        for t, space in enumerate(new_points):
            for i, plane in enumerate(space):
                for j, row in enumerate(plane):
                    for k in range(len(row)):
                        val = self.value_at(t-self.time_delta//2, i-1,j-1,k-1)
                        active_neighbors = self.active_neighbors(t-self.time_delta//2,i-1,j-1,k-1)
                        if val == 1 and active_neighbors in [2,3]:
                            row[k] = 1
                        elif val == 0 and active_neighbors == 3:
                            row[k] = 1

        self.points = new_points

    def value_at(self, t, z, y, x):
        if t < 0 or t >= self.age: return 0
        if z < 0 or z >= self.depth: return 0
        if y < 0 or y >= self.height: return 0
        if x < 0 or x >= self.width: return 0

        return self.points[t][z][y][x] 


    def active_neighbors(self, t, z, y, x):
        total = 0
        for d in range(t-1, t+2):
            for i in range(z-1, z+2):
                for j in range(y-1, y+2):
                    for k in range(x-1, x+2):
                        total += self.value_at(d,i,j,k)

        return total-self.value_at(t,z,y,x) # ignore specified point

    def count(self):
        total = 0
        for t in range(self.age):
            for i in range(self.depth):
                for j in range(self.height):
                    for k in range(self.width):
                        total += self.value_at(t,i,j,k)

        return total

def read(filename):
    values = {"#": 1, ".": 0}
    with open(filename) as f:
        return [array('I', [values[ch] for ch in line.rstrip('\n')]) for line in f]

space = Space(read("input/input17.txt"), time_travel=False)
for i in range(6):
    space.cycle()
print(space.count())

space = Space(read("input/input17.txt"), time_travel=True)
for i in range(6):
    space.cycle()
print(space.count())
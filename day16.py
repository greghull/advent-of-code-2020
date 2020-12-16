## Ugly code below.. but it works.

import re
from functools import reduce

class Field:
    # A Field line looks like:
    # departure location: 49-627 or 650-970
    def __init__(self, line):
        parts = line.split(': ')
        self.name = parts[0]
        
        ranges = parts[1].split(' or ')

        r = ranges[0].split('-')
        self.min1 = int(r[0])
        self.max1 = int(r[1])

        r = ranges[1].split('-')
        self.min2 = int(r[0])
        self.max2 = int(r[1])

        # A set of ticket columns that could correspond to this field
        self.possible_cols = set(range(20))

        # The ticket column that does correspond to this field
        self._col = None

    @property
    def col(self):
        if self._col is None:
            if len(self.possible_cols) == 1:
                self._col = self.possible_cols.pop()
        return self._col

    def has(self, n):
        return (n >= self.min1 and n <= self.max1) or (n >= self.min2 and n <= self.max2)
    
    def __str__(self):
        return f"{self.name}: {self.range1.start}-{self.range1.stop-1} or {self.range2.start}-{self.range2.stop-1}"

FIELDS = []
MY_TICKET = None
NEARBY_TICKETS = []

# Returns 0 if val is a VALID value for any field
# Otherwise returns the given invalid value
def invalid_value(val):
    if any([field.has(val) for field in FIELDS]):
        return 0
    return val
        

def solve1():
    total = 0
    for ticket in NEARBY_TICKETS:
        total += sum([invalid_value(v) for v in ticket])

    return total

def valid_ticket(ticket):
    # A Ticket is invalid if any of it's values is 0
    if not all(ticket):
        return False
    return sum([invalid_value(v) for v in ticket]) == 0


def scan_tickets(tickets):
    for field in FIELDS:
        for ticket in tickets:
            for i,v in enumerate(ticket):
                if not field.has(v):
                    field.possible_cols.discard(i)

def scan_fields():
    for field in FIELDS:
        if field.col is not None:
            for f in FIELDS:
                f.possible_cols.discard(field.col)


def solve2():
    # Filter out the invalid tickets
    tickets = list(filter(lambda x: valid_ticket(x), NEARBY_TICKETS))

    print([f.col for f in FIELDS])

    # Based on ticket values, try to determine which ticket column corresponds to which fields
    scan_tickets(tickets)

    print([f.col for f in FIELDS])

    # There is now at least 1 field that has only a single possible column... r
    # remove that column from the list of possible columns for the other fields.  
    # Repeat this process until we can determine the column identies for at least the first 6 fields
    while None in [f.col for f in FIELDS]:
        scan_fields()
        print([f.col for f in FIELDS])


    # Return the product of the first 6 fields of my ticket
    return reduce(lambda x,y: x*y, [MY_TICKET[FIELDS[i].col] for i in range(6)])

with open("input/input16.txt") as f: 
    line = f.readline().rstrip('\n')

    while line:
        FIELDS.append(Field(line))
        line = f.readline().rstrip('\n')

    f.readline() # Read 'your ticket:' line
    MY_TICKET = [int(x) for x in f.readline().rstrip('\n').split(',')]

    f.readline() # read blank line
    f.readline() # Read 'nearby tickets:' line
    
    for line in [line.rstrip('\n') for line in f]:
        NEARBY_TICKETS.append([int(x) for x in line.split(',')])


print(solve1())
print(solve2())
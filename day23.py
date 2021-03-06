import array

def make_cups(lst):
    cups = array.array("Q", [0] * (len(lst)+1))
    for i in range(len(lst)-1):
        cups[lst[i]] = lst[i+1]
    cups[lst[-1]] = lst[0]
    return cups

def pp(cups, current):
    print(f"cups: ({current})", end=" ")

    cup = cups[current]

    while cup != current:
        print(cup, end=" ")
        cup = cups[cup]
    print()

def pickup(cups, current):
    pc = [0] * 3

    pc[0] = cups[current]
    pc[1] = cups[pc[0]]
    pc[2] = cups[pc[1]]
    cups[current] = cups[pc[2]]

    return pc

def insert(cups, dest, pc):
    tmp = cups[dest]
    cups[dest] = pc[0]
    cups[pc[0]] = pc[1]
    cups[pc[1]] = pc[2]
    cups[pc[2]] = tmp



def play(cups, current, base, display=True):
    if display:
        pp(cups, current)
    
    pickup_cups = pickup(cups, current)
    if display:
        print("pick up:", pickup_cups)
    
    dest = (current-1) % base
    while dest in pickup_cups or dest == 0:
        dest = (dest-1) % base
    if display:
        print("destination:", dest)

    insert(cups, dest, pickup_cups)

    return cups[current]

# PART 1
# cups = make_cups([int(x) for x in "318946572"])
# current = 3
# base = 10

# for i in range(100):
#     print("--", "Move", i+1, "--")
#     current = play(cups, current, base, display=True)
#     print()

# print("-- final --")
# pp(cups, current)

#PART 2
cups2 = make_cups([int(x) for x in "318946572"] + list(range(10,1000001)))
base2 = 1000001
current = 3
for i in range(10000000):
    current = play(cups2, current, base2, display=False)

c1 = cups2[1]
c2 = cups2[c1]
print(c1, c2, c1*c2)
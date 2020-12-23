cups = [int(x) for x in "389125467"]
base = max(cups)

def pp(cups, current):
    print("cups:", end=" ")
    for cup in cups:
        if cup == current:
            print(f"({cup})", end=" ")
        else:
            print(cup, end=" ")
    print()

def pickup(cups, idx):
    pickup_cups = []
    for i in range(3):
        pickup_cups.append(cups.pop((idx+1) % len(cups)))
    return pickup_cups

def insert_cups(cups, dest, pickup_cups):
    idx = cups.index(dest)

    for i in range(3):
        cups.insert(idx+i+1, pickup_cups[i])

def play(cups, current):
    idx = cups.index(current)
    pp(cups, current)    

    pickup_cups = pickup(cups, idx)
    print("pick up:", pickup_cups)

    dest = (current-1) % base
    while dest not in cups:
        dest = (dest-1) % base
    print("destination:", dest)

    insert_cups(cups, dest, pickup_cups)

    return cups[(idx+1) % len(cups)]

current = 3
for i in range(10):
    print("--", "Move", i+1, "--")
    current = play(cups, current)
    print()
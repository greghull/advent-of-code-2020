def solve(n_rounds, initial):
    mem = {}
    last = 0

    for i, n in enumerate(initial):
        mem[n] = i+1
        last = n

    for i in range(len(initial), n_rounds):
        next = i - mem.get(last, i)
        mem[last] = i
        last = next

    return last

# Using an array is faster than using a dictionary, but we have to guess blindly at initial size
def solve2(n_rounds, initial):
    mem = [None] * 100000000
    last = 0

    for i, n in enumerate(initial):
        mem[n] = i+1
        last = n

    for i in range(len(initial), n_rounds):
        if not mem[last]:
            next = 0
        else:
            next = i - mem[last]
        mem[last] = i
        last = next

    return last

print(solve2(2020, [0,13,16,17,1,10,6]))
print(solve2(30000000, [0,13,16,17,1,10,6]))

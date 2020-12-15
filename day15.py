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

print(solve(2020, [0,13,16,17,1,10,6]))
print(solve(30000000, [0,13,16,17,1,10,6]))

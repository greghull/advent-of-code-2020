# Using an array instead of a Table is __much__ faster
# but we are taking a blind guess at what the initial array
# size needs to be
proc solve(n_rounds: int, initial: seq[int]): int =
    var
        mem = newSeq[int](100000000)
        next = 0

    for i in 0 ..< len(initial):
        mem[initial[i]] = i+1
        result = initial[i]

    for i in len(initial) ..< n_rounds:
        if mem[result] == 0:
            next = 0
        else:
            next = i - mem[result]
        mem[result] = i
        result = next

echo solve(2020, @[0,13,16,17,1,10,6])
echo solve(30000000, @[0,13,16,17,1,10,6])
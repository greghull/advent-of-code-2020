import tables

proc solve(n_rounds: int, initial: seq[int]): int =
    var
        mem = initTable[int,int]()

    for i in 0 ..< len(initial):
        mem[initial[i]] = i+1
        result = initial[i]

    for i in len(initial) ..< n_rounds:
        let next = i - mem.getOrDefault(result, i)
        mem[result] = i
        result = next

echo solve(2020, @[0,13,16,17,1,10,6])
echo solve(30000000, @[0,13,16,17,1,10,6])
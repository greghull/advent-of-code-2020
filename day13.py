from functools import reduce
from operator import mul

# The schedule is a list of buses
# A bus is an ordered pair: the first item is the bus's position in the schedule
# and the second item is the bus id, which tells how often it departs


### PART 1 ###

# Given a starting time t, and a bus_id, returns how long you'll wait for that bus to arrive
def wait(t, bus_id):
    bus_t = (t // bus_id) * bus_id
    if bus_t < t:
        bus_t += bus_id

    return bus_t

def solve1(t, sched):
    wait_times = [(bus[1], wait(t, bus[1])) for bus in sched]
    min_wait = min(wait_times, key=lambda x: x[1])
    return min_wait[0]*(min_wait[1]-t)

### PART 2 ###

# For each bus in the schedule, we are looking for a time, t, such that
# t = -bus[0] mod bus[1]

# so our system of equations is:
# t = -sched[0][0] mod sched[0][1]
# t = -sched[1][0] mod sched[1][1]
# ...
# t = -sched[n][0] mod sched[n][1]

# The bus numbers are all prime, and hence co-prime, so we can solve 
# using the Chineese Remainder Theorem
# Theorem explained at: https://brilliant.org/wiki/chinese-remainder-theorem/
def solve2(sched):
    n = len(sched)
    N = reduce(mul, [bus[1] for bus in sched], 1)
    y = [N // bus[1] for bus in sched]
    z = [pow(y[i], -1, sched[i][1]) for i in range(n)]
    x = sum([-sched[i][0]*y[i]*z[i] for i in range(n)])

    return x % N


with open('input/input13.txt') as f:
    departure_t = int(f.readline().rstrip('\n'))
    sched = [(i, int(x)) for i, x in enumerate(f.readline().rstrip('\n').split(',')) if x != 'x']

print(sched)
print(solve1(departure_t, sched))
print(solve2(sched))
# To solve part 2:
# Based on the constraints of the puzzle:
# Any edge length of 3 must be included in all paths
# We can split a large graph into independent graphs at those edges
#
# Given array of independent graphs [G_1, G_2, ..., G_n]
# Then the total number of paths from start to finish is:
# n_paths(G_1) * n_paths(G_2) * ... * n_paths(G_n)

# Given a sequence from the puzzle input, creates a graph
def series_to_graph(s):
    g = {}
    for i in range(len(s)):
        v = []
        for j in range(i+1, i+4):
            if j >= len(s):
                break
            if s[j]-s[i] > 3:
                break
            v.append(s[j])

        g[s[i]] = v

    return g


# Given a graph, finds all paths from start to end
def find_all_paths(g, start=None, end=None, path=[]):
    if not start:
        start = min(g.keys())
    if not end:
        end = max(g.keys())

    path = path + [start]
    if start == end:
        return [path]
    if start not in g:
        return []
    paths = []
    for v in g[start]:
        if v not in path:
            newpaths = find_all_paths(g, v, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


# Given the sorted list of adapters, and a maximum distance between them
# split into slices each time two elements are the maximum distant apart
def split(s, d):
    result = []
    left = 0

    for i in range(len(s)-1):
        if s[i+1] - s[i] == d:
            result.append(s[left:i+1])
            left = i + 1

    result.append(s[left:])

    return result


def solve2(s):
    graphs = [series_to_graph(x) for x in split(s, 3)]

    # Since our graphs are independent total number of paths is
    # the product of the number of paths within each graph
    cnt = 1
    for g in graphs:
        cnt *= len(find_all_paths(g))

    return cnt


# solves part1.. expects a series of adapter joltage values
def solve1(s):
    diffs = [0, 0, 0, 0]
    for i in range(1, len(s)):
        diffs[s[i]-s[i-1]] += 1

    diffs[3] += 1

    return diffs[1]*diffs[3]


with open('input/input10.txt') as f:
    series = sorted([int(line.rstrip('\n')) for line in f])

# insert the outlet before the sorted lists of adapters
series.insert(0, 0)

print(solve1(series))
print(solve2(series))

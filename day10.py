# To solve part 2:
# Create an array of independent graphs [G_1, G_2, ..., G_n] from the input data
# Then the total number of paths from start to finish is:
# n_paths(G_1) * n_paths(G_2) * ... * n_paths(G_n)

# Given the sequence from the puzzle input, creates an array of independent graphs
def create_graphs(s):
    graphs = []
    g = {}
    split = 0
    for i in range(len(s)):
        v = []
        for j in range(i+1, i+4):
            if j >= len(s):
                break
            if s[j]-s[i] > 3:
                break
            v.append(s[j])

            if s[j]-s[i] == 3:
                split = j

        g[s[i]] = v

        if i == split:
            graphs.append(g)
            g = {}
            g[s[i]] = v

    graphs.append(g)

    return graphs

# Given a graph, finds all paths from start to finish
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def solve2(s):
    graphs = create_graphs(s)
    print(graphs)
    print(len(graphs))

    # Since our graphs are independent total number of paths is
    # the product of the number of paths within each graph
    cnt = 1
    for g in graphs:
        cnt *= len(find_all_paths(g, min(g.keys()), max(g.keys())))

    return cnt

# solves part1.. expects a series of adapter joltage values
def solve1(s):
    diffs = [0,0,0,0]
    for i in range(1, len(s)):
        diffs[s[i]-s[i-1]] += 1

    diffs[3] += 1

    print(diffs)

    return diffs[1]*diffs[3]

with open('input/input10.txt') as f:
    series = sorted([int(line.rstrip('\n')) for line in f])
series.insert(0, 0)
    
print(solve1(series))
print(solve2(series))
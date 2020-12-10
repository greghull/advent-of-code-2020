from collections import deque

# solves part1.. expects a series of adapter joltage values
def solve1(s):
    diffs = [0,0,0,0]
    for i in range(1, len(s)):
        diffs[s[i]-s[i-1]] += 1

    diffs[3] += 1

    print(diffs)

    return diffs[1]*diffs[3]

# given an array of, creates a directed graph where each node is connected to
# to others nodes with a maximum jolt difference of 3
def create_graph(s):
    graph = {}
    for i in range(len(s)):
        graph[s[i]] = []
        for j in range(i+1, i+4):
            if j >= len(s):
                break
            if s[j]-s[i] > 3:
                break
            graph[s[i]].append(s[j])

    return graph

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
    cnt = 1
    for g in graphs:
        cnt *= len(find_all_paths(g, min(g.keys()), max(g.keys())))

    return cnt

with open('input/input10.txt') as f:
    series = sorted([int(line.rstrip('\n')) for line in f])
series.insert(0, 0)
    
print(solve1(series))
print(solve2(series))
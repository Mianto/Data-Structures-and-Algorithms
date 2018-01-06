# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)


def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    global ans
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    if rank[realDestination] > rank[realSource]:
        parent[realSource] = realDestination
        lines[realDestination] += lines[realSource]
        ans = max(lines[realDestination], ans)
    else:
        parent[realDestination] = realSource
        if rank[realSource] == rank[realDestination]:
            rank[realSource] += rank[realDestination]
        lines[realSource] += lines[realDestination]
        ans = max(lines[realSource], ans)
    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

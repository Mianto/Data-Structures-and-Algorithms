# Uses python3

import sys


def reach(adj, x, visited):
    visited[x] = 1
    for i in adj[x]:
        if visited[i] == 0:
            reach(adj, i, visited)
        elif visited[i] == 1:
            visited[i] += 1


def acyclic(adj, n):
    for i in range(0, n):
        visited = [0 for _ in range(n)]
        reach(adj, i, visited)
        if visited[i] > 1:
            return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))

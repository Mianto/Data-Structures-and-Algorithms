#Uses python3

import sys


def reach(adj, x, y, visited):
    # write your code here
    visited[x] = 1
    for w in adj[x]:
        if visited[w] == 0:
            reach(adj, w, y, visited)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    visited = [0 for _ in range(n)]
    reach(adj, x, y, visited)
    print(visited[y])

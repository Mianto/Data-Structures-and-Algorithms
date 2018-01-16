# Uses python3

import sys
from queue import deque


def bipartite(adj, s):
    dist = [-1] * len(adj)
    queue = deque()
    queue.append(s)
    dist[s] = 1
    while queue:
        node = queue.popleft()
        for w in adj[node]:
            if dist[w] == -1:
                dist[w] = 1 - dist[node]
                queue.append(w)
            elif dist[w] == dist[node]:
                return 0
    return 1



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj, 0))

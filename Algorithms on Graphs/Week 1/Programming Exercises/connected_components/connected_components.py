#Uses python3

import sys


def reach(adj, x, visited):
    visited[x] = 1
    for w in adj[x]:
        if visited[w] == 0:
            reach(adj, w, visited)


def number_of_components(adj, num_vertices):
    result = 0
    visited = [0 for _ in range(num_vertices)]
    for i in range(0, num_vertices):
        if visited[i] == 0:
            reach(adj, i, visited)
            result += 1
    return result


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
    print(number_of_components(adj, n))

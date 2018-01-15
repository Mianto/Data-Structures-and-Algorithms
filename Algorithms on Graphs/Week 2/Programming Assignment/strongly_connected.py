#Uses python3

import sys

sys.setrecursionlimit(200000)


def dfs(adj, x, visited):
    '''
        finding dfs of the graph
        used on reverse graph
    '''
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            dfs(adj, i, visited)


def post_order(adj, x, visited, order):
    '''
        To return the source of the graphs
    '''
    visited[x] = True
    for i in adj[x]:
        if not visited[i]:
            post_order(adj, i, visited, order)
    order.insert(0, x)


def reverse_graph(adj):
    adj_rev = [[] for _ in range(len(adj))]
    for i in range(len(adj)):
        for x in adj[i]:
            adj_rev[x].append(i)
    return adj_rev


def number_of_strongly_connected_components(adj, n):
    order = []
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            post_order(adj, i, visited, order)

    adj_rev = reverse_graph(adj)

    visit = [False] * n
    count = 0
    while order:
        i = order.pop(0)
        if not visit[i]:
            dfs(adj_rev, i, visit)
            count += 1
    return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj, n))

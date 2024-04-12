import sys
from collections import deque

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def dfs(start):
    if not visited[start]:
        print(start, end=" ")
        visited[start] = True
        for v in graph[start]:
            dfs(v)


def bfs(start):
    if not visited[start]:
        print(start, end=" ")
        visited[start] = True
        for v in graph[start]:
            if not visited[v] and v not in q:
                q.append(v)
        if len(q) != 0:
            bfs(q.popleft())


# main
if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = dict()
    for i in range(1, N + 1):
        graph[i] = []
    visited = [False] * (N + 1)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for g in range(1, N + 1):
        graph[g].sort()
    dfs(V)
    print()
    visited = [False] * (N + 1)
    q = deque()
    bfs(V)

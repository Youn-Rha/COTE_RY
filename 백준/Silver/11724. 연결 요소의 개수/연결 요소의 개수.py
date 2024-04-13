import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def dfs(k):
    visited[k] = True
    tmp.append(k)
    for g in graph[k]:
        if not visited[g]:
            dfs(g)


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = dict()
    for i in range(N + 1):
        graph[i] = []
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False] * (N + 1)
    component = []
    tmp = []
    for i in range(1, N + 1):
        if not visited[i]:
            tmp.clear()
            dfs(i)
            if len(tmp) != 0:
                component.append(tmp.copy())
    print(len(component))

import sys


sys.setrecursionlimit(1000000)


def input():
    return sys.stdin.readline()


def dfs(k):
    for i in tree[k]:
        if not visited[i]:
            visited[i] = k
            dfs(i)


# main
if __name__ == "__main__":
    N = int(input())
    tree = {key: [] for key in range(1, N + 1)}
    for _ in range(N - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    visited = [0] * (N + 1)
    dfs(1)
    for i in range(2, N + 1):
        print(visited[i])

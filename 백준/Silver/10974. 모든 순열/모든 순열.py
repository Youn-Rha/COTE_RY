import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == N:
        print(" ".join(map(str, ans)))
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            ans[k] = i
            sol(k + 1)
            visited[i] = False


N = int(input())
lst = [i for i in range(1, N + 1)]
visited = [False] * (N + 1)
ans = [0] * N
sol(0)
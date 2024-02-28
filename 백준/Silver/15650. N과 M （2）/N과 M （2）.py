import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == M:
        print(" ".join(map(str, s)))
        return
    for i in range(s[k - 1] + 1, N + 1):
        if not visited[i]:
            visited[i] = True
            s[k] = i
            sol(k + 1)
            visited[i] = False


N, M = map(int, input().split())
s = [0] * M
visited = [False] * (N + 1)
sol(0)

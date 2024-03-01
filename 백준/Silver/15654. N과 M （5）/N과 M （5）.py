import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(N):
        if not used[i]:
            used[i] = True
            ans[k] = lst[i]
            sol(k + 1)
            used[i] = False


# main
N, M = map(int, input().split())
used = [False] * N
ans = [0] * M
lst = sorted(list(map(int, input().split())))
sol(0)

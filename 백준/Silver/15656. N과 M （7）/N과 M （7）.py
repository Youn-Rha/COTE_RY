import sys

def input():
    return sys.stdin.readline()


def sol(k):
    if k == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(N):
        ans[k] = lst[i]
        sol(k + 1)


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = [lst[0]] * M
sol(0)
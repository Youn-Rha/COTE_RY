import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == M:
        print(" ".join(map(str, lst)))
        return
    for i in range(lst[k - 1], N + 1):
        lst[k] = i
        sol(k + 1)
        # if not used[i]:
        #     used[i] = True
        #     lst[k] = i
        #     sol(k + 1)
        #     used[i] = False


# main
N, M = map(int, input().split())
#used = [False] * (N + 1)
lst = [1] * M
sol(0)

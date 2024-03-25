import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if depth == M:
        if ans.copy() not in res:
            res.append(ans.copy())
        return
    for i in range(lst.index(ans[depth - 1]), N):
        ans[depth] = lst[i]
        sol(depth + 1)


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    ans = [lst[0]] * M
    res = []
    sol(0)
    for r in res:
        print(" ".join(map(str, r)))

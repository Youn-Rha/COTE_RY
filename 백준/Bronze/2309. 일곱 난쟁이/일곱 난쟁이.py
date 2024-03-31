import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if len(res) != 0:
        return
    if depth == 7:
        if sum(ans) == 100:
            res.append(ans.copy())
            return
        else:
            return
    idx = lst.index(ans[depth - 1]) + 1
    if depth == 0:
        idx = 0
    for i in range(idx, 9):
        ans[depth] = lst[i]
        sol(depth + 1)
    return


if __name__ == "__main__":
    lst = []
    for _ in range(9):
        lst.append(int(input()))
    lst.sort()
    ans = [lst[0]] * 7
    res = []
    sol(0)
    for a in res[0]:
        print(a)

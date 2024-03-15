import sys


def input():
    return sys.stdin.readline()


def sol(k):
    mx, res = 0, 0
    for i in range(k):
        mx = max(mx, lst[i])
        res = max(res, mx - lst[i])
    if res < 0:
        print(0)
    else:
        print(res)


# main
if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    lst.reverse()
    sol(n)

import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    p = lst[0]
    max_cnt, cnt = 0, 0
    for i in range(1, N):
        if p > lst[i]:
            cnt += 1
        else:
            p = lst[i]
            cnt = 0
        max_cnt = max(max_cnt, cnt)
    print(max_cnt)

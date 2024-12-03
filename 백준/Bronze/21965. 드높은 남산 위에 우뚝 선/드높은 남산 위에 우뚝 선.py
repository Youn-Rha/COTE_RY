import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N):
        if cnt == 0 and lst[i - 1] >= lst[i]:
            cnt += 1
        if cnt == 1 and lst[i - 1] <= lst[i]:
            cnt += 1
    if cnt >= 2:
        print("NO")
    else:
        print("YES")
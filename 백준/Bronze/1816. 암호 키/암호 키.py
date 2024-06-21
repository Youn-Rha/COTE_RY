import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        flag = 0
        S = int(input())
        for i in range(2, 1_000_001):
            if S % i == 0:
                flag = 1
        if flag == 0:
            print("YES")
        else:
            print("NO")
import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    s = 0
    for i in range(1, 1 + N):
        s += i ** 3
    print(s)
import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = [0] * 10001
    for _ in range(N):
        lst[int(input())] += 1
    for i in range(1, len(lst)):
        while lst[i] != 0:
            print(i)
            lst[i] -= 1
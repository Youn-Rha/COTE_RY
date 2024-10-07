import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    round1 = list(map(int, input().split()))
    round2 = list(map(int, input().split()))
    total = 0
    for i in range(N):
        total += abs(round1[i]) + abs(round2[i])
    print(total)
import sys
from collections import deque


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = deque(input().rstrip())
    total = 0
    for i in range(len(N)):
        N.rotate()
        total += int("".join(list(N)))
    print(total)
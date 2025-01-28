import math
import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    rooms = [[0 for _ in range(2)] for _ in range(6)]
    N, K = map(int, input().split())
    for _ in range(N):
        S, Y = map(int, input().split())
        rooms[Y - 1][S] += 1
    total = 0
    for i in range(6):
        for j in range(2):
            if rooms[i][j] != 0:
                if rooms[i][j] % K == 0:
                    total += rooms[i][j] // K
                else:
                    total += rooms[i][j] // K + rooms[i][j] % K
    print(total)
import sys
from collections import deque

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    players = dict()
    for _ in range(N):
        s = input().rstrip()
        players[s[0]] = players.get(s[0], 0) + 1
    lst = list(players.items())
    lst.sort(key=lambda x: x[0])
    if max(players.values()) < 5:
        print("PREDAJA")
    else:
        for p in lst:
            if p[1] >= 5:
                print(p[0], end="")

import sys
from collections import deque


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, B = map(int, input().split())
    remains = []
    while N >= B:
        remains.append(N % B)
        N //= B
    remains.append(N % B)
    remains.reverse()
    for i in range(len(remains)):
        if remains[i] >= 10:
            remains[i] = chr(remains[i] + 55)
        else:
            remains[i] = str(remains[i])
    print("".join(remains))

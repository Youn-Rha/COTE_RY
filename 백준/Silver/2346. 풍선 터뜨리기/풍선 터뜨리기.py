import sys
from collections import deque


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    deq = deque([(a + 1, b) for a, b in enumerate(lst)])
    while len(deq) != 0:
        print(deq[0][0])
        tmp = deq[0][1]
        if tmp < 0:
            tmp += len(deq)
        deq.popleft()
        deq.rotate(-(tmp - 1))


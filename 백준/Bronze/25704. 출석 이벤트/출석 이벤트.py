import sys
from collections import deque

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    P = int(input())
    lst = [0]
    if N >= 5:
        lst.append(500)
    if N >= 10:
        lst.append(int(P * 0.1))
    if N >= 15:
        lst.append(2000)
    if N >= 20:
        lst.append(int(P * 0.25))
    P -= max(lst)
    if P <= 0:
        print(0)
    else:
        print(P)

import sys
from collections import deque
from math import factorial


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    H, M = map(int, input().split())
    answer = abs(H - M)
    if answer < 1:
        print(1)    # 거리가 0, 1 일때는 1
    else:           # 4! / (2! * 2! * (2 + 1)) 이런 느낌
        print(int(factorial(answer * 2) / (factorial(answer) ** 2 * (answer + 1))))

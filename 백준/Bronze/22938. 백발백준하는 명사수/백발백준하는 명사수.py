import math
import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    x1, y1, r1 = map(int, input().split())
    x2, y2, r2 = map(int, input().split())
    if r1 + r2 <= math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2):
        print("NO")
    else:
        print("YES")
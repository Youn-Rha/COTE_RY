import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    n = int(input())
    lst = list(map(int, input().split()))
    total = 0
    for i in range(n):
        x, y = map(int, input().split())
        if lst[i] and x < y:
            total += y - x
    print(total)
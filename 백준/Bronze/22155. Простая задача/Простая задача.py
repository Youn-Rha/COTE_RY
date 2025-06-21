import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        i, f = map(int, input().split())
        if (i <= 2 and f <= 1) or (i <= 1 and f <= 2):
            print("Yes")
        else:
            print("No")
import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, X = map(int, input().split())
    lst = list(map(int, input().split()))
    if sum(lst) % X:
        print(0)
    else:
        print(1)
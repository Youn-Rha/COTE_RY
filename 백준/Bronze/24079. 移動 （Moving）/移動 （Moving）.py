import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    X = float(input())
    Y = float(input())
    Z = float(input())
    print(1 if X + Y <= Z + .5 else 0)
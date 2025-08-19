import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    L = int(input())
    S = (L ** 2) * math.sqrt(3)
    print(S / 4)
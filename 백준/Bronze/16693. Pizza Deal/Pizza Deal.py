import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    a, p1 = map(int, input().split())
    r, p2 = map(int, input().split())
    if a / p1 < (r ** 2 * math.pi) / p2:
        print("Whole pizza")
    else:
        print("Slice of pizza")
import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    a, b, c, d, e, f = map(int, input().split())
    for x in range(-999, 1000):
        for y in range(-999, 1000):
            if a * x + b * y == c and d * x + e * y == f:
                print(x, y)
                break

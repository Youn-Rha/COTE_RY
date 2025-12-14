import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    y, c, p = map(int, input().split())
    c //= 2
    print(min(y, c, p))
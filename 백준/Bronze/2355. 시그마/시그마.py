import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()

# main
if __name__ == "__main__":
    A, B = map(int, input().split())
    print(int(.5 * (B+A) * (abs(B - A) + 1)))
import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    return gcd(b, a % b)


# main
if __name__ == "__main__":
    a, b = map(int, input().split())
    g = gcd(a, b)
    for _ in range(g):
        print("1", end="")

import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def gcd(a, b):
    if b == 0:
        return a
    if a < b:
        a, b = a, b % a
    else:
        a, b = b, a % b
    return gcd(a, b)


# main
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        a, b = map(int, input().split())
        g = gcd(a, b)
        a //= g
        b //= g
        print(a * b * g)
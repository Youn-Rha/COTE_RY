import sys

#sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, B = input().split()
    N = reversed(N)
    B = int(B)
    total = 0
    for i, n in enumerate(N):
        if ord(n) >= 65:
            total += (ord(n) - 55) * (B ** i)
        else:
            total += int(n) * (B ** i)
    print(total)
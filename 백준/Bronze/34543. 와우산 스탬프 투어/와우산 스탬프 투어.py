import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    W = int(input())
    total = 10 * N
    if N >= 3:
        total += 20
    if N == 5:
        total += 50
    if W > 1000:
        total -= 15
    print(max(0, total))
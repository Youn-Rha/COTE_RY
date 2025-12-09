import sys, itertools


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    M = int(input())
    if M <= 30:
        print(f"{M / 2:.1f}")
    elif M > 30:
        print(f"{((M - 30) * 3) / 2 + 15:.1f}")

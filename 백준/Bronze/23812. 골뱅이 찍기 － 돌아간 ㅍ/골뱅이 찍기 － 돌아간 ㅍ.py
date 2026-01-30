import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        print("@" * N, end="")
        print(" " * 3 * N, end="")
        print("@" * N)
    for _ in range(N):
        print("@" * 5 * N)
    for _ in range(N):
        print("@" * N, end="")
        print(" " * 3 * N, end="")
        print("@" * N)
    for _ in range(N):
        print("@" * 5 * N)
    for _ in range(N):
        print("@" * N, end="")
        print(" " * 3 * N, end="")
        print("@" * N)
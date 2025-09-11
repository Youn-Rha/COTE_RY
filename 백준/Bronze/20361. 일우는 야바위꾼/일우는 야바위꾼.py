import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, X, K = map(int, input().split())
    cup = [0] * N
    cup[X - 1] = 1
    for _ in range(K):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        cup[A], cup[B] = cup[B], cup[A]
    print(cup.index(1) + 1)
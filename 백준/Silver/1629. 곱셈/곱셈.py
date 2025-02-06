import sys

#sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    A, B, C = map(int, input().split())
    print(pow(A, B, C))
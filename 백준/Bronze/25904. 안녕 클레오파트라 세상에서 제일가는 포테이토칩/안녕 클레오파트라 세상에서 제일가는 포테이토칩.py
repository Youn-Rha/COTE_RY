import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, X = map(int, input().split())
    lst = list(map(int, input().split()))
    while True:
        for i in range(N):
            if X > lst[i]:
                print(i + 1)
                exit(0)
            X += 1

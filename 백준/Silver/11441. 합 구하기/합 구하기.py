import sys

# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    ary = [0] * N
    ary[0] = lst[0]
    for i in range(1, N):
        ary[i] = ary[i - 1] + lst[i]
    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        if a == 1:
            print(ary[b - 1])
        else:
            print(ary[b - 1] - ary[a - 2])

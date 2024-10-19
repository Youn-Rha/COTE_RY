import sys

# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    cnt = 0
    for _ in range(N):
        if int(input()) % 2 != 0:
            cnt += 1
    print(cnt)

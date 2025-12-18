import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 1
    for i in range(1, N):
        if lst[i] >= lst[i - 1]:
            cnt += 1
    print(cnt)
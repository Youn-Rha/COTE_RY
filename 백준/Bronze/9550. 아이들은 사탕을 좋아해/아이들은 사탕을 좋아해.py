import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        lst = list(map(int, input().split()))
        cnt = 0
        for l in lst:
            cnt += l // K
        print(cnt)
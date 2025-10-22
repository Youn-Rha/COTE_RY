import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    scholar = list(map(int, input().split()))
    N = int(input())
    total = 0
    for _ in range(N):
        B, L, S = map(float, input().split())
        if L >= 2.0 and S >= 17:
            total += scholar[int(B)]
    print(total)
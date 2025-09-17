import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    S = input().rstrip()
    cnt = 0
    for i in range(N // 2):
        if S[i] != S[N - 1 - i]:
            cnt += 1
    print(cnt)
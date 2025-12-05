import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    ralpa = list(map(int, input().split()))
    cnt = 0
    for _ in range(N - 1):
        streamer = list(map(int, input().split()))
        total = 0
        for i in range(M):
            total += abs(ralpa[i] - streamer[i])
        if total > 2000:
            cnt += 1
    if cnt >= (N - 1) / 2:
        print("YES")
    else:
        print("NO")

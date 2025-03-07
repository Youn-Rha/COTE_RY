import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, K, P = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        nocream = 0
        for j in range(K):
            if lst[i * K + j] == 0:
                nocream += 1
        if nocream < P:
            cnt += 1
    print(cnt)
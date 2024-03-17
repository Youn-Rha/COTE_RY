import sys


def input():
    return sys.stdin.readline()


def sol(k):
    dp1 = [1] * N
    dp2 = [1] * N
    # 짧은 수가 나올 때까지 cnt 증가 / 짧은 수 가 나오면 cnt 초기화
    cnt = 1
    for i in range(1, N):
        if lst[i] >= lst[i - 1]:
            cnt += 1
        else:
            cnt = 1
        dp1[i] = cnt
        
    # 거꾸로 순회하면서 탐색
    cnt = 1
    for i in range(N - 2, -1, -1):
        if lst[i] >= lst[i + 1]:
            cnt += 1
        else:
            cnt = 1
        dp2[i] = cnt
    print(max(max(dp1), max(dp2)))


if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    sol(N)

import sys


def input():
    return sys.stdin.readline()


def solve():
    for i in range(1, N + 1):
        T, P = lst[i - 1]
        if i + T - 1 <= N:  # 퇴사하는 날짜보다 이전
            # 오늘부터 했을 때 걸리는 시간 이후 일을 마치는 날에 받을 수 있는 최대 페이 저장
            dp[i + T - 1] = max(dp[i + T - 1], max(dp[:i]) + P)


# main
if __name__ == "__main__":
    N = int(input())
    lst = []
    dp = [0] * (N + 1)
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    solve()
    print(max(dp))  # 각각의 날짜마다 받을 수 있는 최대 페이가 누적되어 있음

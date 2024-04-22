import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0 for _ in range(N)] for _ in range(2)]
        lst = []
        for _ in range(2):
            lst.append(list(map(int, input().split())))

        dp[0][0], dp[1][0] = lst[0][0], lst[1][0]   # 초기 값 설정
        if N >= 3:
            dp[0][1] = dp[1][0] + lst[0][1]
            dp[1][1] = dp[0][0] + lst[1][1]

            # 00 01 02 03 04 05         02 자리에서 선택할 수 있는 선택지 11(바로 전 단계) 또는 (00 또는 10) (전전 단계)
            #                           12 자리에서 선택할 수 있는 선택지 01(바로 전 단계) 또는 (00 또는 10) (전전 단계)
            # 10 11 12 13 14 15         따라서 00 10 01 11 자리는 인덱스 오류 나므로 초기값 넣어 줘야 한다.

            for i in range(2, N):
                dp[0][i] = max(dp[1][i - 1], dp[0][i - 2], dp[1][i - 2]) + lst[0][i]
                dp[1][i] = max(dp[0][i - 1], dp[0][i - 2], dp[1][i - 2]) + lst[1][i]
        elif N == 2:
            dp[0][1] = dp[1][0] + lst[0][1]
            dp[1][1] = dp[0][0] + lst[1][1]

        print(max(dp[0][N - 1], dp[1][N - 1]))

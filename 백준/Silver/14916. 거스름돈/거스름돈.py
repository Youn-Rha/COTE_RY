import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    n = int(input())
    dp = [-1, -1, 1, -1, 2, 1] + [-1] * 99_995          # 예외 case 미리 설정 후 배열 설정 (100001개)
    for i in range(6, n + 1):
        if dp[i - 5] != -1 and dp[i - 2] != -1:         # 이전 단계에서 5원을 추가할 수 있는 경우와 2원을 추가할 수 있는 경우 비교
            dp[i] = min(dp[i - 5] + 1, dp[i - 2] + 1)
        elif dp[i - 5] == -1 and dp[i - 2] != -1:       # 이전 단계에서 2원만 추가할 수 있는 경우만 존재할 경우
            dp[i] = dp[i - 2] + 1
        else:                                           # 이전 단계에서 5원만 추가할 수 있는 경우만 존재할 경우
            dp[i] = dp[i - 5] + 1
    print(dp[n])
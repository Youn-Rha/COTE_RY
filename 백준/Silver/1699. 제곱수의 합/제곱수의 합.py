import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    dp = [float('inf')] * (N + 1)
    for i in range(1, N + 1):
        p = int(i ** 0.5)
        if p ** 2 == i:
            dp[i] = 1
        else:
            while p != 0:
                # dp[i - p ** 2] + dp[p ** 2] 원래 이렇게 생각했는데 뒤에꺼는 무조건 제곱수라 1임
                dp[i] = min(dp[i], dp[i - p ** 2] + 1) 
                p -= 1
    print(dp[N])
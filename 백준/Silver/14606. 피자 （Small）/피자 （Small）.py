import sys


def input():
    return sys.stdin.readline()


def sol(k):
    dp = [0] * 11
    dp[2] = 1
    for i in range(3, 11):
        if i % 2 == 0:
            dp[i] = dp[i // 2] + dp[i // 2] + (i // 2) ** 2
        else:
            dp[i] = dp[i // 2] + dp[i // 2 + 1] + (i // 2) * (i // 2 + 1)

    return dp[k]


if __name__ == "__main__":
    print(sol(int(input())))
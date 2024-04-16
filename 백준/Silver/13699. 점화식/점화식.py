import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    n = int(input())
    dp = [0] * (n + 1)
    dp[0] = 1
    # dp[k] = dp[0] * dp[k-1-0] + dp[1] * dp[k-1-1] ---
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    print(dp[n])
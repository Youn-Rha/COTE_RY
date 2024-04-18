import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    n = int(input())
    dp = [0, 0, 2, 3] * (n + 1)
    dp[2], dp[3] = 2, 3
    for i in range(4, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10
    print(dp[n])
import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    dp = [float('inf')] * (N + 1)
    dp[1] = 1
    for i in range(2, N + 1):
        p = int(i ** 0.5)
        if p ** 2 == i:
            dp[i] = 1
        else:
            while p != 0:
                dp[i] = min(dp[i], dp[i - p ** 2] + dp[p ** 2])
                p -= 1
    print(dp[N])
import sys


def input():
    return sys.stdin.readline()


if __name__ == "__main__":
	n = int(input())
	dp = [1, 1]
	for i in range(2, 46):
		dp.append(dp[i - 1] + dp[i - 2])
	for i in range(n):
		print(dp[int(input())])
		
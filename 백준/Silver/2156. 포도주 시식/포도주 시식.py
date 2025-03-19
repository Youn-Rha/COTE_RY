N = int(input())
wine =[]
dp = [0]*N
for i in range(N):
	wine.append(int(input()))
dp[0] = wine[0]
if N != 1:
	dp[1] = wine[0] + wine[1]
if N > 2:
	dp[2] = wine[2] + max(wine[0], wine[1])
	dp[2] = max(dp[2],dp[1])
	for i in range(3, N):
		dp[i] = wine[i] + max(wine[i-1]+dp[i-3], dp[i-2], dp[i-1]-wine[i])
		dp[i] = max(dp[i], dp[i-1])
print(max(dp))
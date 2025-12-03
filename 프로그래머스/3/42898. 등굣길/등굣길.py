def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    # 미리 웅덩이를 -1로 표시해놓기
    for py, px in puddles:
        dp[px - 1][py - 1] = -1
    # 이전 경로는 무조건 왼쪽 / 위쪽
    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            # 이전 경로가 왼쪽
            if i - 1 >= 0 and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j]
            # 이전 경로가 위쪽
            if j - 1 >= 0 and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1]
    return dp[n - 1][m - 1] % 1_000_000_007
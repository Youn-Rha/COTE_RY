import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, K = map(int, input().split())
    items = []
    used = [False] * N
    tmp = []
    for _ in range(N):
        items.append(tuple(map(int, input().split())))
    dp = [[0, []] for _ in range(K + 1)]
    for i in range(1, K + 1):
        idx = 0
        for j in range(N):
            if items[j][0] <= i and dp[i][0] < dp[i - items[j][0]][0] + items[j][1] and j not in dp[i - items[j][0]][1]:
                dp[i][0] = dp[i - items[j][0]][0] + items[j][1]
                tmp = dp[i - items[j][0]][1].copy()
                tmp.append(j)
                dp[i][1] = tmp.copy()
                tmp.clear()
    dp.sort(key=lambda x: x[0], reverse=True)

    print(dp[0][0])

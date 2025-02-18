import sys
from collections import deque

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def dfs(i, j):
        if 0 <= i < N and 0 <= j < M and ary[i][j] != 0:
            if not visited[i][j]:
                visited[i][j] = 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)


    N, M = map(int, input().split())
    ary = [[0 for _ in range(M)] for _ in range(N)]
    ice = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(M):
            ary[i][j] = lst[j]
            if lst[j] != 0:
                ice.append((i, j))
    time = 0
    while True:
        cnt = 0
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for i, j in ice:
            if ary[i][j] != 0 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
        if cnt > 1:
            print(time)
            break

        if cnt == 0:
            print(0)
            break

        # 얼마나 녹는 지 검사
        melt = [[0 for _ in range(M)] for _ in range(N)]
        for i, j in ice:
            if ary[i][j] != 0:
                if i - 1 >= 0 and ary[i - 1][j] == 0:
                    melt[i][j] += 1
                if i + 1 < N and ary[i + 1][j] == 0:
                    melt[i][j] += 1
                if j - 1 >= 0 and ary[i][j - 1] == 0:
                    melt[i][j] += 1
                if j + 1 < M and ary[i][j + 1] == 0:
                    melt[i][j] += 1
        ice = []
        # 얼음 녹이기
        for i in range(N):
            for j in range(M):
                ary[i][j] = max(ary[i][j] - melt[i][j], 0)
                if ary[i][j] != 0:
                    ice.append((i, j))

        time += 1


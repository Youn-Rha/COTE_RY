import sys
sys.setrecursionlimit(100000)



def input():
    return sys.stdin.readline()


def dfs(x, y):
    if 0 <= x < N and 0 <= y < M and bot[x][y]:
        bot[x][y] = 0
        dfs(x, y + 1)   # 상
        dfs(x, y - 1)   # 하
        dfs(x - 1, y)   # 좌
        dfs(x + 1, y)   # 우
    else:
        return


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        bot = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            X, Y = map(int, input().split())
            bot[Y][X] = 1
        result = 0
        for i in range(N):
            for j in range(M):
                if bot[i][j]:
                    dfs(i, j)
                    result += 1
        print(result)
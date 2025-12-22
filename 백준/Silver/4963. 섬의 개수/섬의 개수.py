import sys

sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    while True:
        def dfs(x, y):
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]

                if not(0 <= nx < h and 0 <= ny < w):
                    continue
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)


        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        graph = []
        # 상 하 좌 우 좌상 우상 좌하 우하
        dx = [0, 0, -1, 1, -1, 1, -1, 1]
        dy = [1, -1, 0, 0, 1, 1, -1, -1]
        visited = [[False] * w for _ in range(h)]
        for _ in range(h):
            graph.append(list(map(int, input().split())))

        cnt = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    cnt += 1
        print(cnt)
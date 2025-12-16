import sys
from collections import deque


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    maps = []
    for i in range(N):
        maps.append(list(input().rstrip()))
    visited = [[False] * N for _ in range(N)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    ans = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == '1' and not visited[i][j]:
                total = 1
                queue = deque()
                queue.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if not(0 <= nx < N and 0 <= ny < N):
                            continue
                        if maps[nx][ny] == "1" and not visited[nx][ny]:
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                            total += 1
                ans.append(total)
    ans.sort()
    print(len(ans))
    print("\n".join(map(str, ans)))
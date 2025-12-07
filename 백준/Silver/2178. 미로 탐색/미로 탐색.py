import sys
from collections import deque


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    for _ in range(N):
        graph.append(list(input().rstrip()))

    visited = [[False] * M for _ in range(N)]
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue.append((0, 0, 1))
    while queue:
        x, y, distance = queue.popleft()
        if x == N-1 and y == M-1:
            print(distance)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0 <= nx < N and 0 <= ny < M):
                continue
            if not visited[nx][ny] and graph[nx][ny] != '0':
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
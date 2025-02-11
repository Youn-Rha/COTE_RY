import sys
from collections import deque

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


def bfs(l, sx, sy, ex, ey):
    # 나이트가 이동할 수 있는 8가지 방향
    dx = [2, 2, -2, -2, 1, -1, 1, -1]
    dy = [1, -1, 1, -1, 2, 2, -2, -2]

    # 방문 여부를 저장하는 배열
    visited = [[False] * l for _ in range(l)]
    queue = deque([(sx, sy, 0)])  # (x 좌표, y 좌표, 현재 이동 횟수)
    visited[sx][sy] = True  # 시작점 방문 처리

    while queue:
        x, y, dist = queue.popleft()

        # 목적지 도착 시 거리 반환
        if x == ex and y == ey:
            return dist

        # 나이트가 이동할 수 있는 8가지 방향 탐색
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            # 체스판 내부에 있고 방문하지 않은 경우 이동
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        cnt, queue_cnt, result = 0, 0, 0
        l = int(input())
        sx, sy = map(int, input().split())
        ex, ey = map(int, input().split())
        print(bfs(l, sx, sy, ex, ey))



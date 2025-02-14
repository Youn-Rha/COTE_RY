import sys, itertools
import collections

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


def bfs(x, y, dist):
    if 0 <= x < N and 0 <= y < M and tomato[x][y] == 0:
        tomato[x][y] = 1
        deque.append((x, y, dist + 1))

# main
if __name__ == "__main__":
    M, N = map(int, input().split())
    tomato = []
    for _ in range(N):
        tomato.append(list(map(int, input().split())))
    deque = collections.deque()
    dist = 0
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 1:
                deque.append((i, j, dist))
    while deque:
        x, y, dist = deque.popleft()
        bfs(x + 1, y, dist)
        bfs(x - 1, y, dist)
        bfs(x, y + 1, dist)
        bfs(x, y - 1, dist)
    for i in range(N):
        for j in range(M):
            if tomato[i][j] == 0:
                print(-1)
                exit(0)
    print(dist)

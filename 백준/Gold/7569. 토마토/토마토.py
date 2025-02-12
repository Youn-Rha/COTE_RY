import sys
from collections import deque
sys.setrecursionlimit(100000)



def input():
    return sys.stdin.readline()


def bfs(z, y, x, dist):
    if 0 <= x < M and 0 <= y < N and 0 <= z < H:
        if tomato[z][y][x] == 0:
            tomato[z][y][x] = 1
            deque.append((z, y, x, dist + 1))


# main
if __name__ == "__main__":
    M, N, H = map(int, input().split())
    tomato = []
    for i in range(H):
        toma = []
        for j in range(N):
            toma.append(list(map(int, input().split())))
        tomato.append(toma)
    deque = deque()
    x, y, z, dist = 0, 0, 0, 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if tomato[z][y][x] == 1:
                    deque.append((z, y, x, 0))
    while deque:
        z, y, x, dist = deque.popleft()
        bfs(z + 1, y, x, dist) # 앞
        bfs(z - 1, y, x, dist) # 뒤
        bfs(z, y, x + 1, dist) # 우
        bfs(z, y, x - 1, dist) # 좌
        bfs(z, y + 1, x, dist) # 하
        bfs(z, y - 1, x, dist) # 상
    for z in range(H):
        for y in range(N):
            if 0 in tomato[z][y]:
                print(-1)
                exit(0)
    print(dist)


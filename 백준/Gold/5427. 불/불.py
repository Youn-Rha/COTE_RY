import collections
import sys
from collections import deque
sys.setrecursionlimit(100000)



def input():
    return sys.stdin.readline()


def bfs_fire(x, y, dist):
    if 0 <= x < h and 0 <= y < w and not building[x][y] == "#":
        if fire[x][y] == float('inf'):
            fire[x][y] = dist + 1
            deque_fire.append((x, y, dist + 1))

def bfs_escape(x, y, dist):
    global flag
    if 0 <= x < h and 0 <= y < w and building[x][y] == ".":
        building[x][y] = "@"
        deque_escape.append((x, y, dist + 1))
    elif x == -1 or y == -1 or x == h or y == w:    # 종료 조건
        flag = True

# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        deque_fire = deque()
        deque_escape = deque()
        x, y, dist_fire, dist_escape = 0, 0, 0, 0
        flag = False
        w, h = map(int, input().split())
        building = [["" for _ in range(w)] for _ in range(h)]
        fire = [[float('inf') for _ in range(w)] for _ in range(h)]
        for i in range(h):
            s = input().rstrip()
            for j in range(w):
                building[i][j] = s[j]
                if s[j] == "*":
                    deque_fire.append((i, j, dist_fire))
                    fire[i][j] = -1
                if s[j] == "@":
                    deque_escape.append((i, j, dist_escape))
        while deque_fire:                           # 불 먼저 이동
            x, y, dist_fire = deque_fire.popleft()
            bfs_fire(x + 1, y, dist_fire)
            bfs_fire(x - 1, y, dist_fire)
            bfs_fire(x, y + 1, dist_fire)
            bfs_fire(x, y - 1, dist_fire)
        while deque_escape:                         # 사람 탈출 이동
            x, y, dist_escape = deque_escape.popleft()
            bfs_escape(x + 1, y, dist_escape)
            bfs_escape(x - 1, y, dist_escape)
            bfs_escape(x, y + 1, dist_escape)
            bfs_escape(x, y - 1, dist_escape)
            if flag and fire[x][y] > dist_escape:   # 종료 조건
                break
            else:
                flag = False
        if flag:
            print(dist_escape + 1)
        else:
            print("IMPOSSIBLE")

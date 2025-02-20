import sys
from collections import deque
import queue

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def bfs(x, dist):
        if 0 <= x <= 100_000 and not visited[x]:
            visited[x] = True
            deque.append((x, dist + 1))


    N, K = map(int, input().split())
    deque = deque()
    visited = [False] * 100_001
    for i in (N - 1, N + 1, N * 2):
        if 0 <= i <= 100_000:
            deque.append((i, 1))
    if N == K:
        print(0)
    else:
        while True:
            x, dist = deque.popleft()
            if x == K:
                print(dist)
                break
            for i in (x - 1, x + 1, x * 2):
                bfs(i, dist)
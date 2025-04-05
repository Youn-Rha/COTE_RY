import sys
from collections import deque

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


def bfs(x, dist):
    if 0 <= x <= 100_000 and not visited[x]:
        visited[x] = True
        deque.append((x, dist + 1))


# main
if __name__ == "__main__":
    N, K = map(int, input().split())
    deque = deque()
    visited = [False] * 100_001
    if N * 2 <= 100_000:
        deque.append((N * 2, 0))
    if N - 1 >= 0:
        deque.append((N - 1, 1))
    if N + 1 <= 100_000:
        deque.append((N + 1, 1))

    if N == K:
        print(0)
    else:
        while True:
            x, dist = deque.popleft()
            if x == K:
                print(dist)
                break
            bfs(x * 2, dist - 1)    # 0초 후
            bfs(x - 1, dist)
            bfs(x + 1, dist)
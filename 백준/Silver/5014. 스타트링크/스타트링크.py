import sys
from collections import deque



def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def bfs(x, button):
        if 1 <= x <= F and not visited[x]:
            visited[x] = True
            deque.append((x, button + 1))
    F, S, G, U, D = map(int, input().split())
    deque = deque()
    visited = [False] * (F + 1)
    flag = False
    deque.append((S, 0))
    while deque:
        x, button = deque.popleft()
        if x == G:
            flag = True
            print(button)
            break
        bfs(x + U, button)
        bfs(x - D, button)
    if not flag:
        print("use the stairs")
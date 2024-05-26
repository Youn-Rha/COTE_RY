import sys
from collections import deque


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, X = map(int, input().split())
    tmp = list(map(int, input().split()))
    lst = [0] * N
    lst[0] = tmp[0]
    for i in range(1, N):
        lst[i] = lst[i - 1] + tmp[i]
    visited_max = 0
    cnt = 1
    for i in range(X - 1, N):    # 5, 2 -> (0~1) (1~2) (2~3) (3~4) / 7, 5 -> (0, 4) (1, 5) (2, 6)
        if i - X != -1:
            if visited_max == lst[i] - lst[i - X]:
                cnt += 1
            elif visited_max < lst[i] - lst[i - X]:
                cnt = 1
            visited_max = max(visited_max, lst[i] - lst[i - X])
        else:
            if visited_max == lst[i]:
                cnt += 1
            elif visited_max < lst[i] - lst[i - X]:
                cnt = 1
            visited_max = max(visited_max, lst[i])
    if visited_max == 0:
        print("SAD")
    else:
        print(visited_max)
        print(cnt)
import sys
from collections import deque

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def divide(x, y, n):
        color = paper[x][y]
        # 종이 하나의 색깔 확인
        for i in range(x, x + n):
            for j in range(y, y + n):
                # 색깔 다르면 9등분으로 쪼개기
                if color != paper[i][j]:
                    for a in range(3):
                        for b in range(3):
                            divide(x + (n // 3) * a, y + (n // 3) * b, n // 3)
                    return
        result[color] += 1

    N = int(input())
    paper = []
    for _ in range(N):
        paper.append(list(map(int, input().split())))
    result = [0, 0, 0]
    divide(0, 0, N)
    print(result[-1])
    print(result[0])
    print(result[1])

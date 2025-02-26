import sys

def input():
    return sys.stdin.readline().strip()

def dfs(arr, x, y, size):
    if size == 3:
        pattern = ["***", "* *", "***"]
        for dx in range(3):
            for dy in range(3):
                arr[x + dx][y + dy] = pattern[dx][dy]
        return

    div = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue  # 가운데 부분을 공백 유지
            dfs(arr, x + i * div, y + j * div, div)

# 입력 받기
N = int(input())

# N x N 배열을 공백(' ')으로 초기화
canvas = [[' ' for _ in range(N)] for _ in range(N)]

# 별 패턴 채우기
dfs(canvas, 0, 0, N)

# 출력
for row in canvas:
    print(''.join(row))

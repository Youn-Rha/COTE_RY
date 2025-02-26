import sys

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def draw_stars(arr, x, y, size):
        if size == 1:
            arr[x][y] = '*'
            return

        div = size // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    # 가운데는 공백
                    continue
                draw_stars(arr, x + i * div, y + j * div, div)

    N = int(input())
    canvas = [[' ' for _ in range(N)] for _ in range(N)]
    draw_stars(canvas, 0, 0, N)
    for row in canvas:
        print(''.join(row))
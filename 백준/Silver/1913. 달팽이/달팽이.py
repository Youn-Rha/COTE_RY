import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    X = int(input())
    ans = [[0] * N for _ in range(N)]
    dx = [0, 1, 0, -1, 0]
    dy = [1, 0, -1, 0, 1]
    repeat = [1, 1, 2, 2, 2]
    # u r d d l l u u / u r r r d d d d l l l l u u u u /u r r r r r d d d d d d
    x, y = N // 2, N // 2
    ans_x, ans_y = x, y
    ans[y][x] = 1
    i = 2
    while i <= N ** 2:
        for j in range(len(repeat)):
            for _ in range(repeat[j]):
                x += dx[j]
                y -= dy[j]
                ans[y][x] = i
                if i == X:
                    ans_x, ans_y = x, y
                i += 1
        for k in range(4):
            repeat[k + 1] += 2
    for i in range(N):
        print(" ".join(map(str, ans[i])))
    print(ans_y + 1, ans_x + 1)
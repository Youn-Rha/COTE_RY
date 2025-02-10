import sys, math

sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()


def dfs1(i, j, color):
    if 0 <= i < N and 0 <= j < N and pic1[i][j] == color and not visited1[i][j]:
        visited1[i][j] = True
        dfs1(i+1, j, color)
        dfs1(i-1, j, color)
        dfs1(i, j+1, color)
        dfs1(i, j-1, color)


def dfs2(i, j, color):
    if 0 <= i < N and 0 <= j < N and pic2[i][j] == color and not visited2[i][j]:
        visited2[i][j] = True
        dfs2(i+1, j, color)
        dfs2(i-1, j, color)
        dfs2(i, j+1, color)
        dfs2(i, j-1, color)

# main
if __name__ == "__main__":
    N = int(input())
    # 1 - 적록색약 아닌 사람 / 2 - 적록색약인 사람
    pic1 = []
    pic2 = []
    cnt1, cnt2 = 0, 0
    visited1 = [[False] * N for _ in range(N)]
    visited2 = [[False] * N for _ in range(N)]
    for _ in range(N):
        s = input()
        pic1.append(s)
        # 그림 넣을 때 미리 G를 R로 바꿔줌
        pic2.append(s.replace("G", "R"))
    for i in range(N):
        for j in range(N):
            # 적록색약 아닌 사람
            if not visited1[i][j]:
                dfs1(i, j, pic1[i][j])
                cnt1 += 1
            # 적록색약인 사람
            if not visited2[i][j]:
                dfs2(i, j, pic2[i][j])
                cnt2 += 1
    print(cnt1, cnt2)
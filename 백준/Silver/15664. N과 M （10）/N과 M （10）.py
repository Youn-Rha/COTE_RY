import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if depth == M:
        if ans not in res:                          # 중복되는 수열 제거
            res.append(ans.copy())
            return
        else:
            return
    idx = lst.index(ans[depth - 1]) + 1             # 비내림차순을
    if depth == 0:                                  # 위한 인덱스 값
        idx = 0                                     # 설정
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            ans[depth] = lst[i]
            sol(depth + 1)
            visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = sorted(list(map(int, input().split())))
    ans = [lst[0]] * M
    res = []
    visited = [False] * N                           # 중복 제거
    sol(0)
    for r in res:
        print(" ".join(map(str, r)))

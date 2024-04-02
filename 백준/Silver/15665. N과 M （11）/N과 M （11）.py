import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if depth == M:
        print(" ".join(map(str, ans)))
        return
    for i in range(len(lst)):               # 중복 제거로 줄어든 원소의 개수
        ans[depth] = lst[i]
        sol(depth + 1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = set(map(int, input().split()))    # 중복되는 원소 제거
    lst = sorted(list(lst))
    ans = [0] * M
    sol(0)
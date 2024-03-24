import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if depth == 6:
        print(" ".join(map(str, ans)))
        return
    idx = lst.index(ans[depth - 1]) + 1         # 중복 제거
    if depth == 0:                              
        idx = 0
    for i in range(idx, len(lst)):
        ans[depth] = lst[i]
        sol(depth + 1)


# main
if __name__ == "__main__":
    lst = []
    while True:
        lst = list(map(int, input().split()))
        if lst[0] == 0:
            break
        lst.pop(0)                              # 배열 길이 나타내는 수 삭제
        ans = [lst[0]] * 6
        sol(0)
        print()
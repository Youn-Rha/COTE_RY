import sys


def input():
    return sys.stdin.readline()


def sol(m):
    if m == k:
        ans_lst.add("".join(map(str, ans)))     # 문자열로 변환해서 처리
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            ans[m] = lst[i]
            sol(m + 1)
            visited[i] = False


# main
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    visited = [False] * n                       # 서로 다른 카드를 뽑음
    lst = []
    for i in range(n):
        lst.append(int(input()))
    ans = [lst[0]] * k
    ans_lst = set()                             # 중복되는 경우 처리 / 개수 찾는 문젝기 때문에 순서 상관x
    sol(0)
    print(len(ans_lst))
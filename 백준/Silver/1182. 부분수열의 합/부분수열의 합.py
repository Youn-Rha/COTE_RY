import sys


def input():
    return sys.stdin.readline()


def sol(depth, start):                      # start = 중복 제거를 위한 이전 원소 인덱스 기억
    if depth == n:
        res.append(sum(ans))
        return
    for i in range(start, N):
        ans[depth] = lst[i]
        sol(depth + 1, i + 1)


# main
if __name__ == "__main__":
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    for n in range(1, N + 1):               # n = 부분집합의 개수
        ans = [lst[0]] * n
        res = []                            # 각각의 부분집합의 합을 가지고 있는 배열
        sol(0, 0)
        cnt += res.count(S)                 # 합이 S인 개수 cnt 에 추가
    print(cnt)
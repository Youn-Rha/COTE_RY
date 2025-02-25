import sys

sys.setrecursionlimit(10000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def sol(k):
        if k == N:  # 종료 조건
            cnt = 0
            for l in lst:
                if l[0] <= 0:
                    cnt += 1
            result.append(cnt)
            return
        if lst[k][0] <= 0:  # 지금 손에 들고 있는 게 깨져 있으면
            sol(k + 1)
            return
        hit = False
        for i in range(N):
            if lst[i][0] > 0 and i != k and lst[k][0] > 0:
                hit = True
                lst[i][0] -= lst[k][1]
                lst[k][0] -= lst[i][1]
                sol(k + 1)
                # 다음 depth 보내고 원상복구
                lst[i][0] += lst[k][1]
                lst[k][0] += lst[i][1]
        # 하나도 못치는 경우에만 다음 depth
        if not hit:
            sol(k + 1)


    N = int(input())
    lst = []
    broken = [False] * N
    result = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    sol(0)
    print(max(result))
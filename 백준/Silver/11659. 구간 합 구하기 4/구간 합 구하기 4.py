import sys


def input():
    return sys.stdin.readline()


def sol():
    return


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    # 누적합 구하기
    for i in range(1, N):
        lst[i] += lst[i - 1]

    for _ in range(M):
        a, b = map(int, input().split())
        # a = 1 일때는 인덱스 오류가 나므로 예외 처리
        if a == 1:
            print(lst[b - 1])
        # 2 4 이면 lst[4] - lst[1]을 해줘야 2, 3, 4 누적합
        else:
            print(lst[b - 1] - lst[a - 2])

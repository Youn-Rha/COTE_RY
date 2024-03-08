import sys


def input():
    return sys.stdin.readline()


def hanoi(n, start, end):
    point = 6 - start - end     # 자리가 1, 2, 3 세가지 이므로 항상 합이 6임
    if n == 0:
        return
    hanoi(n - 1, start, point)  # n-1개를 1에서 2로
    print(start, end)           # 큰 원판을 1에서 3으로
    hanoi(n - 1, point, end)    # n-1개를 2에서 3으로


# main
if __name__ == "__main__":
    n = int(input())
    # a(n) = 2a(n-1)+1 -> a(n)+1 = 2(a(n-1)+1) - > a(n) = 2^n - 1
    print(2 ** n - 1)
    if n <= 20:
        hanoi(n, 1, 3)

import sys


def input():
    return sys.stdin.readline()


def sol():
    dp = [0.0] * n
    dp[0] = lst[0]
    # dp 배열에는 누적곱들이 들어가고 곱해졌을 때 작아지는 경우 그 위치부터 다시 누적곱 시작
    for i in range(1, n):
        dp[i] = max(lst[i] * dp[i - 1], lst[i])

    print(f'{max(dp):.3f}')


# main
if __name__ == "__main__":
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(float(input()))
    sol()
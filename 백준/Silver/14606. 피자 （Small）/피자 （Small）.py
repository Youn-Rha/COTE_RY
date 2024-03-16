import sys


def input():
    return sys.stdin.readline()


def sol(k):
    dp = [0] * 11
    dp[2] = 1
    for i in range(3, 11):
        # 임의의 수를 쪼갰을 때 각각의 곱이 가장 큰 경우는 딱 반으로 나눴을 때임
        # (6의 경우 3 3 일 때, 9의 경우 4 5 일 때)
        if i % 2 == 0:
            dp[i] = dp[i // 2] + dp[i // 2] + (i // 2) ** 2
        else:
            dp[i] = dp[i // 2] + dp[i // 2 + 1] + (i // 2) * (i // 2 + 1)

    return dp[k]


if __name__ == "__main__":
    print(sol(int(input())))

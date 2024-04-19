import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    A = input().rstrip()
    B = input().rstrip()
    alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2,
             2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
    n = len(A)
    n *= 2
    m = int(n * (n + 1) / 2) - 1
    dp = [0] * m
    idx = 0
    for a, b in zip(A, B):
        dp[idx] = alpha[ord(a) - ord('A')]
        dp[idx + 1] = alpha[ord(b) - ord('A')]
        idx += 2
    cnt = 0
    n -= 1
    for i in range(m - 2):
        if cnt == n:
            n -= 1
            cnt = 0
            continue
        dp[idx] = (dp[i] + dp[i + 1]) % 10
        idx += 1
        cnt += 1
    print("".join(map(str, dp[-2:])))


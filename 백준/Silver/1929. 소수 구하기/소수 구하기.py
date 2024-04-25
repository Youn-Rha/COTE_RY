import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


def sieve(n):               # 에라토스테네스의 체
    lst = [True] * (n + 1)
    lst[0], lst[1] = False, False
    p = 2
    while p * p <= n:
        lst[p*p::p] = [False] * ((n - p * p) // p + 1)
        p += 1
    return lst


# main
if __name__ == "__main__":
    M, N = map(int, input().split())
    prime = sieve(N)
    for i in range(M, N + 1):
        if prime[i]:
            print(i)

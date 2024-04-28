import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def primeSieve(N):
    prime = [True] * (N + 1)
    prime[0], prime[1] = False, False
    p = 2
    while p * p <= N + 1:
        prime[p * p::p] = [False] * ((N - p * p) // p + 1)
        p += 1
    return prime


# main
if __name__ == "__main__":
    while True:
        N = int(input())
        if N == 0:
            break
        prime = primeSieve(2 * N + 1)
        ans = []
        for i in range(N + 1, 2 * N + 1):
            if prime[i]:
                ans.append(i)
        print(len(ans))

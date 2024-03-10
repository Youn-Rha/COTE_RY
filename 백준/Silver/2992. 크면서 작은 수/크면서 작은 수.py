import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == len(X):
        num.append(int("".join(ans)))
        return
    for i in range(len(X)):
        if not visited[i]:
            visited[i] = True
            ans[k] = X[i]
            sol(k + 1)
            visited[i] = False


if __name__ == "__main__":
    X = input().strip()
    ans = [""] * len(X)
    visited = [False] * len(X)
    num = []
    sol(0)
    num.sort(reverse=True)
    idx = num.index(int(X))
    if idx != 0:
        print(num[idx - 1])
    else:
        print(0)

import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == len(S):
        print("".join(ans))
        return
    for i in range(len(S)):
        if not used[i]:
            used[i] = True
            ans[k] = S[i]
            sol(k + 1)
            used[i] = False


# main
if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        S = input().strip()
        ans = [""] * len(S)
        used = [False] * len(S)
        print(f"Case # {i + 1}:")
        sol(0)

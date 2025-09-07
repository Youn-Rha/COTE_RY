import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = list(input().rstrip())
    T = list(input().rstrip())
    for i in range(len(T) - 1, len(S) - 1, -1):
        if T[i] == "A":
            T.pop()
        elif T[i] == "B":
            T.pop()
            T = T[::-1]
    if S == T:
        print(1)
    else:
        print(0)

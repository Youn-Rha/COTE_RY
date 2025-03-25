import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    E, S, M = map(int, input().split())
    if E == 15:
        E = 0
    if S == 28:
        S = 0
    if M == 19:
        M = 0
    for i in range(1, 15 * 28 * 19 + 1):
        if i % 15 == E and i % 28 == S and i % 19 == M:
            print(i)
            break
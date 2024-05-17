import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = sorted([N, M])
    rect = []
    for i in range(N):
        rect.append(list(input().rstrip()))

    S = lst[0]
    while True:
        flag = 0
        for i in range(N - S + 1):
            for j in range(M - S + 1):
                if rect[i][j] == rect[i + S - 1][j] == rect[i][j + S - 1] == rect[i + S - 1][j + S - 1]:
                    flag = 1
                    break

        if flag == 1:
            break
        S -= 1

    print(S ** 2)
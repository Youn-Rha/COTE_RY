import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst_M = [None] * N
    lst_P = [None] * N
    for _ in range(M):
        a, b, c = input().split()
        a, c = int(a), int(c)
        if b == 'P':
            lst_P[a - 1] = c
        else:
            lst_M[a - 1] = c
    min_num, max_num = 0, 0
    for i in range(N):
        if lst_P[i] == 1 and lst_M[i] == 0:
            min_num += 1
            max_num += 1
        elif lst_M[i] != 1 and lst_P[i] != 0:
            max_num += 1
    print(min_num, max_num)
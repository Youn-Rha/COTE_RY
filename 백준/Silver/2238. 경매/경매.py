import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    U, N = map(int, input().split())
    lst = []
    cnt = {}
    for i in range(N):
        S, P = input().split()
        P = int(P)
        cnt[P] = cnt.get(P, 0) + 1
        lst.append([S, P, i])
    for i in range(N):
        lst[i].append(cnt[lst[i][1]])
    lst.sort(key=lambda x: (x[3], x[1], x[2]))
    print(lst[0][0], lst[0][1])
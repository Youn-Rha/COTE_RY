import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def findCenter(x, y):
    global cnt
    lst = []
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            lst.append(images[i][j])
    lst.sort()
    if lst[4] >= T:
        cnt += 1


# main
if __name__ == "__main__":
    R, C = map(int, input().split())
    images = []
    for _ in range(R):
        images.append(list(map(int, input().split())))
    T = int(input())
    cnt = 0
    for i in range(R - 2):
        for j in range(C - 2):
            findCenter(i, j)
    print(cnt)
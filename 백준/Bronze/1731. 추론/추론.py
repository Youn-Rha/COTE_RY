import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(int(input()))

    if lst[2] - lst[1] == lst[1] - lst[0]:
        print(lst[-1] + lst[2] - lst[1])
    else:
        print(lst[-1] * (lst[2] // lst[1]))
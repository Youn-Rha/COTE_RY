import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(input().split())
    rank = {"B": 1, "S": 2, "G": 3, "P": 4, "D": 5}
    new_lst = sorted(lst, key=lambda x: (rank[x[0]], -int(x[1:])))
    if lst == new_lst:
        print("OK")
    else:
        print("KO")
        for i in range(N):
            if lst[i] != new_lst[i]:
                print(new_lst[i], end=" ")
import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        lst = list(map(int, input().split()))
        dic = dict()
        flag = 0
        winner = "SYJKGW"
        for n in range(1, len(lst)):
            dic[lst[n]] = dic.get(lst[n], 0) + 1
        for a, y in dic.items():
            if y > (len(lst) - 1) / 2:
                flag = 1
                winner = str(a)
        print(winner)

import sys, math


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def self_num():
    def cal(n):
        lst = list(map(int, str(n)))
        return n + sum(lst)
    for i in range(1, 10001):
        p = i
        while cal(p) <= 10000:
            p = cal(p)
            if num[p]:
                num[p] = False


# main
if __name__ == "__main__":
    num = [True] * 10001
    self_num()
    for i in range(1, 10001):
        if num[i]:
            print(i)

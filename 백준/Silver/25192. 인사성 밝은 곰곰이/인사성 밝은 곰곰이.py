import sys


def input():
    return sys.stdin.readline()


def solve():
    return


# main
if __name__ == "__main__":
    N = int(input())
    p = dict()
    tmp = set()
    flag = 0
    input()
    for _ in range(N - 1):
        s = input().rstrip()
        if s == "ENTER":
            p[flag] = tmp.copy()
            flag += 1
            tmp.clear()
        else:
            tmp.add(s)
    p[flag] = tmp.copy()
    total = 0
    for v in list(p.values()):
        total += len(v)
    print(total)

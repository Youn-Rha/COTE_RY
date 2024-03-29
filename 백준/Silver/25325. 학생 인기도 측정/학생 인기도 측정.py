import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    return


# main
if __name__ == "__main__":
    n = int(input())
    students = input().split()
    dic_std = dict()
    for student in students:
        dic_std[student] = 0
    for i in range(n):
        like_std = input().split()
        for l in like_std:
            dic_std[l] += 1
    ans = sorted(list(dic_std.items()), key=lambda x: (-int(x[1]), x[0]))
    for a in ans:
        print(" ".join(map(str, a)))
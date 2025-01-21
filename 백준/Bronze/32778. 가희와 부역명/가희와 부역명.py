import math
import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    s = input()
    lst = s.split()
    index = len(lst)
    for i, l in enumerate(lst):
        if "(" in l:
            index = i
            break
    s = s.replace("(", "")
    s = s.replace(")", "")
    lst = s.split()
    print(" ".join(map(str, lst[:index])))
    if len(lst) == index:
        print("-")
    else:
        print(" ".join(map(str, lst[index:])))
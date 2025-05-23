import sys, math


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    lst = [input().rstrip(), input().rstrip()]
    x, y = abs(ord(lst[0][0]) - ord(lst[1][0])), abs(int(lst[0][1]) - int(lst[1][1]))
    if x > y:
        x, y = y, x
    print(x, y)
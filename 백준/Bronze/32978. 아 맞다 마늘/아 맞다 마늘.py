import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst1 = set(input().split())
    lst2 = set(input().split())
    print((lst1 - lst2).pop())
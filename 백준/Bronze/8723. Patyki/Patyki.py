import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()



# main
if __name__ == "__main__":
    lst = list(map(int, input().split()))
    lst.sort()
    if lst[0] == lst[1] == lst[2]:
        print(2)
    elif lst[0] ** 2 + lst[1] ** 2 == lst[2] ** 2:
        print(1)
    else:
        print(0)
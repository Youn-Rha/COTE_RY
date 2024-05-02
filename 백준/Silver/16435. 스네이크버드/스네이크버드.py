import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()



# main
if __name__ == "__main__":
    N, L = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()
    for i in range(N):
        if L >= lst[i]:
            L += 1
    print(L)
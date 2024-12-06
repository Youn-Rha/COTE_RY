import sys, math

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline().rstrip()


# main
if __name__ == "__main__":
    lst = [0 for _ in range(10)]
    A = int(input())
    B = int(input())
    C = int(input())
    for i in str(A * B * C):
        lst[int(i)] += 1
    for i in range(10):
        print(lst[i])
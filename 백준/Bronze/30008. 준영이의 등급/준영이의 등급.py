import sys
from copy import deepcopy

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    for l in lst:
        grade = l * 100 // N
        if 0 <= grade <= 4:
            print(1, end=" ")
        elif 4 < grade <= 11:
            print(2, end=" ")
        elif 11 < grade <= 23:
            print(3, end=" ")
        elif 23 < grade <= 40:
            print(4, end=" ")
        elif 40 < grade <= 60:
            print(5, end=" ")
        elif 60 < grade <= 77:
            print(6, end=" ")
        elif 77 < grade <= 89:
            print(7, end=" ")
        elif 89 < grade <= 96:
            print(8, end=" ")
        elif 96 < grade <= 100:
            print(9, end=" ")

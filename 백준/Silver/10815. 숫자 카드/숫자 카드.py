import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def binarySearchEQ(numbers, target):
    def recur(fromIndex, toIndex):
        if fromIndex > toIndex:
            return -1
        mid = int((fromIndex + toIndex) / 2)
        if numbers[mid] < target:
            return recur(mid + 1, toIndex)
        elif numbers[mid] > target:
            return recur(fromIndex, mid - 1)
        else:
            return mid

    return recur(0, len(numbers) - 1)

# main
if __name__ == "__main__":
    N = int(input())
    sg = sorted(list(map(int, input().split())))
    M = int(input())
    test = list(map(int, input().split()))
    sol = []
    for t in test:
        if binarySearchEQ(sg, t) == -1:
            sol.append(0)
        else:
            sol.append(1)
    print(" ".join(map(str, sol)))

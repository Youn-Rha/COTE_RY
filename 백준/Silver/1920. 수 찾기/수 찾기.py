import sys

sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def binarySearchEQ(numbers, target):
    def recur(fromIndex, toIndex):
        if fromIndex > toIndex: return -1

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
    num = list(map(int, input().split()))
    num.sort()
    M = int(input())
    sol = list(map(int, input().split()))
    for i in range(M):
        if binarySearchEQ(num, sol[i]) == -1:
            print(0)
        else:
            print(1)

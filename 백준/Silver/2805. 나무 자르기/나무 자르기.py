import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    left = 0
    right = max(lst)
    while left <= right:
        mid = (left + right) // 2
        tree = 0
        for l in lst:
            if l - mid > 0:
                tree += l - mid
                if tree >= M:
                    break
        if tree < M:
            right = mid - 1
        else:
            left = mid + 1
    print(right)
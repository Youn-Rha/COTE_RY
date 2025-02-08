import sys


def input():
    return sys.stdin.readline()


def hanoi(num, start, end):
    if num == 1:
        print(start, end)
        return
    else:
        hanoi(num-1, start, 6-start-end)
        print(start, end)
        hanoi(num-1, 6-start-end, end)


# main
if __name__ == "__main__":
    K = int(input())
    print(2 ** K - 1)
    hanoi(K, 1, 3)
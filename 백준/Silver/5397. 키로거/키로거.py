import collections
import sys


# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        case = input().rstrip()
        left = collections.deque()
        right = collections.deque()
        for c in case:
            if c == "<":
                if len(left) >= 1:
                    right.appendleft(left.pop())
            elif c == ">":
                if len(right) >= 1:
                    left.append(right.popleft())
            elif c == "-":
                if len(left) >= 1:
                    left.pop()
            else:
                left.append(c)
        print("".join(map(str, left)) + "".join(map(str, right)))
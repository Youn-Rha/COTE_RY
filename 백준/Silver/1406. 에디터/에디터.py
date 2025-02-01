import sys, itertools
import collections

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    left = collections.deque((input().rstrip()))
    right = collections.deque()
    n = int(input())
    for _ in range(n):
        w = "".join(input().split())
        if w[0] == 'L':
            if len(left) >= 1:
                right.appendleft(left.pop())
        elif w[0] == 'D':
            if len(right) >= 1:
                left.append(right.popleft())
        elif w[0] == 'B':
            if len(left) >= 1:
                left.pop()
        elif w[0] == 'P':
            left.append(w[1])

    print("".join(left) + "".join(right))

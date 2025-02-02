import sys, itertools
import collections

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    cnt = 0
    for _ in range(N):
        S = input().rstrip()
        stack = []
        for s in S:
            if len(stack) != 0 and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
        if len(stack) == 0:
            cnt += 1
    print(cnt)
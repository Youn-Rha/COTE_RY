import sys, itertools
import collections

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    S = input().rstrip()
    stack = []
    cnt = 0
    for i, s in enumerate(S):
        if stack and s == ")":
            stack.pop()
            if S[i - 1] == "(":
                cnt += len(stack)
            else:
                cnt += 1
        else:
            stack.append(s)
    print(cnt)
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
            # 레이저 부분
            if S[i - 1] == "(":
                cnt += len(stack)
            # 막대기 끄트머리 부분
            else:
                cnt += 1
        else:
            stack.append(s)
    print(cnt)
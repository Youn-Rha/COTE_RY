import sys, itertools
import collections

# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    # left ^ cursor ^ right
    left = collections.deque(" " + " ".join(input().rstrip()) + " ")
    right = collections.deque()
    # abcd -> _a_b_c_d_ -> 중간에 공백으로 커서 위치 판별
    n = int(input())
    for _ in range(n):
        w = "".join(input().split())
        if w[0] == 'L':
            if len(left) >= 2:
                right.appendleft(left.pop())
                right.appendleft(left.pop())
        elif w[0] == 'D':
            if len(right) >= 2:
                left.append(right.popleft())
                left.append(right.popleft())
        elif w[0] == 'B':
            if len(left) >= 2:
                left.pop()
                left.pop()
        elif w[0] == 'P':
            left.append(w[1])
            left.append(" ")

    print("".join(left).replace(" ", "") + "".join(right).replace(" ", ""))

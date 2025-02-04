import queue
import sys
def input():
    return sys.stdin.readline().rstrip()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    stack = []
    result = [0] * N
    for i, l in enumerate(lst):
        while stack:
            if stack[-1][1] < l:                # 스택의 맨 마지막 값이 현재 값보다 작으면
                stack.pop()                     # 무시해도 되니까 pop
            else:                               # 현재 값보다 크면
                result[i] = stack[-1][0] + 1    # 그 값의 인덱스 추가(인덱스가 1부터 시작하므로 +1)
                break
        stack.append((i, l))
    print(" ".join(map(str, result)))
import sys
def input():
    return sys.stdin.readline().rstrip()


# main
if __name__ == "__main__":
    N = int(input())
    stack = []
    lst = []
    for _ in range(N):
        lst.append(int(input()))
    cnt = 1
    flag = True
    answer = []
    for l in lst:
        if cnt <= l:
            while cnt <= l:
                stack.append(cnt)
                answer.append("+")
                cnt += 1
            stack.pop()
            answer.append("-")
        else:
            if stack.pop() > l:
                print("NO")
                flag = False
                break
            else:
                answer.append("-")
    if flag:
        print("\n".join(answer))
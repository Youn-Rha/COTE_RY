import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    return


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()                              # 최종 결과는 (a, a+b, a+b+c -> 3*a+2*b+1*c)
    total = 0                               # 이므로 결국 맨 앞부터 작은 원소가 와야함
    for i in range(N):
        total += lst[i] * (N - i)           # a, a+b, a+b+c -> 3*a+2*b+1*c
    print(total)
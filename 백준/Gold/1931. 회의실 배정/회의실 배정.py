import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    lst.sort(key=lambda x: (x[1], x[0])) # 회의 끝 시간이 빠른 것부터 / 시작 시간이 빠른 것부터
    tmp = lst[0]
    cnt = 1
    for i, l in enumerate(lst):
        if i == 0:
            continue
        if l[0] >= tmp[1]: # 이전 끝 시간 - 다음 시작 시간 비교
            tmp = l
            cnt += 1
    print(cnt)
import sys


def input():
    return sys.stdin.readline()


def sol():
    lst = set()
    for i in range(1, len(S)):          # 문자의 개수(1개, 2개 ...)
        for j in range(len(S) - i + 1): # 구성된 문자의 개수에 따라 반복되는 횟수
            lst.add(S[j:j + i])

    return len(lst) + 1


# main
if __name__ == "__main__":
    S = input().strip()
    print(sol())

import sys


def input():
    return sys.stdin.readline()


def sol(k):
    return


if __name__ == "__main__":
    N, M = map(int, input().split())
    monster = {}
    for i in range(N):
        tmp = input().strip()
        monster[i + 1] = tmp
        monster[tmp] = i + 1
    for _ in range(M):
        q = input().strip()
        # q 가 숫자일 때는 숫자로 변환하고 숫자가 아닐 때는 그대로 인덱스 찾기
        try:
            q = int(q)
            print(monster[q])
        except Exception:
            print(monster[q])

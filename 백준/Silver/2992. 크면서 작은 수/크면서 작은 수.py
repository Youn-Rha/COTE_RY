import sys


def input():
    return sys.stdin.readline()


def sol(k):
    if k == len(X):
        num.append(int("".join(ans)))  # 문자열을 정수형으로 정답배열에 추가
        return
    for i in range(len(X)):
        if not visited[i]:
            visited[i] = True
            ans[k] = X[i]
            sol(k + 1)
            visited[i] = False


if __name__ == "__main__":
    X = input().strip()
    ans = [""] * len(X)
    visited = [False] * len(X)
    num = []
    sol(0)
    num.sort(reverse=True)              # 정수형으로 저장된 숫자들을 내림차순 정렬
    idx = num.index(int(X))             # X의 바로 앞 문자를 찾기 위한 X의 index 추출
    if idx != 0:                        # idx 0인 경우는 X가 맨 앞에 있을 경우, 즉 X가 가장 큰 경우
        print(num[idx - 1])
    else:
        print(0)

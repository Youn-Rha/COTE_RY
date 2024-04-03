import sys


def input():
    return sys.stdin.readline()


def sol(depth):
    if not visited[depth]:                      # 방문하지 않은 노드만 탐색
        visited[depth] = True                   # 방문 처리
        for c in com[depth]:                    # 연결된 노드 탐색
            if c not in ans and not visited[c]: # 방문 안한 곳 + 정답 배열에 없는 곳
                ans.append(c)
                sol(c)
    else:
        return


if __name__ == "__main__":
    N = int(input())
    T = int(input())
    com = dict()
    ans = []                                    # 1번과 연결된 컴퓨터 모음
    visited = [False] * (N + 1)                 # 방문 여부 확인

    # 그래프 만들기
    for _ in range(T):
        a, b = map(int, input().split())
        if a in com:
            com[a].append(b)
        else:
            com[a] = [b]
        if b in com:
            com[b].append(a)
        else:
            com[b] = [a]
    if 1 in com:
        sol(1)
    print(len(ans))
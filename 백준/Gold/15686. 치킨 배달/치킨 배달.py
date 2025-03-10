import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    def sol(k, idx):        # chicken집의 경우의 수를 백트랙킹으로 구현
        if k == M:
            dis_total = 0
            # 모든 집에 대한 치킨집의 최소 거리 구해서 합하기
            for h in house:
                min_dis = 100
                for c in sel_chicken:
                    # sel_chicken의 인덱스로 chicken 배열의 값 참조하기
                    min_dis = min(min_dis, abs(h[0] - chicken[c][0]) + abs(h[1] - chicken[c][1]))
                dis_total += min_dis
            distance.append(dis_total)
            return
        for i in range(idx, len(chicken)):
            if not visited[i]:
                sel_chicken[k] = i  # sel_chicken = [0, 2, 3] chicken의 인덱스 저장
                visited[i] = True
                sol(k + 1, i)
                visited[i] = False

    N, M = map(int, input().split())
    house = []
    chicken = []
    distance = []
    for i in range(N):
        lst = list(map(int, input().split()))
        for j in range(N):
            if lst[j] == 1:
                house.append((i, j))
            elif lst[j] == 2:
                chicken.append((i, j))
    sel_chicken = [0] * M
    visited = [False] * len(chicken)
    sol(0, 0)
    print(min(distance))
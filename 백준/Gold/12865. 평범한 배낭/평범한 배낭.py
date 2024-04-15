import sys


# sys.setrecursionlimit(100000)

def input():
    return sys.stdin.readline()


# 수업시간에 배운 내용과 달리 각 아이템들을 중복으로 사용할 수 없다!
# main
if __name__ == "__main__":
    N, K = map(int, input().split())
    items = []
    tmp = []
    for _ in range(N):
        items.append(tuple(map(int, input().split())))
    dp = [[0, []] for _ in range(K + 1)]
    for i in range(1, K + 1):
        idx = 0
        for j in range(N):
            # 흔한 냅색 문제의 알고리즘 ([무게만큼 뺀 곳의 가치 + 무게만큼의 가치]가 더 크면 넣는다)
            if items[j][0] <= i and dp[i][0] < dp[i - items[j][0]][0] + items[j][1] and j not in dp[i - items[j][0]][1]:
                dp[i][0] = dp[i - items[j][0]][0] + items[j][1]
                # tmp 배열은 중복 방지를 위해 이전의 가지고 짐을 복사해서 넣어주는 버퍼
                tmp = dp[i - items[j][0]][1].copy()
                tmp.append(j)
                dp[i][1] = tmp.copy()
                tmp.clear()

    dp.sort(key=lambda x: x[0], reverse=True) # 무게에 맞는 아이템 조합이 없을수도 있으므로 내림차순 정렬을 통해 최대값 색출

    print(dp[0][0])

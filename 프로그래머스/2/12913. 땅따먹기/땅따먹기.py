def solution(land):
    n = len(land)
    for i in range(1, n):
        for j in range(4): # 열 개수는 항상 4개로 고정
            # 바로 윗칸에서 자기 자신 인덱스 제외한 나머지들 중에 가장 큰 것 선택
            land[i][j] += max([land[i - 1][x] for x in range(4) if x != j])
    

    return max(land[-1])
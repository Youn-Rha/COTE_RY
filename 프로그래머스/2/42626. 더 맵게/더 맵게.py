import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        min_value = heapq.heappop(scoville)
        if min_value >= K:
            break
        if len(scoville) == 0:
            return -1
        heapq.heappush(scoville, min_value + heapq.heappop(scoville) * 2)
        answer += 1
    
    return answer
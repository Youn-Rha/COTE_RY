def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        
        # 스택이 비어 있지 않고, 이번 시점에서 가격이 내려간 경우
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()       # 가격이 내려간 idx 추출
            answer[idx] = i - idx   # 내려갈 때까지 버튼 기간 입력

        stack.append(i)
        
    # 끝까지 버틴 가격들
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    return answer
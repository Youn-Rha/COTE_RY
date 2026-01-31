import sys
from collections import deque

# 빠른 입출력을 위해 설정
input = sys.stdin.readline

def solve():
    # 1. 입력 받기
    N, L = map(int, input().split())
    arr = list(map(int, input().split()))
    
    # 2. 덱(Deque) 초기화
    # 덱에는 (값, 인덱스) 형태의 튜플을 저장하거나, 인덱스만 저장해도 됩니다.
    # 여기서는 직관적인 이해를 위해 (값, 인덱스)를 저장합니다.
    dq = deque()
    
    # 3. 배열 순회
    for i in range(N):
        curr_num = arr[i]
        
        # [Core 1] 덱의 뒤에서부터 현재 값보다 큰 값들은 모두 제거
        # 이유: 현재 값(curr_num)이 더 작으므로, 기존의 큰 값들은 최솟값 후보 탈락
        while dq and dq[-1][0] > curr_num:
            dq.pop()
        
        # 현재 값과 인덱스를 덱에 추가
        dq.append((curr_num, i))
        
        # [Core 2] 덱의 앞에서부터 윈도우 범위를 벗어난 인덱스 제거
        # 윈도우의 유효 범위: 인덱스 (i - L + 1) 부터 i 까지
        if dq[0][1] <= i - L:
            dq.popleft()
            
        # [Core 3] 덱의 맨 앞이 현재 윈도우의 최솟값
        print(dq[0][0], end=' ')

if __name__ == "__main__":
    solve()
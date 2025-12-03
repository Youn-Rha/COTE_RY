def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    dp_a = [0] * n
    dp_b = [0] * n
    dp_a[0], dp_a[1] = sticker[0], sticker[0] # case 1에서는 1번을 뜯지 않으니까 0번째 최댓값이 그대로 옴
    dp_b[1] = sticker[1]
    
    # case 1 -> 0번째 쓰고 1, n-1(마지막) 번째 안쓰기
    for i in range(2, n - 1):
        dp_a[i] = max(sticker[i] + dp_a[i - 2], dp_a[i - 1]) # 이번거(n번째) 뜯기(n-1번째는 못 뜯음) / 이번거(n번째) 안 뜯기(n-1번째까지 최대인 거 가져오면 됨)
    # case 2 -> 0번째 안쓰고 1, n-1(마지막) 번째 쓰기
    for i in range(2, n):
        dp_b[i] = max(sticker[i] + dp_b[i - 2], dp_b[i - 1]) # 이번거(n번째) 뜯기(n-1번째는 못 뜯음) / 이번거(n번째) 안 뜯기(n-1번째까지 최대인 거 가져오면 됨)

    return max(max(dp_a), max(dp_b))
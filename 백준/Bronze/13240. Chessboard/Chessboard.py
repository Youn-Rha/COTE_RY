n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        if i % 2 == 0: # 짝수번째 줄
            print('*' if j % 2== 0 else '.', end="")
        else:
            print('.' if j % 2== 0 else '*', end="")
    print()
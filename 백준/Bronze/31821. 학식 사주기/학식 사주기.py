n = int(input())
menu = [0] + [int(input()) for _ in range(n)]
m = int(input())
ans = 0
for _ in range(m):
    ans += menu[int(input())]
print(ans)
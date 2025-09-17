n = int(input())
stst = list(input())
j = n-1
ans = 0
for i in range(n//2):
    if j<i:
        break
    if stst[i] != stst[j]:
        ans += 1
    j -= 1
print(ans)
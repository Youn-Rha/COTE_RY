import sys
input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
flag = False
for i in range(n, 0, -1):
    for j in range(i-1):
        if nums[j] > nums[j+1]:
            cnt += 1
            nums[j], nums[j+1] = nums[j+1], nums[j]
            if cnt == k:
                print(" ".join(map(str, nums)))
                exit()
if cnt < k:
    print(-1)
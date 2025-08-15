import math
nums = list(map(int, input().split()))
nums.sort()
a = nums[0]
b = nums[1]
c = nums[2]

if a+b > c:
    print(a+b+c)
else:
    print((a+b)*2-1)
n = int(input())
num_list = list(map(int, input().split()))
x = int(input())
num = [0 for i in range(x)]
cnt = 0
for n in num_list:
	if n < x and x != 2 * n:
		num[n] = 1
		n = x - n
		if num[n] == 1:
			cnt += 1
print(cnt)
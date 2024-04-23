a, b = map(int, input().split())
m, n = 0, 0
if a < b:
	m = a
else:
	m = b
for i in range(m, 0, -1):
	if a % i == 0 and b % i == 0:
		print(i)
		print(int(a * b / i))
		break
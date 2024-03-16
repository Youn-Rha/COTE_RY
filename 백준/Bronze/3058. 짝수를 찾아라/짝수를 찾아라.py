T = int(input())
for i in range(T):
	e = []
	n = list(map(int, input().split()))
	n.sort()
	for i in n:
		if i % 2 == 0:
			e.append(i)
	print(sum(e), e[0])
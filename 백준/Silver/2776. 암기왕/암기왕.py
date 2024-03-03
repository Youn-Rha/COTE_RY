T = int(input())
for i in range(T):
	N = int(input())
	s1 = set(map(int, input().split()))
	M = int(input())
	s2 = list(map(int, input().split()))
	for s in s2:
		if s in s1:
			print(1)
		else:
			print(0)
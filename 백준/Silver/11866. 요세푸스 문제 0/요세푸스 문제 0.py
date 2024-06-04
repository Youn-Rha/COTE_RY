N, K = map(int, input().split())
lst = [i for i in range(1, N + 1)]
idx = (K - 1) % N
print("<", end="")
for i in range(N - 1):
	print("{}, ".format(lst.pop(idx)), end="")
	N -= 1
	idx = (idx + K - 1) % N
print("{}>".format(lst[0]))
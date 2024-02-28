import itertools

N, M = map(int, input().split())
nums = [i for i in range(1, N + 1)]
iter = list(itertools.permutations(nums, M))
for i in iter:
	i = list(i)
	print(*i)
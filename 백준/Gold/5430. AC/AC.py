T = int(input())
for i in range(T):
	inst = input()
	l = int(input())
	a = input()
	if len(a) != 2:
		lst = list(map(int, a[1:-1].split(',')))
	else:
		lst = []
	if inst.count('D') > len(lst):
		print("error")
		continue
	else:
		pivot = 0
		for i in inst:
			if i == 'R' and pivot == 0:
				pivot = -1
			elif i == 'R' and pivot == -1:
				pivot = 0
			else:
				del lst[pivot]
		print('[', end="")
		if pivot == -1:
			lst.reverse()
		print(*lst, sep=',', end="")
		print(']')
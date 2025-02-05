bracket = "()[]"
S = input()
while S != '.':
	balance = []
	lst = []
	for s in S:
		if s in bracket:
			lst.append(s)
	#print(balance)
	flag = 0
	for l in lst:
		if l == '(' or l == "[":
			balance.append(l)
		elif len(balance) != 0 and l == ')':
			if balance[-1] == "(":
				del balance[-1]
			else:
				flag = 1
				break
		elif len(balance) != 0 and l == ']':
			if balance[-1] == "[":
				del balance[-1]
			else:
				flag = 1
				break
		else:
			flag = 1
			break
	if len(balance) == 0 and flag == 0:
		print("yes")
	else:
		print("no")
	S = input()

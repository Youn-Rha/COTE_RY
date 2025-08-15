import sys

def input():
	return sys.stdin.readline()

A, B = input().split()
A = list(A)
a = sum(map(int, A))
B = list(B)
b = sum(map(int, B))
print(a * b)
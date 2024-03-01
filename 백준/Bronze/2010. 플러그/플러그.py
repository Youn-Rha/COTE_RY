import sys

def input():
	return sys.stdin.readline()
	
N = int(input())
total = 1
for i in range(N):
	total = total + int(input()) - 1
print(total)
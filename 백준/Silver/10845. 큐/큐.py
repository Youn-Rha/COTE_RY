import sys


def input():
    return sys.stdin.readline()


queue = list()
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == 'push':
        queue.append(int(s[1]))
    elif s[0] == 'pop':
        if len(queue) != 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(queue))
    elif s[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)

import sys, math

def input():
    return sys.stdin.readline()
# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        a, b = input().split()
        print(bin(int('0b' + a, 2) + int('0b' + b, 2))[2:])
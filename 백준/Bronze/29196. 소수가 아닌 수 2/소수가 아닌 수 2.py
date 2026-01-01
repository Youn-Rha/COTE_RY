import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    k = float(input())
    k *= 10 ** 8
    print("YES")
    print(int(k), 10 ** 8)
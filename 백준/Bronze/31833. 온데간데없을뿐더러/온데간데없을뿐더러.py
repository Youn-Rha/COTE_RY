import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    X = "".join(input().split())
    Y = "".join(input().split())
    if int(X) > int(Y):
        print(Y)
    else:
        print(X)
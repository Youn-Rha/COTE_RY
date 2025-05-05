import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    lst = list(map(int, input().split()))
    if lst.count(0) >= len(lst) / 2:
        print("INVALID")
    else:
        if lst.count(1) > lst.count(-1):
            print("APPROVED")
        else:
            print("REJECTED")
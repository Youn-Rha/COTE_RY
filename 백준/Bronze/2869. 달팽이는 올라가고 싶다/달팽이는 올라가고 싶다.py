import sys

def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    A, B, V = map(int, input().split())
    t = A-B
    day = 0
    V -= B
    day += V // (A-B)
    if V % (A - B):
        day += 1
    print(day)
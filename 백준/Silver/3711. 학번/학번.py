import sys


def input():
    return sys.stdin.readline()


# main
if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        G = int(input())
        lst = []
        for _ in range(G):
            lst.append(int(input()))
        m = 1
        lst_set = set()
        while True:
            for l in lst:
                lst_set.add(l % m)
            if len(lst_set) == len(lst):
                break
            else:
                m += 1
                lst_set.clear()
        print(m)
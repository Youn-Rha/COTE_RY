import sys


def input():
    return sys.stdin.readline()


def recur(depth):
    return


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        fashion = dict()
        for _ in range(n):
            name, type = input().split()
            if type in fashion:
                fashion[type].append(name)
            else:
                fashion[type] = [name]
        f_val = list(fashion.values())
        if len(fashion.keys()) == 1:
            print(len(f_val[0]))
        else:
            cnt = 1
            for v in f_val:
                cnt *= (len(v) + 1)
            print(cnt - 1)

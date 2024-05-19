import sys

# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline()


def factorization(n):
    result = dict()
    while n % 2 == 0:
        n /= 2
        if 2 in result:
            result[2] += 1
        else:
            result[2] = 1
    p = 3
    while p * p <= n:
        while n % p == 0:
            n /= p
            if p in result:
                result[p] += 1
            else:
                result[p] = 1
        p += 2

    if n > 2:
        if n in result:
            result[int(n)] += 1
        else:
            result[int(n)] = 1
    return result


# main
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        result = list(factorization(int(input())).items())
        result.sort(key=lambda x:x[0])
        for r in result:
            print(r[0], r[1])
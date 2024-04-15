import itertools


# 조건 체크
def check(l: list):
    vowels = 'aeiou'
    a = 0 # 자음 개수
    b = 0 # 모음 개수
    for alphabet in l:
        if alphabet in vowels:
            b += 1
        else:
            a += 1
    if a < 2 or b < 1:
        return 0
    else:
        return 1


L, C = map(int, input().split())
char = list(input().split())
char.sort()
password = tuple(itertools.combinations(char, L))
for word in password:
    if check(word):
        print("".join(word))


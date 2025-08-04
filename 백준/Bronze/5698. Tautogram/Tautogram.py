s = list(input().split())
while s != ['*']:
    flag = True
    for i in range(len(s)-1):
        if s[i][:1].upper() != s[i+1][:1].upper():
            print('N')
            flag = False
            break
    if flag:
        print('Y')
    s = list(input().split())
    
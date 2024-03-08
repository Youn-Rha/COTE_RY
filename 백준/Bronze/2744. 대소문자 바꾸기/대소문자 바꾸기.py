S = input().strip()
for s in S:
    if s.isupper():
        print(s.lower(), end="")
    else:
        print(s.upper(), end="")
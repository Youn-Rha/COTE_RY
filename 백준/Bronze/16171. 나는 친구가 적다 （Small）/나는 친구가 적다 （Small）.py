a = input()
b = input()
for i in range(10):
    a = a.replace(str(i), "")

if a.count(b):
    print(1)
else:
    print(0)
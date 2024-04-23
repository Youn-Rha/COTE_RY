def gcd(a, b):
    if a < b:
        temp = b
        b = a
        a = temp
    if a % b == 0:
        return b
    return gcd(b, a % b)


m, n = map(int, input().split())
g = gcd(m, n)
print(int(g * (m / g) * (n / g)))

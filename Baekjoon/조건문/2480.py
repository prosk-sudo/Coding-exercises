def prize(a, b, c):
    d, e, f = sorted([a, b, c])

    if d == f:
        return 10000 + d * 1000
    if d == e or e == f:
        return 1000 + e * 100
    return f * 100

a, b, c = map(int, input().split())
print(prize(a, b, c))

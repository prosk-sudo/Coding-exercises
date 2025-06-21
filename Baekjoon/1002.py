num_test = int(input())
res = []

for _ in range(num_test):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
    res.append(
        -1 if d_squared == 0 and r1 == r2
        else 0 if d_squared > (r1 + r2) ** 2 or d_squared < (r1 - r2) ** 2
        else 1 if d_squared == (r1 + r2) ** 2 or d_squared == (r1 - r2) ** 2
        else 2
    )

for tc in res:
    print(tc)

lst = [(1, 0), (0, 1)]

for i in range(2, 41):
    z0, o0 = lst[i-2]
    z1, o1 = lst[i-1]
    lst.append((z0 + z1, o0 + o1))

T = int(input())
for _ in range(T):
    N = int(input())
    zero, one = lst[N]
    print(zero, one)

n1 = int(input())
n2 = int(input())

print(f"{n1*(n2%10)}\n{n1*((n2%100)//10)}\n{n1*(n2//100)}\n{n1*n2}")

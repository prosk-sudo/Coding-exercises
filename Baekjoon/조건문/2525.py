A, B = map(int, input().split())
C = int(input())
after_C_in_min = (A*60+B+C+1440) % 1440
print(f"{after_C_in_min // 60} {after_C_in_min % 60}")

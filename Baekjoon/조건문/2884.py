h, m = map(int, input().split())
in_minutes = (h*60+m+1395) % 1440
print(f"{in_minutes // 60} {in_minutes % 60}")

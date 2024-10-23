a, b = map(int, input().split())

f = 1 if a < b else 0
s = 1 if a == b else 0

print(f"{f} {s}")
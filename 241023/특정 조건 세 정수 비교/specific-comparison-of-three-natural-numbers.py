a, b, c = map(int, input().split())

# a, b, c -> a : 1 -> b, c 

minValues = min(a,b,c)

f = 1 if a == minValues else 0
s = 1 if a == b and a == c and b == c else 0

print(f"{f} {s}")
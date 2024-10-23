n, m = map(int,input().split())

if n >= 90:
    if 95 <= m <= 100:
        print('100000')
    elif m >= 90: 
        print('50000')
else:
    print('0')
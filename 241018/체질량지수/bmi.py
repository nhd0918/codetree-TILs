h, w = map(int,input().split())

## cm -> m, 1.78
## 키 168 cm(=1.68 m)인 사람의 BMI는 55 kg/(1.68 m)² = 19.4

h /= 100
b = w / (h * h)

if b >= 25:
    print( int(b) )
    print("Obesity")
else:
    print( int(b) )
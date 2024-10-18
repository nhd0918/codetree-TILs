a, b = map(int, input().split())

# 조건에 따라 결과 출력
if a >= b:
    print(a * b)  # a가 b보다 크면 두 수의 곱 출력
else:
    if b != 0:
        print(a // b)  # b가 0이 아닐 때만 a를 b로 나눈 몫 출력
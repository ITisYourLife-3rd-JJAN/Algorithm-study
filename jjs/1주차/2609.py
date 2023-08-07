n, m = map(int, input().split())

# 유클리드 호제법
# 최대공약수 구하기
# n을 m으로 나눈 나머지를 구한 뒤
# m을 나머지로 나눈 나머지를 구하는 식을 반복
def max(n, m):
    while m > 0:
        n, m = m, n % m
    return n

# 최소공배수 구하기
# n과 m을 곱한 뒤 최대공약수로 나누어 최소가 맞는지 확인
def min(n, m):
    return n * m // max(n, m)

print(max(n, m))
print(min(n, m))
# math 모듈 이용하여 최대공약수 구하기
from math import gcd

n, m = map(int, input().split())

lst = list(map(int, input().split()))
max = abs(m-lst[0])
# 동생들의 위치 탐색하고 최대공약수 연산 수행

for i in lst[1:]:
    max = gcd(abs(i-m), max) # 마지막 연산의 값이 모든 값의 최대 공약수가 된다

print(max)


# def realgcd(n, m):
#     while m > 0:
#         n, m = m, n % m
#     return n
#
# if m == 1:
#     print(max)
# else:
#     for i in range(1, n):
#         max = realgcd(max, abs(m-lst[i]))
#     print(max)
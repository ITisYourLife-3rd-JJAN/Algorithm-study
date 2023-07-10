from math import gcd

n, m = map(int, input().split())

lst = list(map(int, input().split()))
max = abs(m-lst[0])

for i in lst[1:]:
    max = gcd(abs(i-m), max)

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
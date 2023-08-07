N, S, R = map(int, input().split())

D = list(map(int, input().split()))
A = list(map(int, input().split()))

result = 0

for i in D:
    if i - 1 in A:
        A.remove(i - 1)
    elif i + 1 in A:
        A.remove(i + 1)
    else:
        result += 1

print(result)
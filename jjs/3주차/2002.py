N = int(input())

result = 0
dict = dict()
arr = []

for i in range(N):
    car = input()
    dict[car] = i

for _ in range(N):
    car = input()
    arr.append(car)

for k in range(N - 1):
    for h in range(k + 1, N):
        if dict[arr[k]] > dict[arr[h]]:
            result += 1
            break

print(result)
N = int(input())

arr = []
dict = {}

for _ in range(N):
    name = input().split(".")
    print(name)
    arr.append(name[1])

for i in arr:
    if dict.get(i):
        dict[i] += 1
    else:
        dict[i] = 1

dict = sorted(dict.items())

for k, h in dict:
    print(k, h)
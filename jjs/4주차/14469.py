N = int(input())

arr = []
for _ in range(N):
    k, h = map(int, input().split())
    arr.append([k, h])

arr.sort()

t = 0
for i in range(len(arr)):
    if t > arr[i][0]:
        t = t + arr[i][1]
    else:
        t = arr[i][0] + arr[i][1]

print(t)
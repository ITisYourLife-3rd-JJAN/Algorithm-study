N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

tip = 0
for i in range(N):
    t = arr[i] - i
    if t > 0:
        tip += t

print(tip)
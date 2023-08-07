N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()

rank = 0
for i in range(1, N + 1):
    rank += abs(i - arr[i - 1])

print(rank)
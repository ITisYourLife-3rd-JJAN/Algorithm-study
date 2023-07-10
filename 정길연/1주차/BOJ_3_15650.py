from itertools import combinations

n, m = map(int, input().split())

nums = [i for i in range(1, n + 1)]

for seq in combinations(nums, m):
    print(*seq)
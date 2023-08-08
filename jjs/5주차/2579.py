N = int(input())

arr = [0] * 301
for i in range(N):
    arr[i] = int(input())

dp = [0] * 301
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]) # 연속 3칸을 모두 오를 수 없기 때문에 선택 단, 마지막 계단은 반드시 밟아야 함

for i in range(3, N):# 4칸 이상일 경우 고려해야 할 것들
    # 두번째 칸 까지 밟은 후 세번째를 건너 뛰고 마지막 칸 오르는 경우 -> dp[i - 2] + arr[i]
    # 두번째 칸 건너 뛰고 세번째 칸과 마지막 칸을 오르는 경우 -> dp[i - 3] + arr[i - 1] + arr[i]
    dp[i] = max(dp[i - 2], dp[i - 3] + arr[i - 1]) + arr[i]

# 이 중 최대가 되는 dp를 구하면 됨
print(max(dp))
N = int(input())

arr = [0] * 10001
for i in range(N):
    arr[i] = int(input())

dp = [0] * 10001
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max(dp[1], arr[0] + arr[2], arr[1] + arr[2]) # 연속 3잔을 모두 마실 수 없기 때문에 선택

for i in range(3, N): # 4잔 이상일 경우 고려해야 할 것들
    # 마지막 잔을 마시지 않는 경우 -> dp[i - 1]
    # 두번째 잔 까지 선택한 후 세번째를 건너 뛰고 마지막 잔 마시는 경우 -> dp[i - 2] + arr[i]
    # 두번째 잔 건너 뛰고 세번째 잔과 마지막 잔을 마시는 경우 -> dp[i - 3] + arr[i - 1] + arr[i]
    dp[i] = max(dp[i - 1], dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i])

# 이 중 최대가 되는 dp를 구하면 됨
print(max(dp))
N = int(input())
lst = list(map(int, input().split()))

dp = [1] * N # 혼자일 때는 길이가 1이므로 1로 초기화
for i in range(N):
    for j in range(i):
        if lst[i] < lst[j]: # 감소하려면 앞의 수가 다음 수보다 커야함
            dp[i] = max(dp[i], dp[j] + 1) # 앞 숫자의 부분 수열 길이에 1을 더한 값이 나의 부분 수열 길이이고 이 중 가장 긴 값이 dp

print(max(dp))
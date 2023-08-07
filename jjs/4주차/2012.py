N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort() # 기대 등수 정렬

rank = 0
for i in range(1, N + 1): # 1등부터 N등까지 순회
    rank += abs(i - arr[i - 1]) # 예상 등수에서 실제 등수를 뺀 절대값이 불만족도가 되고 이를 누적

print(rank)
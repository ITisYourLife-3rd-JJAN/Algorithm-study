N = int(input())

arr = []
for _ in range(N):
    k, h = map(int, input().split())
    arr.append([k, h]) # 2차원 배열로 소 받기

arr.sort() # 먼저 도착한 소 부터 정렬

t = 0
for i in range(len(arr)):
    if t > arr[i][0]: # 앞소가 검문받고있을 경우
        t = t + arr[i][1] # 앞소 소요 초 + 뒷소 검문 초
    else: # 앞소가 검문이 끝나고 갔을 경우
        t = arr[i][0] + arr[i][1] # 뒷소가 도착한 초 + 검문 초

print(t)
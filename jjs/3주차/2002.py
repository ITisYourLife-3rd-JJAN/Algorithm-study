N = int(input())

result = 0
dict = dict()
arr = []

for i in range(N):
    car = input()
    dict[car] = i # 들어가는 차 저장

for _ in range(N):
    car = input()
    arr.append(car) # 나오는 차 저장

for k in range(N - 1): # 나오는 차를 탐색
    for h in range(k + 1, N):
        if dict[arr[k]] > dict[arr[h]]: # 현재 자동차의 인덱스보다 작은 차가 있을 경우
            result += 1 # 카운트해준다
            break

print(result)
N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True) # 팁 많이 주는 사람 순으로 정렬

tip = 0
for i in range(N):
    t = arr[i] - i # 주려고 하는 팁 - (등수 - 1) 에서 (등수 - 1) 부분은 0, 1, 2 순으로 가기 때문에 인덱스와 같음
    if t > 0: # 팁 계산 결과가 양수라면
        tip += t # 누적

print(tip)
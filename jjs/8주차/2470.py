N = int(input())
lst = list(map(int, input().split()))
lst.sort() # 입력값을 오름차순으로 정렬

s = 0 # 먼저 포인터 두개를 왼쪽 끝, 오른쪽 끝으로 정해줌
e = N - 1

ans = abs(lst[s] + lst[e]) # 양 끝을 더한 값을 기본으로 설정
result = [lst[s], lst[e]] # 위치를 기억 할 배열 필요

while s < e: # 두 포인터가 만나기 직전까지 반복문 돌리기
    left = lst[s]
    right = lst[e]

    val = left + right # 시작지점과 종료지점의 값을 더한 뒤

    if abs(val) < ans: # 이것을 절대값으로 변경하고 기본값과 비교하여 만약 기본값보다 작다(즉 0과 가깝다)면
        ans = abs(val) # ans에 새로운 값 저장
        result = [left, right] # 마찬가지로 위치도 업데이트
        if ans == 0: # 만약 ans가 0 이 되면 가장 좋은 값이 나온것이기 때문에 종료
            break

    if val < 0: # 만약 밸류값이 음수라면 시작 지점을 오른쪽으로 한 칸 당김
        s += 1
    else: # 양수라면 종료 지점을 왼쪽으로 한 칸 당김
        e -= 1

print(result[0], result[1])
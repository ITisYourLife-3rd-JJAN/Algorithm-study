for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort() # 입력 받은 수들을 비교하기 편하도록 정렬
    B.sort()

    cnt = 0
    result = 0

    for i in range(N): # A의 크기만큼 for문 돌리기
        while True:
            if cnt == M or A[i] <= B[cnt]: # cnt == M 즉 A[i]가 B의 모든 원소보다 큼 또는 A[i]번째 수가 B[cnt]번째 수보다 작거나 같을 경우
                result += cnt # 결과값에 cnt를 더해줌
                break # A[0], A[1]은 1 이므로 B[cnt] = 1일 때 까지 계속 만족 후 브레이크
            else: # A[2]가 되면 3 <= 1이 불만족하므로
                cnt += 1 # cnt + 1이 됨

    print(result)
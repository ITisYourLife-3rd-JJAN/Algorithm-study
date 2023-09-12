N, K = map(int, input().split())
kit = list(map(int, input().split()))

cnt = 0
check = [0] * N

def dfs(d, now): # 현재 날짜와 현재 무게 사용
    global cnt

    if now < 0: # 현재 무게가 음수가 되면 안되므로
        return # 바로 리턴
    if d >= N: # 위의 조건을 잘 통과하고 운동 일수가 N이상이 되면 cnt 올려줌
        cnt += 1
        return

    for i in range(N):
        if check[i] == 0:
            check[i] = 1 # 쓴 키트 체크해주기
            dfs(d + 1, now + kit[i] - K) # 현재 근육량 + 키트 중량 - K 가 0 이상일때만 dfs 진입
            # 첫번째 테케의 경우 dfs(1, 0 + 3 - 4) 즉 1, -1이 되기 때문에 바로 리턴됨
            # 두번째 테케의 경우 dfs(1, 0 + 7 - 4) 즉 1, 3이 되기 때문에 조건을 만족함
            # 세번째 테케의 경우 dfs(2, 3 + 3 - 4) 즉 2, 2가 되기 때문에 조건을 만족함
            # 네번째 테케의 경우 dfs(3, 2 + 5 - 4) 즉 3, 3이 되기 때문에 조건을 만족함 => 여기까지 2 1 3 순으로 진행
            # 그럼이제 다시 2 3 1 순서로 진행되고 또 넘어가고 하는 식으로 진행
            check[i] = 0 # 다시 0으로 바꿔줌

dfs(0, 0)

print(cnt)
N = int(input())
lst = [list(map(int, input())) for _ in range(N)]

cnt = 0
num = [] # 결과 담을 리스트

dx = [0, 1, -1, 0] # 상 하 좌 우 탐색
dy = [1, 0, 0, -1]

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N: # 범위 벗어 날 경우
        return

    if lst[x][y] == 1: # 집이 있다면
        global cnt
        cnt += 1 # 방문 한 횟수 저장
        lst[x][y] = 0 # 방문 한 집 0으로 만들기
        for i in range(4): # 상 하 좌 우 탐색하면서 다시 dfs 돌림
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1: # 그래프의 원소가 1일때만 dfs로 집 방문
            dfs(i, j)
            num.append(cnt) # 각 단지를 돌면서 단지의 집 수를 세어줌
            cnt = 0

num.sort() # 오름차순 정력 해줌

print(len(num)) # 총 단지 수
for i in num:
    print(i)
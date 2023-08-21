from collections import deque

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]
for _ in range(K):
    X1, Y1, X2, Y2 = map(int, input().split())
    for Y in range(Y1, Y2):
        for X in range(X1, X2):
            graph[Y][X] = 1

dx = [0, 1, -1, 0] # 상 하 좌 우 탐색
dy = [1, 0, 0, -1]
cnt = 1
area = 0
result = []

def dfs(y, x):
    global cnt
    graph[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N and graph[ny][nx] == 0:
            cnt += 1
            dfs(ny, nx)

for Y in range(M):
    for j in range(N):
        if graph[Y][X] == 0:
            area += 1
            dfs(Y, X)
            result.append(cnt)
            cnt = 1

result.sort()
print(len(result))
for i in result:
    print(i, end=' ')
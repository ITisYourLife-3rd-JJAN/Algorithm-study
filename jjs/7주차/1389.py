from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)] # 노드의 연결을 담아줄 배열이 필요함
lst = [] # 케빈 베이컨 수 담아줄 리스트가 필요함
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 친구 사이의 관계를 양방향으로 저장
    graph[b].append(a)
    # 플로이드식으로 표현하려면 배열에서 graph[a][b] = 1 이런식으로 표현해주면 됨

def bfs(v):
    queue = deque([v])
    visit[v] = 1

    while queue:
        t = queue.popleft()
        for i in graph[t]: # 친구 관계를 탐색하는데
            if not visit[i]: # 만약 아직 탐색하지 않은 친구라면
                visit[i] = visit[t] + 1 # 탐색하고 횟수 체크
                queue.append(i)

for i in range(1, N + 1): # 반복하며 모든 친구 탐색
    visit  = [0] * (N + 1)
    bfs(i)
    lst.append(sum(visit)) # 리스트에 결과 넣어줌

print(lst.index(min(lst)) + 1) # 가장 작은 케빈 베이컨의 인덱스에 +1 하면 그 사람의 번호
from heapq import heappush, heappop

N = int(input())
M = int(input())

I = int(1e9) # 무한대로 설정
d = [I] * (N + 1) # 최단거리 테이블(각 도시 사이의 거리를 무한대로 초기화)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split()) # a 에서 b로 가는 비용 c
    graph[a].append((b, c))

S, E = map(int, input().split())

def dstra(S):
    heap = [] # 최소힙 이용
    heappush(heap, (0, S))
    d[S] = 0 # 시작 지점 0으로 초기화

    while heap:
        dist, now = heappop(heap) # 최단거리 짧은 노드 정보 꺼내기

        if d[now] < dist: # 만약 이미 꺼낸 노드였다면
            continue # 무시하고 지속

        for i in graph[now]: # 선택 된 노드와 인접한 노드를 확인하고
            cost = dist + i[1]

            if cost < d[i[0]]: # 만약 선택 된 노드를 거쳐서 이동하는 것이 더 빠르면
                d[i[0]] = cost # 비용 저장해줌
                heappush(heap, (cost, i[0]))

dstra(S)

print(d[E])
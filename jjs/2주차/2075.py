import heapq

N = int(input())
hq = []

for _ in range(N):
    lst = list(map(int, input().split()))

    if not hq:
        for i in lst:
            # 우선순위 큐 안에 push
            heapq.heappush(hq, i)
    else:
        # 만약 큐가 꽉 찼다면
        for i in lst:
            if hq[0] < i: # 크기 비교 해서
                heapq.heappop(hq) # 하나 빼주고
                heapq.heappush(hq, i) # 넣어주기

print(hq[0])
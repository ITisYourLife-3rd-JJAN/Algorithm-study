import heapq

n = int(input())        # n번쨰 큰수 찾기

heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    if not heap:
        for num in nums:
            heapq.heappush(heap, num)
    else:
        for num in nums:
            if heap[0] < num:     # heap[0]==최솟값
                heapq.heappush(heap, num)
                heapq.heappop(heap)
                

print(heap[0])
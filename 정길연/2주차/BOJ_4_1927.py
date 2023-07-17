import sys
input = sys.stdin.readline

import heapq

heap = []
N = int(input())

for _ in range(N):
    num = int(input())
    
    if num == 0:      # 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
        if len(heap):
            print(heapq.heappop(heap))
        else:   
            print(0)
    else:           # 자연수라면 배열에 x라는 값을 추가
        heapq.heappush(heap, num)
from collections import deque

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idx = 0

    while queue:
        max_item = max(queue)   # 현재의 최댓값이 가장 먼저 인쇄되므로, 최댓값 저장
        item = queue.popleft() 
        m -= 1                  # 앞에 것을 뽑았으니 순서가 1개 당겨짐

        if max_item == item:    # 뽑은 숫자가 제일 큰 숫자일 때
            idx += 1           
            if m < 0:           
                print(idx)
                break

        else:                   # 뽑은 숫자가 제일 큰 숫자가 아니면, 제일 뒤로
            queue.append(item) 
            if m < 0 :          # 제일 앞에서 뽑히면, 제일 뒤로 
                m = len(queue) - 1  

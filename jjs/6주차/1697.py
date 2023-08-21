from collections import deque

N , K = map(int, input().split())

max = 1000001
arr = [0] * max

def bfs():
    q = deque() # deque 양쪽에서 입/출력 가능
    q.append(N) # q = deque([5])
    while q:
        x = q.popleft() # 첫 시작점이 x = 5, q = deque([])
        if x == K: # 수빈이 위치가 동생이 있는 K 와 같아지면
            print(arr[x]) # 얼마 걸렸는지 프린트 후 종료
            break

        for i in (x - 1, x + 1, x * 2): # i = 4, 6, 10
            if 0 <= i <= max and not arr[i]: # arr[i]는 0 즉 false
                arr[i] = arr[x] + 1 # arr[4, 6, 10] = arr[5] + 1 즉 1
                q.append(i) # q = deque([4, 6, "10"]) => arr[9, 11, 20] 반복 해서 arr[17, 19, 36] = arr[18] + 1 = 3 + 1 = 4

bfs()
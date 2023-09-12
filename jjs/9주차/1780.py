N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
arr = [0, 0, 0]

def nine(r, c, N):
    num = lst[r][c]
    for i in range(r, r + N):
        for j in range(c, c + N):
            if lst[i][j] != num: # 시작 종이의 수가 현재 종이의 수와 다르다면
                for k in range(3): # 3x3 범위 탐색
                    for l in range(3):
                        nine(r + k * (N // 3), c + l * (N // 3), N // 3) # 0,3
                return

    if num == -1: # -1, 0, 1 각 수를 어레이에 카운트해줌
        arr[0] += 1
    elif num == 0:
        arr[1] += 1
    else:
        arr[2] += 1

nine(0, 0, N)
for i in range(len(arr)):
    print(arr[i])
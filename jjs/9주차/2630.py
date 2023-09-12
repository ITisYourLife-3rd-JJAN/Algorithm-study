N = int(input())

lst = [list(map(int, input().split())) for _ in range(N)]
z, o = 0, 0

def cut(x, y, N):
    global z, o
    check = lst[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != lst[i][j]: # 만약 조건을 만족하지 않는다면 다시 4개로 쪼갬
                n = N // 2
                cut(x, y, n)  # 오른쪽 위
                cut(x, y + n, n)  # 왼쪽 위
                cut(x + n, y, n)  # 오른쪽 아래
                cut(x + n, y + n, n)  # 왼쪽 아래
                return

    if check == 0:
        z += 1
    else:
        o += 1


cut(0, 0, N)
print(z)
print(o)
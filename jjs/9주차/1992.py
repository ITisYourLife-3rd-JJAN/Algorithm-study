N = int(input())

lst = [list(map(int, input())) for _ in range(N)]

def cut(x, y, N):
    check = lst[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if check != lst[i][j]: # 만약 조건을 만족하지 않는다면 다시 4개로 쪼갬
                print("(", end='') # 각 분할 시작과 끝에 괄호 넣어줌
                n = N // 2
                cut(x, y, n)  # 오른쪽 위
                cut(x, y + n, n)  # 왼쪽 위
                cut(x + n, y, n)  # 오른쪽 아래
                cut(x + n, y + n, n)  # 왼쪽 아래
                print(")", end='')
                return

    if check == 1: # 조건을 만족하는 경우 값을 그대로 뽑아줌
        print(1, end='')
    else:
        print(0, end='')


cut(0, 0, N)
mine = [list(map(int, input().split())) for _ in range(5)]
ans = []
for _ in range(5):
    ans += list(map(int, input().split()))

cnt = 0

def check():
    bingo = 0

    for r in mine: # 가로 확인
        if r.count(0) == 5: # mine을 한 줄씩 탐색하는데 만약 r번째 행에서 0이 5번 카운트 된다면 가로로 한줄 빙고라는 뜻
            bingo += 1

    c = 0
    for i in range(5): # 세로 확인
        for j in range(5):
            if mine[j][i] == 0: # mine을 세로로 한 줄씩 탐색해서 만약 0이 있다면 c에 갯수 세어주고
                c += 1
        if c == 5: # 세로줄에 0의 갯수가 5개라면 빙고
            bingo += 1

    ld = 0
    for i in range(5): # 왼 -> 오 대각선 확인
        if mine[i][i] == 0: # [i][i] 대각선 방향으로 탐색해서 만약 0이 있다면 ld에 갯수 세어주고
            ld += 1
    if ld == 5: # 대각선에 0의 갯수가 5개라면 빙고
        bingo += 1

    rd = 0
    for i in range(5): # 오 -> 왼 대각선 확인
        if mine[i][4 - i] == 0: # [i][4 - i] 대각선 방향으로 탐색해서 만약 0이 있다면 ld에 갯수 세어주고
            rd += 1
    if rd == 5: # 대각선에 0의 갯수가 5개라면 빙고
        bingo += 1

    return bingo



for i in range(25): # 사회자가 총 25개의 숫자 부름
    for r in range(5):
        for c in range(5):
            if ans[i] == mine[r][c]: # 같은 수를 찾았다면
                mine[r][c] = 0 # 해당 자리를 0으로 변경하고
                cnt += 1 # 부른 숫자 카운트

    if cnt >= 12: # 만약 카운트 값이 12 이상이라면 즉, 3빙고가 성립하기 위한 최소한의 수라면
        result = check() # 빙고 갯수를 세어보고
        if result >= 3: # 3 이상이라면 출력한다
            print(cnt)
            break
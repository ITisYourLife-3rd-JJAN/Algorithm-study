from itertools import permutations

N = int(input())

num = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3)) # 1~9 까지 모든 수 중 3개를 조합 한 리스트

for _ in range(N):
    ipt, s, b = map(int, input().split())
    ipt = list(str(ipt))
    rm_cnt = 0

    for i in range(len(num)):
        strike, ball = 0, 0
        i -= rm_cnt # 매번 돌 때 마다 조합 리스트의 첫번째 원소부터 비교해주기 위해 리무브 카운트를 빼고 num[0] 부터 시작
        for j in range(3):
            if num[i][j] == ipt[j]: # 만약 민혁이가 말한 수가 존재하고 자리까지 일치한다면
                strike += 1 # 스트라이크 추가
            elif ipt[j] in num[i]: # 만약 민혁이가 말한 수가 조합에 포함되어 있다면
                ball += 1 # 볼 추가

        if (strike != s) or (ball != b): # 만약 민혁이가 말한 수가 주어진 스트라이크, 볼 갯수와 일치하지 않는다면
            num.remove(num[i]) # 해당 조합은 리무브시켜줌
            rm_cnt += 1 # 리무브한 것 체크

print(len(num))
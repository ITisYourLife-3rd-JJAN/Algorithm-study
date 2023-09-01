S, P  = map(int, input().split())
lst = list(str(input()))
a, c, g, t = map(int, input().split())

dic = {"A": 0, "C": 0, "G": 0, "T": 0} # 문자를 세기 위한 딕셔너리 만들기
start = lst[:P] # 0부터 P-1 즉 P개의 문자로 시작

for i in start: # start의 문자를 하나씩 dic에 세어줌
    dic[i] += 1

cnt = 0
if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
    cnt += 1 # 만약 기본 시작 조건이 만족한다면 카운트

s_idx = 0 # 시작지점 지정
e_idx = s_idx + P # 종료지점 지정

for i in range(len(lst) - P): # lst의 길이에서 P를 빼준 것 만큼 돌아야 함 즉 9-8=1 이므로
    dic[lst[s_idx + i]] -= 1 # 기존 구간에서 시작 지점 하나를 빼주고
    dic[lst[e_idx + i]] += 1 # 종료 지점 하나를 더해줌
    if dic["A"] >= a and dic["C"] >= c and dic["G"] >= g and dic["T"] >= t:
        cnt += 1 # 그리고 다시 조건이 만족하는지 체크한 후 카운트

print(cnt)
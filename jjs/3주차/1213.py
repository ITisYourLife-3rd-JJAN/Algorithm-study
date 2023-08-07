from collections import Counter

N = list(map(str, input()))
N.sort()

cnt = Counter(N) # 각 알파벳의 개수 세어줌
odd = 0
c_word = ""

for i in cnt:
    if cnt[i] % 2 == 1: #만약 홀수라면
        odd += 1 # 홀수가 몇개인지 세어줌
        c_word += i # 홀수인 문자 더해줌
        N.remove(i) # 사용한 문자 제거

    if odd > 1: # 만약 홀수가 여러개라면 넌 탈락
        print("I'm Sorry Hansoo")
        break

result = "" # 글자를 넣을 빈 문자열

if odd == 1: # 만약 홀수가 한개라면 가운데 글자가 정해지고
    words = ""
    for i in range(0, len(N), 2): # 같은글자 두개씩 반복이니까 간격 지정해서 더해주기
        words += N[i]
    result = words + c_word + words[::-1] # 가운데 글자 넣고 거꾸로 반복

print(result)
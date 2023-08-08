N = int(input())

arr = []
dict = {}

for _ in range(N):
    name = input().split(".") # .기준으로 입력 받아
    arr.append(name[1]) # 인덱스1번인 확장자만 따로 저장
print(name)
print(arr)
for i in arr:
    # 밸류값 리턴하는 딕셔너리 get 메소드 활용하여 카운트
    if dict.get(i): # 딕셔너리에 i가 있으면
        dict[i] += 1 # 1더해줌
    else: # 없으면 최초 카운트
        dict[i] = 1

dict = sorted(dict.items()) # 키값 알파벳 순으로 정렬

for k, h in dict:
    print(k, h)
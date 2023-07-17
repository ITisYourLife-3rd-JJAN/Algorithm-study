def gcd(a, b):  #유클리드 호제법 gcd
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

n,s = map(int, input().split())  
brothers = list(map(int, input().split())) 

li = []
for i in range(n): 
    if brothers[i]-s >= 0:  #수빈이 현재 위치와 동생 위치의 차이를 append
        li.append(brothers[i]-s)
    else:  # 0보다 작으면 절댓값
        li.append(abs(brothers[i] - s))


li2=[]
if n==1:
    print(li[0]) 
else:
    for i in range(n):
        if i+1 < len(li):
            li2.append(gcd(li[i], li[i+1]))  #최소공배수 
        else:
            pass
    print(min(li2))  # 최소공배수
